import pandas as pd

ruta_2014 = r"C:\Users\Germán Llorente\Desktop\germiprogramer\CHAMPIONS-LEAGUE\datos\datos_limpios\champions2014_limp.csv"
ruta_2015 = r"C:\Users\Germán Llorente\Desktop\germiprogramer\CHAMPIONS-LEAGUE\datos\datos_limpios\champions2015_limp.csv"
ruta_2016 = r"C:\Users\Germán Llorente\Desktop\germiprogramer\CHAMPIONS-LEAGUE\datos\datos_limpios\champions2016_limp.csv"
ruta_2017 = r"C:\Users\Germán Llorente\Desktop\germiprogramer\CHAMPIONS-LEAGUE\datos\datos_limpios\champions2017_limp.csv"
ruta_2018 = r"C:\Users\Germán Llorente\Desktop\germiprogramer\CHAMPIONS-LEAGUE\datos\datos_limpios\champions2018_limp.csv"
ruta_2019 = r"C:\Users\Germán Llorente\Desktop\germiprogramer\CHAMPIONS-LEAGUE\datos\datos_limpios\champions2019_limp.csv"
ruta_2020 = r"C:\Users\Germán Llorente\Desktop\germiprogramer\CHAMPIONS-LEAGUE\datos\datos_limpios\champions2020_limp.csv"
ruta_2021 = r"C:\Users\Germán Llorente\Desktop\germiprogramer\CHAMPIONS-LEAGUE\datos\datos_limpios\champions2021_limp.csv"
ruta_2022 = r"C:\Users\Germán Llorente\Desktop\germiprogramer\CHAMPIONS-LEAGUE\datos\datos_limpios\champions2022_limp.csv"
ruta_2023 = r"C:\Users\Germán Llorente\Desktop\germiprogramer\CHAMPIONS-LEAGUE\datos\datos_limpios\champions2023_limp.csv"
ruta_2024 = r"C:\Users\Germán Llorente\Desktop\germiprogramer\CHAMPIONS-LEAGUE\datos\datos_limpios\champions2024_limp.csv"
ruta_ranking_fifa = r"C:\Users\Germán Llorente\Desktop\germiprogramer\CHAMPIONS-LEAGUE\datos\datos_limpios\ranking_UEFA_limp.csv"
ruta_real_madrid_liga = r"C:\Users\Germán Llorente\Desktop\germiprogramer\CHAMPIONS-LEAGUE\datos\equipos_seleccionados\real_madrid\real_madrid_liga.csv"
ruta_manchester_city_liga = r"C:\Users\Germán Llorente\Desktop\germiprogramer\CHAMPIONS-LEAGUE\datos\equipos_seleccionados\manchester_city\manchester_city_liga.csv"

ch14 = pd.read_csv(ruta_2014)
ch15 = pd.read_csv(ruta_2015)
ch16 = pd.read_csv(ruta_2016)
ch17 = pd.read_csv(ruta_2017)
ch18 = pd.read_csv(ruta_2018)
ch19 = pd.read_csv(ruta_2019)
ch20 = pd.read_csv(ruta_2020)
ch21 = pd.read_csv(ruta_2021)
ch22 = pd.read_csv(ruta_2022)
ch23 = pd.read_csv(ruta_2023)
ch24 = pd.read_csv(ruta_2024)
ranking_fifa = pd.read_csv(ruta_ranking_fifa)

real_madrid_liga = pd.read_csv(ruta_real_madrid_liga)
manchester_city_liga = pd.read_csv(ruta_manchester_city_liga)