# Використовуємо офіційний образ Python версії 3.9
FROM python:3.12

COPY . /app
WORKDIR /app
RUN pip install psycopg2

# Виконуємо команду для запуску тестів під час створення контейнера
CMD ["python", "pq_checker.py"]