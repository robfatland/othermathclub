FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && \
    apt-get install -y --no-install-recommends ffmpeg && \
    rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir numpy matplotlib

COPY hexadecachoron_anim.py /app/hexadecachoron_anim.py

ENTRYPOINT ["python", "hexadecachoron_anim.py"]
