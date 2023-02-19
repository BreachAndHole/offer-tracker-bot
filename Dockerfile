FROM python:3.11
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install --upgrade pip
RUN pip3 install -r /app/requirements.txt
COPY . .
CMD ["python3", "__main__.py"]