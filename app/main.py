import uvicorn
from fastapi import FastAPI
from dotenv import load_dotenv
from endpoints.training import router_training
from endpoints.inference import router_inference
from database import models
from database.database import engine

load_dotenv()

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router_training)
app.include_router(router_inference)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)