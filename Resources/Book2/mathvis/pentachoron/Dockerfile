FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && \
    apt-get install -y --no-install-recommends ffmpeg && \
    rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir numpy matplotlib

COPY pentachoron_anim.py /app/pentachoron_anim.py

ENTRYPOINT ["python", "pentachoron_anim.py"]
