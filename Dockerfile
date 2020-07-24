FROM tiangolo/uvicorn-gunicorn:python3.7

COPY ./awesome_app /app
COPY ./requirements/awesome_app.txt /app

WORKDIR /app/

ENV PYTHONPATH=/app

RUN pip install --no-cache-dir -r awesome_app.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
