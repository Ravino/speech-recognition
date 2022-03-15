FROM python:3.8

COPY . .
RUN bash ./install.sh


ENTRYPOINT ["python3"]
CMD ["main.py"]
