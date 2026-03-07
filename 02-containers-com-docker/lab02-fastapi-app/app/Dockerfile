FROM python:3.11-slim

WORKDIR /app

# boa prática: instalar deps primeiro (melhora cache do build)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# agora copia o código
COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
