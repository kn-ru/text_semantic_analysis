# Text Semantic Analysis
Проект представляет собой веб сервер, реализующий функцию предсказания эмоционально окраски новости на русском языке.
Обуччающий датасет был загружен с [соревнования](https://www.kaggle.com/competitions/sentiment-analysis-in-russian/overview)

# Зависимости
- устанавливаем python3, pip3, python3-venv
- клонируем проект
```
git clone https://github.com/kn-ru/text_semantic_analysis.git
```
- создаем виртуальное окуружение
```
cd text_semantic_analysis
python3 -m venv semanticenv
source semanticenv/bin/activate
pip3 install --upgrade pip
pip3 install --upgrade setuptools
```
- устанавливаем пакеты
```
pip3 install -r requirements.txt
```
Устанавливаем FastAPI
```
pip3 install FastAPI[all]
```
# Запуск сервера

Сервер запускаем командой
```
uvicorn main:app
```