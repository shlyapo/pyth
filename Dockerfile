FROM python:3.8
 ## гарантирует, что наш вывод консоли выглядит знакомым и не буферизируется Docker, что нам не нужно
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE=1
RUN mkdir /web_django
WORKDIR /web_django
COPY requirements.txt /web_django/
RUN pip install --upgrade pip && pip install -r requirements.txt
COPY . /web_django/
ADD . /lab_34/
CMD python3 manage.py runserver 0.0.0.0:$PORT
## delete last