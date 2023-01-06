FROM python:3.9

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

COPY ./docker/entrypoint.sh /app/entrypoint.sh

RUN sed -i 's/\r$//g' /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

COPY ./project /app/project

RUN apt update && \
apt install -y libgl1-mesa-glx


ENTRYPOINT [ "/app/entrypoint.sh" ]