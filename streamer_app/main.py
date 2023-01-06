from fastapi import FastAPI

from .routers import video_streamer


app = FastAPI()

# including routers or views
app.include_router(video_streamer.router)


if __name__ == "__main__":
    import uvicorn
    from .settings import host_info
    uvicorn.run(app, host=host_info, port=8000)