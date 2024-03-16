from fastapi import FastAPI,File,UploadFile
from secrets import token_hex

import uvicorn
app = FastAPI(title="File Upload API")

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    file_ext=file.filename.split(".").pop()
    file_name=token_hex(10)
    file_path=f"{file_name}.{file_ext}"
    with open(file_path,"wb") as buffer:
        content=await file.read()
        buffer.write(content)
    return {"success":True,"file_path":file_path,"message":"File uploaded successfully"}

if __name__ == "__main__":
    uvicorn.run("main:app",host="127.0.0.1",reload=True)
    
