FROM python:3.10-bullseye
RUN fastapi uvicorn psycopg2-binary sqlalchemy
CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000" ]