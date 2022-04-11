FROM python:3.9

WORKDIR /app

COPY ./requirements.txt /requirements.txt

RUN pip install --no-cache-dir --upgrade -r /requirements.txt
RUN pip install requests

COPY ./app /app

CMD ["uvicorn", "main:app", "--host=0.0.0.0" , "--reload" , "--port", "80"]
