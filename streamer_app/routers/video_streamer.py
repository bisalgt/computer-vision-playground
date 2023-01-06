
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, StreamingResponse

from ..settings import templates
from ..camera_module import camera





router = APIRouter(

)


@router.get("/", response_class=HTMLResponse)
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


@router.get('/video_stream', response_class=HTMLResponse)
async def video_response():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return  StreamingResponse(video_stream(),
                    media_type='multipart/x-mixed-replace; boundary=frame')
