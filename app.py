from fastapi import FastAPI
import uvicorn
from api import routes
from db import crud, models
from db.database import engine

api = FastAPI()


def configure_db():
    models.Base.metadata.create_all(bind=engine)


def configure_app():
    api.include_router(routes.router)


if __name__ == '__main__':
    configure_db()
    configure_app()
    uvicorn.run(api,
                port=8000,
                host='127.0.0.1')
else:
    configure_app()
