FROM python:3.12-alpine

WORKDIR /code


RUN apk update && apk add --no-cache \
    bash \
    netcat-openbsd \
    build-base \
    libffi-dev \
    musl-dev \
    gcc \
    cargo \
    && rm -rf /var/cache/apk/*


COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir -r requirements.txt


COPY . .


COPY wait-for-it.sh /wait-for-it.sh
RUN chmod +x /wait-for-it.sh


CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
