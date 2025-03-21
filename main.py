from fastapi import FastAPI
from routers.router import router
from fastapi.staticfiles import StaticFiles 
app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/images", StaticFiles(directory="static/images"), name="images")
app.mount("/js", StaticFiles(directory="static/js"), name="js")
app.include_router(router)