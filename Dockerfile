FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    texlive \
    texlive-lang-japanese \
    texlive-pictures \
    texlive-science \
    latexmk \
    poppler-utils \
    make \
    && apt-get clean

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /work
