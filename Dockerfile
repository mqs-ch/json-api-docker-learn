# Используем официальный образ Python 3.10 (slim-версия для экономии места)
FROM python:3.10-slim

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файл с зависимостями
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем сам скрипт
COPY stats.py .

# Запускаем скрипт при старте контейнера
CMD ["python", "stats.py"]
