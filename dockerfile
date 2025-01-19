FROM python:3.12.7-alpine3.20
ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY requirements.txt .

RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt

COPY . . 

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]