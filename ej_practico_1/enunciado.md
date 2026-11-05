**Ejercicio 1 — Comparar inferSchema vs schema explícito (medición y observación)**

Lee sales_simple.csv de dos formas:

(A) usando inferSchema=True y (B) usando un schema explícito (StructType). Mide el tiempo de lectura en cada caso y observa printSchema() y count(). Piensa cuál usarías en desarrollo y cuál en producción.

Objetivo
Entender la diferencia práctica entre inferSchema (conveniente pero hace una pasada extra) y schema explícito (reproducible y más eficiente en ETLs grandes).

**Ejercicio 2 — Añadir weekday y agrupar: ventas totales por día de la semana**

Crea la columna total = price * quantity. Añade una columna weekday (día de la semana) a partir de date y agrupa para obtener la suma de total por weekday. Ordena el resultado por el total descendente.

Objetivo
Practicar withColumn, to_date/date_format y groupBy + agregaciones.



**Ejercicio 3 — Manejar registros corruptos / malformados**

Imagina que alguien añadió una fila mal formada a sales_simple.csv (por ejemplo, 11,2024-01-20,Portátil,not_a_number,2 donde price NO es convertible a double). Crea un CSV sales_malformed.csv con esa fila extra. Lee el CSV de dos maneras:

A) usando option("mode", "DROPMALFORMED") y un schema explícito — comprueba el count final.

B) usando option("mode", "PERMISSIVE") y option("columnNameOfCorruptRecord", "_corrupt_record") con mismo schema — comprueba cómo Spark conserva el registro corrupto en una columna.

Piensa la diferencia y cuándo usar cada modo.

Objetivo
Saber manejar líneas malformadas sin romper el pipeline.

