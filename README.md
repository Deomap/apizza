# apizza

Apizza is a simple API for a medium-sized pizzeria chain. This API provides an interface for user interaction with the database and other pizzeria systems. Apizza gives you the ability to authenticate and set permissions for different user groups. The service can also be deployed in Docker. The API is made on Python using FastAPI, SQLAlchemy (database) and Pydantic models.

### Starting app

You can start API using Docker. Write in console (in project root):
```html
docker build -t image .
```
Docker will auto install all the needed. With already existing image you can run:
```html
docker run -d --name apizza -p 80:80 image
```
Where ```image``` is built docker image.

To run API you need to install:
- Python language == 3.10
- redis == 4.1.4 (with redis-server)
- bcrypt == 3.2.0
- pydantic == 1.9.0
- python-jose == 3.3.0
- pytest == 7.1.1
- fastapi == 0.75.0
- fastapi-auth == 0.1.1
- SQLAlchemy == 1.4.32
- uvicorn == 0.17.5
- passlib == 1.7.4
- cryptography == 36.0.2
