FROM python:3.9.16-slim-buster

WORKDIR /app

COPY required_versions.txt .

RUN pip3 install --no-cache-dir -r required_versions.txt

COPY . .

ENV FLASK_APP="myapp.py"

EXPOSE 5000

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]