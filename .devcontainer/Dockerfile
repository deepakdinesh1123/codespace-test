FROM python:3.10-bullseye
RUN pip install fastapi uvicorn psycopg2-binary sqlalchemy
COPY main.py /var/lib/docker/codespacemount/workspace/codespace-test/
# CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000" ]