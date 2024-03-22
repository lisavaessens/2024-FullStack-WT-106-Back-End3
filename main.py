from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import config
#from routes import lg, lv, rv, wv

app = FastAPI()



origins = config.cors_origins.split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/test")
def main():
    return {"message": "Hello World"}

