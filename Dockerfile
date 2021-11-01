# docker image build -t translate-images .
FROM python:3.7
WORKDIR /
RUN apt-get update \
    && apt-get install -y \
        build-essential \
        cmake \
        git \
        wget \
        unzip \
        yasm \
        pkg-config \
        libswscale-dev \
        libtbb2 \
        libtbb-dev \
        libjpeg-dev \
        libpng-dev \
        libtiff-dev \
        libavformat-dev \
        libpq-dev \
    && rm -rf /var/lib/apt/lists/*

RUN apt-get --fix-missing update \
    && apt-get --fix-broken install \
    && apt-get install -y poppler-utils \
    && apt-get install -y tesseract-ocr tesseract-ocr-all \
    && apt-get install -y libtesseract-dev \
    && apt-get install -y libleptonica-dev \
    && ldconfig && apt install -y libsm6 libxext6


COPY ./requirements.txt ./ 
COPY ./converter.py ./
COPY ./in/ ./in/
RUN pip3 install opencv-python
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
