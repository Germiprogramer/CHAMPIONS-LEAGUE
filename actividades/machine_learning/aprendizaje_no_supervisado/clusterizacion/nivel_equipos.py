import sys
sys.path.append(r'C:/Users/Germán Llorente/Desktop/germiprogramer/CHAMPIONS-LEAGUE')
from classes.clusterizacion.clusterizacion import *
from auxiliar.rutas import *

features = ['W_av', 'D_av', 'L_av', 'GF_av', 'GA_av', 'GD_av', 'Pts_av', 'xG_av', 'xGA_av', 'xGD_av']
clasterizador = Clusterizacion(ch24, features)
clasterizador.normalizar_datos()
clasterizador.metodo_del_codo(max_clusters=10)

# Aplicar K-Means con 4 clusters
clasterizador.aplicar_kmeans(n_clusters=3)

# Aplicar Agglomerative Clustering con 4 clusters
clasterizador.aplicar_agglomerative(n_clusters=4)

# Aplicar DBSCAN con los parámetros por defecto
clasterizador.aplicar_dbscan(eps=0.5, min_samples=5)

# Aplicar GMM con 4 componentes
clasterizador.aplicar_gmm(n_components=5)

# Evaluar los clusters generados por K-Means y Agglomerative Clustering utilizando el coeficiente de silueta
clasterizador.evaluar_clusters('Cluster_KMeans')
clasterizador.evaluar_clusters('Cluster_Agglomerative')
clasterizador.evaluar_clusters('Cluster_GMM')


# Mostrar los clusters generados por cada algoritmo

clasterizador.graficar_clusters('Cluster_GMM')
