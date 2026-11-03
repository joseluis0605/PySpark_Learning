# importamos libreria
from pyspark.sql import SparkSession

# definimos sesion spark
spark = (SparkSession.builder
                 .appName("Nombre_aplicacion") # definimos nombre aplicacion
                 .master("local[*]") # indicamos ejecución local usando todos los nucleos de los procesadores
                 .config("spark.driver.memory", "2g") # definimos memoria del driver
                 .getOrCreate()
)

print(f"version spark: {spark.version}")

# creamos dataset
lista_valores = [("españa", "madrid"), ("francia", "paris"), ("alemania", "berlin")]
lista_columnas = ["pais", "capital"]

# creamos dataframe
df = spark.createDataFrame(lista_valores, lista_columnas)
df.show()
