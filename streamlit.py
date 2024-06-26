# -*- coding: utf-8 -*-
"""untitled7.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/gist/Kvoki/4dabad9cad7c04f0e032e5b910ea6b9d/untitled7.ipynb
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

# Загрузка данных
def load_data():
    # Используйте полный путь к вашему файлу
    data = pd.read_csv("/content/areaburntbywildfiresbyweek_new.csv")
    return data

# Функция для отображения описания полей данных
def show_data_description(data):
    st.subheader("Описание полей данных:")
    st.write("Этот раздел содержит описание каждого поля в исходных данных.")
    st.write("Пожалуйста, ознакомьтесь с ним перед анализом данных.")

    # Описание полей
    data_description = {
        "Entity": "Страна",
        "Code": "Код страны",
        "Year": "Год",
        "area burnt by wildfires in 2024": "Площадь, сгоревшая от лесных пожаров в 2024 году",
        "burnt by wildfires in 2023": "Площадь, сгоревшая от лесных пожаров в 2023 году",
        "burnt by wildfires in 2022": "Площадь, сгоревшая от лесных пожаров в 2022 году",
        "burnt by wildfires in 2021": "Площадь, сгоревшая от лесных пожаров в 2021 году",
        "burnt by wildfires in 2020": "Площадь, сгоревшая от лесных пожаров в 2020 году",
        "area burnt by wildfires in 2019": "Площадь, сгоревшая от лесных пожаров в 2019 году",
        "a burnt by wildfires in 2018": "Площадь, сгоревшая от лесных пожаров в 2018 году"
    }

    # Вывод описания полей
    for column, description in data_description.items():
        st.write(f"**{column}**: {description}")

# Функция для анализа и предобработки данных
def data_analysis(data):
    st.subheader("Анализ и предобработка данных:")
    st.write("Этот раздел содержит анализ и предобработку данных перед их использованием в анализе и визуализации.")

    # Поиск нулевых значений
    st.write("### Нулевые значения:")
    st.write(data.isnull().sum())

    # Количество уникальных значений для любого столбца
    st.write("### Количество уникальных значений для каждого столбца:")
    st.write(data.nunique())

    # Описательная статистика данных
    st.write("### Описательная статистика данных:")
    st.write(data.describe())

    # Количество всех категорий в виде графиков
    st.write("### Количество всех категорий в виде графиков:")
    categorical_columns = data.select_dtypes(include=['object']).columns.tolist()
    for column in categorical_columns:
        plt.figure(figsize=(10, 6))
        sns.countplot(x=column, data=data)
        plt.title(f"Распределение значений по категориям в столбце '{column}'")
        plt.xticks(rotation=45)
        plt.xlabel(column)
        plt.ylabel("Количество")
        st.pyplot(plt)

# Функция для визуализации распределения выбранных категорий и выделения выбросов
def data_visualization(data):
    st.subheader("Визуализация:")
    st.write("Этот раздел содержит визуализацию данных для анализа распределения и выявления выбросов.")

    # Выбор категорий для визуализации
    selected_columns = st.multiselect("Выберите столбцы для визуализации:", data.columns)

    if selected_columns:
        for column in selected_columns:
            # Визуализация распределения выбранной категории
            plt.figure(figsize=(10, 6))
            sns.histplot(data[column], bins=20, kde=True)
            plt.title(f"Распределение значений в столбце '{column}'")
            plt.xlabel(column)
            plt.ylabel("Количество")
            st.pyplot(plt)

            # Выделение выбросов
            plt.figure(figsize=(10, 6))
            sns.boxplot(x=data[column])
            plt.title(f"Выделение выбросов в столбце '{column}'")
            plt.xlabel(column)
            st.pyplot(plt)

# Функция для обучения и оценки классификационной модели
def train_and_evaluate_model(data):
    st.subheader("Обучение и оценка результатов прогнозирования:")
    st.write("Этот раздел содержит обучение классификационной модели и оценку ее результатов.")

    # Разделение данных на признаки (X) и целевую переменную (y)
    X = data.drop(["Code", "Year", "Entity"], axis=1)  # Исключаем ненужные столбцы
    y = data["Code"]

    # Разделение данных на обучающий и тестовый наборы
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Обучение модели
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)

    # Предсказание на тестовом наборе
    y_pred = model.predict(X_test)

    # Оценка результатов
    st.write("### Матрица путаницы:")
    st.write(confusion_matrix(y_test, y_pred))

    st.write("### Отчет о классификации:")
    st.write(classification_report(y_test, y_pred))

    st.write("### Оценка точности:")
    st.write(f"Точность модели: {accuracy_score(y_test, y_pred)}")

# Заголовок
st.title("Анализ данных")

# Загрузка данных
data = load_data()

# Вывод данных
st.write("Демонстрация данных:")
st.write(data)

# Описание полей данных
show_data_description(data)

# Анализ и предобработка данных
data_analysis(data)

# Визуализация
data_visualization(data)

# Обучение и оценка результатов прогнозирования
train_and_evaluate_model(data)