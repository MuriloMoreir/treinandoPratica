FROM python:3.10

WORKDIR /app
COPY . .

EXPOSE 5000

CMD ["python", "app_teste.py"]
