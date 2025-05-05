from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")
notes = {}  #

@app.get("/", response_class=HTMLResponse)
async def read_notes(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "notes": notes.keys()})

@app.post("/add")
async def add_note(request: Request, note: str = Form(...), name: str = Form(...)):
    notes[name] = note
    return await read_notes(request)


@app.get('/note/{note_name}')
async def read_note(reuest: Request, note_name: str):
    return templates.TemplateResponse('read.html', {'request': reuest, "note": notes[note_name]})
