from fastapi import APIRouter,Request
from fastapi.responses import HTMLResponse  
from fastapi.templating import Jinja2Templates 
from fastapi.staticfiles import StaticFiles
router = APIRouter()

templates = Jinja2Templates(directory="templates")

@router.get("/class.html", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("class.html", {"request": request})

@router.get("/index.html", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@router.get("/blog.html", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("blog.html", {"request": request})

@router.get("/about.html", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})
    

    

