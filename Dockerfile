FROM python:3.10

RUN apt-get update && apt-get install -y tesseract-ocr tesseract-ocr-spa

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT ["streamlit", "run", "app.py"]