FROM python:3.8.2-alpine
WORKDIR /app
COPY main.py .
ENTRYPOINT [ 'python3' ]
CMD [ 'main.py' ]
