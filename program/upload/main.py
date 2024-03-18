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

class url_ip1(BaseModel):
    url1:str

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...) ):
    file_ext=file.filename.split(".").pop()
    file_name=file.filename.split(".")[0]
    file_path=f"{cur_direrctory}/{file_name}.{file_ext}" 
    # file_path=f"{file_name}.{file_ext}"
    with open(file_path,"wb") as buffer:
        content=await file.read()
        buffer.write(content)
    
    frame_extractor = VideoFrameExtractor(file_path)

    frames = frame_extractor.get_frames()
    counter = 0
    names=model_obj.names
    ts=[]
    video_timestamp = VideoTimestamp(video_path)
    for frame in frames:
        counter += 1
        # print(counter)
        results=model_obj.predict(frame)
        for r in results:
            for c in r.boxes.cls:
                if names[int(c)] == 'car':
                    ts.append(video_timestamp.get_timestamp(counter))  # Use the instance to get the timestamp
                

    video_timestamp.release()
    
    ts_updated=ts
    ts_updated=np.array(ts_updated)
    ts_updated_filtered = ts_updated[abs(ts_updated - np.mean(ts_updated)) < 2 * np.std(ts_updated)]
    
    
    return {"success":True,"file_path":file_path,"message":"File uploaded successfully"}



# @app.post("/prompt"):
# async def prompt():
#     return {"success":True,"message":"Server is running"}


@app.post('/analyze')
def phish_url(request:url_ip1):
    url_ip = request.url1
    print(url_ip)
    return {"success":True,"url":url_ip}



if __name__ == "__main__":
    uvicorn.run("main:app",host="127.0.0.1",reload=True)
    



