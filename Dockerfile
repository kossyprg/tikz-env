FROM debian:bullseye

RUN apt-get update && apt-get install -y \
    texlive \
    texlive-lang-japanese \
    texlive-pictures \
    texlive-science \
    latexmk \
    poppler-utils \
    make \
    && apt-get clean

WORKDIR /work
