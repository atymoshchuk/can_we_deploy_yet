FROM tiangolo/uvicorn-gunicorn:python3.7

RUN pip install --no-cache-dir fastapi

COPY ./awesome_app /app

WORKDIR /app/

ENV PYTHONPATH=/app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]