# Naam: Mehmet Alpertas
# Studentnummer: 545676
# Opmerking: Voor dit bestand is AI (ChatGPT) gebruikt als hulpbron

FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
