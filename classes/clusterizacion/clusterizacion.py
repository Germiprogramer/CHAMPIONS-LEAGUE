import sys
sys.path.append(r'C:/Users/Germán Llorente/Desktop/germiprogramer/CHAMPIONS-LEAGUE')
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans, AgglomerativeClustering, DBSCAN, MeanShift, estimate_bandwidth
from sklearn.mixture import GaussianMixture
from sklearn.metrics import silhouette_score
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from auxiliar.rutas import *
from sklearn.impute import SimpleImputer

class Clusterizacion:
    def __init__(self, data, features):
        """
        Inicializar la clase con el dataframe y las características (features) a utilizar.
        """
        self.data = data
        self.features = features
        self.X_scaled = None

    def normalizar_datos(self):
        """
        Imputar valores faltantes y normalizar los datos.
        """
        imputer = SimpleImputer(strategy='mean')
        X_imputed = imputer.fit_transform(self.data[self.features])

        scaler = StandardScaler()
        self.X_scaled = scaler.fit_transform(X_imputed)

    def metodo_del_codo(self, max_clusters=10):
        """
        Aplicar el método del codo para determinar el número óptimo de clusters para K-Means.
        """
        inertia = []
        for k in range(1, max_clusters + 1):
            kmeans = KMeans(n_clusters=k, random_state=42)
            kmeans.fit(self.X_scaled)
            inertia.append(kmeans.inertia_)
        
        plt.figure(figsize=(10, 6))
        plt.plot(range(1, max_clusters + 1), inertia, marker='o', linestyle='--')
        plt.title('Método del Codo')
        plt.xlabel('Número de Clusters')
        plt.ylabel('Inercia')
        plt.xticks(range(1, max_clusters + 1))
        plt.grid(True)
        plt.show()

    def aplicar_kmeans(self, n_clusters):
        """
        Aplicar K-Means al dataset con un número específico de clusters.
        """
        kmeans = KMeans(n_clusters=n_clusters, random_state=42)
        kmeans.fit(self.X_scaled)
        self.data['Cluster_KMeans'] = kmeans.labels_

    def aplicar_agglomerative(self, n_clusters):
        """
        Aplicar clustering aglomerativo al dataset.
        """
        agglomerative = AgglomerativeClustering(n_clusters=n_clusters)
        self.data['Cluster_Agglomerative'] = agglomerative.fit_predict(self.X_scaled)

    def aplicar_dbscan(self, eps=0.5, min_samples=5):
        """
        Aplicar DBSCAN al dataset.
        """
        dbscan = DBSCAN(eps=eps, min_samples=min_samples)
        self.data['Cluster_DBSCAN'] = dbscan.fit_predict(self.X_scaled)

    def aplicar_gmm(self, n_components):
        """
        Aplicar Gaussian Mixture Models al dataset.
        """
        gmm = GaussianMixture(n_components=n_components, random_state=42)
        gmm.fit(self.X_scaled)
        self.data['Cluster_GMM'] = gmm.predict(self.X_scaled)

    def evaluar_clusters(self, cluster_column):
        """
        Evaluar los clusters utilizando el coeficiente de silueta.
        """
        score = silhouette_score(self.X_scaled, self.data[cluster_column])
        print(f"Coeficiente de silueta para {cluster_column}: {score}")

data = ch24



features = ['W_av', 'D_av', 'L_av', 'GF_av', 'GA_av', 'GD_av', 'Pts_av', 'xG_av', 'xGA_av', 'xGD_av']
clasterizador = Clusterizacion(data, features)
clasterizador.normalizar_datos()
clasterizador.metodo_del_codo(max_clusters=10)

# Aplicar K-Means con 4 clusters
clasterizador.aplicar_kmeans(n_clusters=4)

# Aplicar Agglomerative Clustering con 4 clusters
clasterizador.aplicar_agglomerative(n_clusters=4)

# Aplicar DBSCAN con los parámetros por defecto
clasterizador.aplicar_dbscan(eps=0.5, min_samples=5)

# Aplicar GMM con 4 componentes
clasterizador.aplicar_gmm(n_components=4)

# Evaluar los clusters generados por K-Means y Agglomerative Clustering utilizando el coeficiente de silueta
clasterizador.evaluar_clusters('Cluster_KMeans')
clasterizador.evaluar_clusters('Cluster_Agglomerative')

# Ver las primeras filas del dataframe para observar las asignaciones de cluster
print(data[['Squad', 'Cluster_KMeans', 'Cluster_Agglomerative', 'Cluster_DBSCAN', 'Cluster_GMM']])

from sklearn.decomposition import PCA
import seaborn as sns

# Reducir los datos a 2 dimensiones usando PCA
pca = PCA(n_components=2)
X_pca = pca.fit_transform(clasterizador.X_scaled)

# Convertir los resultados a un DataFrame para facilitar el plotting
pca_df = pd.DataFrame(data=X_pca, columns=['PC1', 'PC2'])
pca_df['Cluster'] = data['Cluster_KMeans']  # Usar las etiquetas de clúster de K-Means

# Graficar los resultados
plt.figure(figsize=(14, 10))

# Graficar los puntos
sns.scatterplot(x='PC1', y='PC2', hue='Cluster', data=pca_df, palette='viridis', s=100, alpha=0.7, legend='full')

# Añadir los nombres de los equipos al gráfico
for i, txt in enumerate(data.Squad):
    plt.annotate(txt, (X_pca[i, 0], X_pca[i, 1]), textcoords="offset points", xytext=(5,-5), ha='center', fontsize=8)

plt.title('Visualización de Clusters con PCA y Nombres de Equipos')
plt.xlabel('Componente Principal 1')
plt.ylabel('Componente Principal 2')
plt.legend(title='Cluster')
plt.show()
