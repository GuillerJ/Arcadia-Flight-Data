FROM python:3.9
ADD . /app
WORKDIR /app
EXPOSE 80
RUN pip3 install -r frontend/requirements.txt
RUN pip3 install -r backend/requirements.txt
RUN chmod a+x startup.sh
CMD ["/bin/bash", "startup.sh"]
