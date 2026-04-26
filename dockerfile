FROM python:3.11

WORKDIR /app

RUN apt-get update && apt-get install -y \
    make \
    gcc-riscv64-linux-gnu \
    && rm -rf /var/lib/apt/lists/*
    
COPY requirements.txt . 

RUN pip install -r requirements.txt

COPY . .


