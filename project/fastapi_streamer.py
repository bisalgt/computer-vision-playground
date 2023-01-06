import uvicorn
import cv2

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, StreamingResponse
from fastapi.templating import Jinja2Templates

import camera


app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
   return templates.TemplateResponse('index.html', {"request": request})


def video_stream():
    """Video streaming generator function."""
    video_camera = camera.VideoCamera()
    while True:
        frame = video_camera.get_frame()
        if frame != None:
            yield (b'--frame\r\n'
                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.get('/video_stream', response_class=HTMLResponse)
async def video_response():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return  StreamingResponse(video_stream(),
                    media_type='multipart/x-mixed-replace; boundary=frame')


if __name__ == "__main__":
    print('stop: ctrl+c')
    uvicorn.run(app, host="0.0.0.0", port=8000)