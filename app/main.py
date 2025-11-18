import uvicorn
from fastapi import FastAPI

from dotenv import load_dotenv

from endpoints import training, inference, monitoring
from database import models
from database.database import engine

load_dotenv()

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(training.router)
app.include_router(inference.router)
app.include_router(monitoring.router)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)