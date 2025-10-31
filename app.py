from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

app = FastAPI()

@app.get("/", response_class=PlainTextResponse)
def read_root():
    return "Email: 23f2004078@ds.study.iitm.ac.in\nHello from Codespaces!"