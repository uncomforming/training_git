from fastapi import FastAPI,Request
from fastapi import staticfiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import route

app = FastAPI()
app.mount("static",staticfiles(directory="static"),name="static")
app.include_router(route.router)

templates=Jinja2Templates(directory="templates")


@app.get("/")
async def index(name: str, request: Request):
    return templates.TemplateResponse("template.html", {
        "name": name,
        "request": request
    })
