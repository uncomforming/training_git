FROM python:3.9-slim
#作る場所
WORKDIR /app
#ライブラリの一覧
COPY liblary.txt .
RUN pip install --no-cache-dir --upgrade -r /app/liblary.txt
#copy元
COPY ./main/ .

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8080"]