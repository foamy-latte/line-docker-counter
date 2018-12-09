FROM python:alpine3.6
COPY . /app
WORKDIR /app
RUN pip install -r test_requirements.txt
EXPOSE 80
CMD pytest; coverage run test_main.py test