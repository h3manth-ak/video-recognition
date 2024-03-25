from fastapi import FastAPI,File,UploadFile
from secrets import token_hex
from fastapi.middleware.cors import CORSMiddleware
import os
import uvicorn
from pydantic import BaseModel
from ultralytics import YOLO
from frame_extraction_obj import VideoFrameExtractor
from xttym import VideoTimestamp
import numpy as np
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from genai import GenerativeModelWrapper
from dotenv import load_dotenv



load_dotenv()
API_KEY = os.getenv("API_KEY")
cur_direrctory=os.path.dirname(os.path.abspath(__file__))
# print(cur_direrctory)
origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:8080",
    "http://localhost:3000/"
]

app = FastAPI(title="File Upload API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
model_obj = YOLO('yolov8n.pt')
file_path = ''
file_name = ''
file_ext = ''

class url_ip1(BaseModel):
    url1:str

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...) ):
    global file_path,file_name,file_ext
    file_ext=file.filename.split(".").pop()
    file_name=file.filename.split(".")[0]
    file_path=f"{cur_direrctory}/{file_name}.{file_ext}" 
    # file_path=f"{file_name}.{file_ext}"
    with open(file_path,"wb") as buffer:
        content=await file.read()
        buffer.write(content)
    
    
    
    
    return {"success":True,"file_path":file_path,"message":"File uploaded successfully"}



# @app.post("/prompt"):
# async def prompt():
#     return {"success":True,"message":"Server is running"}


@app.post('/analyze')
def phish_url(request:url_ip1):
    global file_path,file_name,file_ext
    url_ip = request.url1
    # print(file_path)
    model_wrapper = GenerativeModelWrapper(API_KEY)
    prompt = url_ip
    response_text = model_wrapper.generate_response(prompt)
    print(response_text)
    frame_extractor = VideoFrameExtractor(file_path)

    frames = frame_extractor.get_frames()
    counter = 0
    names=model_obj.names
    ts=[]
    video_timestamp = VideoTimestamp(file_path)
    for frame in frames:
        counter += 1
        # print(counter)
        results=model_obj.predict(frame)
        for r in results:
            for c in r.boxes.cls:
                if names[int(c)] == response_text:
                    ts.append(video_timestamp.get_timestamp(counter))  # Use the instance to get the timestamp
                

    video_timestamp.release()
    
    ts_updated=ts
    ts_updated=np.array(ts_updated)
    ts_updated_filtered = ts_updated[abs(ts_updated - np.mean(ts_updated)) < 2 * np.std(ts_updated)]
    # print(min(ts_updated_filtered), max(ts_updated_filtered))
    
    

# Specify the input video file path
    

    # Specify the output video file path
    output_video_path = f"C:/Users/USER/Desktop/web-pro/public/{file_name}.{file_ext}"
    
    start_timestamp = 0
    end_timestamp = 0

    print(len(ts_updated_filtered))
    # Specify the start and end timestamps in seconds
    
    if len(ts_updated_filtered) !=0:
        start_timestamp = min(ts_updated_filtered)
        end_timestamp = max(ts_updated_filtered)
        ffmpeg_extract_subclip(file_path, start_timestamp, end_timestamp, targetname=output_video_path)
    

        
    # Crop the video from start_timestamp to end_timestamp
   
    
        
    print(response_text)
    return {"success":True,"url":url_ip,"file_path":file_path,"start":start_timestamp,"end":end_timestamp,"message":response_text}


# print("Server is running ")


if __name__ == "__main__":
    uvicorn.run("main:app",host="127.0.0.1",reload=True)
    



