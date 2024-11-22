FROM python:3.12

COPY ./awesome_app /app
COPY ./requirements/awesome_app.txt /app

WORKDIR /app/

ENV PYTHONPATH=/app

RUN pip install --no-cache-dir -r awesome_app.txt

CMD ["fastapi", "run", "main.py"]
