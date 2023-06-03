FROM python:3.9-slim

WORKDIR /app

COPY liblary.txt .
RUN pip install --no-cache-dir --upgrade -r /app/liblary.txt

COPY ./main/ .

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8080"]