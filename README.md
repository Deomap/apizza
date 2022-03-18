# apizza

Apizza is a simple API for a medium-sized pizzeria chain. This API provides an interface for user interaction with the database and other pizzeria systems. Apizza gives you the ability to authenticate and set permissions for different user groups. The service can also be deployed in Docker. The API is made on Python 3.10 using FastAPI, SQLAlchemy (database) and Pydantic models.

### Starting app

You can start API using Docker. Write in console (in project root):
```html
docker build -t image .
```
Docker will auto install required paackages. With already existing image you can run:
```html
docker run -d --name apizza -p 80:80 image
```
If you want to run application in IDE or something else you can install all the needed with command:
```html
pip install --no-cache-dir --upgrade -r requirements
```
