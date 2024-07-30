from datetime import datetime, date
from pyspark.sql import SparkSession, Row
from pyspark.sql.types import StructType, StructField, IntegerType, DoubleType, StringType, DateType, TimestampType

# Inicialização da sessão do Spark
spark = SparkSession.builder \
    .appName('app-pyspark') \
    .master('spark://spark-master:7077') \
    .getOrCreate()


# Definição do esquema do DataFrame
schema = StructType([
    StructField("a", IntegerType(), True),
    StructField("b", DoubleType(), True),
    StructField("c", StringType(), True),
    StructField("d", DateType(), True),
    StructField("e", TimestampType(), True)
])

# Criação do DataFrame com o esquema definido
df = spark.createDataFrame([
    Row(a=1, b=2.0, c='string1', d=date(2000, 1, 1), e=datetime(2000, 1, 1, 12, 0)),
    Row(a=2, b=3.0, c='string2', d=date(2000, 2, 1), e=datetime(2000, 1, 2, 12, 0)),
    Row(a=4, b=5.0, c='string3', d=date(2000, 3, 1), e=datetime(2000, 1, 3, 12, 0))
], schema)

# Exibição do DataFrame
df.show()