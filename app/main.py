import os
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import uvicorn

BASE_DIR = 'app' # refers to folder app
#print(os.path.isdir(os.path.join(BASE_DIR, "templates")))
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))

app = FastAPI()

@app.get('/', response_class=HTMLResponse) # http GET
def home_view(request: Request):
    print(request)
    #return {'hello':'world'}
    return templates.TemplateResponse("home.html", {"request":request, "param":"Hello"})

@app.post('/') # http POST
def home_detail_view():
    return {'hello':'world'}
