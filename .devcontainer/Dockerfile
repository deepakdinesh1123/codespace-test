FROM python:3.10-bullseye

COPY main.py .
COPY requirements.txt .
RUN pip install -r requirements.txt
CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000" ]