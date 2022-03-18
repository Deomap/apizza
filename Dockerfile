#
FROM python:3.10

#
WORKDIR /dock

#
COPY ./requirements /dock/requirements

#
RUN pip install --no-cache-dir --upgrade -r /dock/requirements

#
COPY . /dock

#
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]