from fastapi import FastAPI
from fastapi import staticfiles

app = FastAPI()
app.mount("static",staticfiles(directory="static"),name="static")

