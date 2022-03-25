FROM python:3.10
ENV PYTHONUNBUFFERED 1
# RUN apt-get update
# RUN curl -fsSL https://deb.nodesource.com/setup_16.x | bash -
# RUN apt-get install -y nodejs
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -i https://pypi.douban.com/simple -r requirements.txt
COPY . /code/
