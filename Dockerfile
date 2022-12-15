FROM nvidia/cuda:11.3.1-devel-ubuntu20.04 as base

ENV APP_HOME /app

ENV NVIDIA_DRIVER_CAPABILITIES compute,utility
ENV DEBIAN_FRONTEND=noninteractive
ENV NVIDIA_VISIBLE_DEVICES all
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

# Available development environments:
# - gcp (Cloud Run/App Engine)
# - dev (Local Development/VM)
# - prod (Production)
ENV ENVIRONMENT dev
ENV PORT 7071

RUN apt-get update \
    && apt-get -y install netcat gcc libpq-dev git wget python3.9 python3-pip \
    && apt-get clean

WORKDIR $APP_HOME

COPY requirements.txt .
COPY setup.py .

RUN pip3 install git+https://github.com/KnowCorp/rigel
RUN pip3 install git+https://github.com/boudinfl/pke.git@69337af9f9e72a25af6d7991eaa9869f1322dd72

RUN python3 -m nltk.downloader universal_tagset
RUN python3 -m spacy download en

RUN wget https://github.com/explosion/sense2vec/releases/download/v1.0.0/s2v_reddit_2015_md.tar.gz
RUN tar -xvf  s2v_reddit_2015_md.tar.gz

COPY . .

ENTRYPOINT [ "uvicorn", "main:app", "--reload", "--workers=4", "--host=0.0.0.0", "--port=7071" ]
