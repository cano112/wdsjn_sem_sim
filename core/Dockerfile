FROM python:3.6
ENV APP /app

WORKDIR $APP
ADD requirements.txt $APP/requirements.txt

EXPOSE 5000
RUN pip install -r requirements.txt

ADD . $APP
CMD python app.py