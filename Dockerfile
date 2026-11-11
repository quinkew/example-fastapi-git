FROM python:3.14.7

RUN apt-get update && apt-get install -y --no-install-recommends gcc python3-dev && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/server

COPY requirements.txt ./

RUN pip install --prefer-binary -r requirements.txt

COPY . .

CMD ["uvicorn", "server.main:app", "--host", "0.0.0.0", "--port", "8000"]