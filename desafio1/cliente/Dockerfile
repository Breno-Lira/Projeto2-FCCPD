FROM python:3.11-slim

WORKDIR /app

RUN pip install requests

COPY cliente.py /app/cliente.py

CMD ["python", "cliente.py"]
