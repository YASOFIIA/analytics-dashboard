from fastapi import FastAPI, Request
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates
from routers import charts, graphs
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.include_router(charts.router)
app.include_router(graphs.router)

app.mount("/static", StaticFiles(directory="static"), name="static")
templates= Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", context={"request": request})