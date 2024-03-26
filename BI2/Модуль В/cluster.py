# Кластеризация данных
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# Загрузка данных
data = pd.read_excel('itogdata.xlsx')

# Преобразование текстовых описаний навыков в числовой формат
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(data['Навыки'])

# Выбор количества кластеров с помощью метода локтя
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
    kmeans.fit(tfidf_matrix)
    wcss.append(kmeans.inertia_)

# Обучение модели кластеризации
num_clusters = 3  # Выбираем количество кластеров
kmeans = KMeans(n_clusters=num_clusters, init='k-means++', random_state=42)
kmeans.fit(tfidf_matrix)

# Добавление меток кластеров к исходным данным
data['cluster'] = kmeans.labels_

# Оценка качества кластеризации с помощью силуэта
silhouette_avg = silhouette_score(tfidf_matrix, kmeans.labels_)
print(f"Средний показатель силуэта: {silhouette_avg}")

# Вывод результатов кластеризации
print(data[['Навыки', 'cluster']])