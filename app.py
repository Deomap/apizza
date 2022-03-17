from fastapi import FastAPI, Depends
import uvicorn
from api.routes import api
from db import tables
from db.database import engine

application = FastAPI()


def configure_db(drop):
    if drop:
        tables.Base.metadata.drop_all(bind=engine)
    tables.Base.metadata.create_all(bind=engine)


def configure_app():
    application.include_router(api.router)


if __name__ == '__main__':
    configure_db(drop=False)
    configure_app()
    uvicorn.run(
        application,
        port=8000,
        host='127.0.0.1',
    )
else:
    configure_app()