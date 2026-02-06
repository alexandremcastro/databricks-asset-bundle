import pytest

from pyspark.testing.utils import assertSchemaEqual
from pyspark.sql.types import (
    StructType,
    StructField,
    TimestampType,
    DoubleType,
    IntegerType,
)

from nyc_taxis.src.helpers.parameters import get_path


PROJECT: str = "nyc-analysis"
PATH: str = get_path(PROJECT)


def test_bronze_nyc_analysis_schema():
    """
    Test that the schema of the NYC analysis Spark table matches the expected bronze schema.

    The expected schema includes:
        - tpep_pickup_datetime: TimestampType
        - tpep_dropoff_datetime: TimestampType
        - trip_distance: DoubleType
        - fare_amount: DoubleType
        - pickup_zip: IntegerType
        - dropoff_zip: IntegerType
    """
    SCHEMA: StructType = spark.table(PATH).schema

    expected_schema = StructType(
        [
            StructField("tpep_pickup_datetime", TimestampType(), True),
            StructField("tpep_dropoff_datetime", TimestampType(), True),
            StructField("trip_distance", DoubleType(), True),
            StructField("fare_amount", DoubleType(), True),
            StructField("pickup_zip", IntegerType(), True),
            StructField("dropoff_zip", IntegerType(), True),
        ]
    )

    assertSchemaEqual(SCHEMA, expected_schema)
    print("Schemas are equal.")
