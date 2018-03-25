## Dockerfile:
FROM python:3
RUN mkdir /code
WORKDIR /code
# Copy requirment first and install it rather than run it directly from code to cache pip
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/
