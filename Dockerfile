FROM python:3.7

RUN pip install fastapi uvicorn aiofiles fastapi-async-sqlalchemy python-multipart pymysql

EXPOSE 8000

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]