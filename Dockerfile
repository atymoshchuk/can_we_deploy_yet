FROM python:3.12-slim AS compile-image

WORKDIR /app

# hadolint ignore=DL3008
RUN apt-get update && \
    apt-get install -y --no-install-recommends build-essential gcc && \
    python -m venv /opt/venv

# Make sure we use the virtualenv:
ENV PATH="/opt/venv/bin:$PATH"

COPY ./requirements/awesome_app.txt .
RUN pip install --no-cache-dir -r awesome_app.txt

FROM python:3.12-slim AS build-image
COPY --from=compile-image /opt/venv /opt/venv

WORKDIR /app

# Make sure we use the virtualenv:
ENV PATH="/opt/venv/bin:$PATH"

COPY ./awesome_app /app

CMD ["fastapi", "run", "main.py"]
