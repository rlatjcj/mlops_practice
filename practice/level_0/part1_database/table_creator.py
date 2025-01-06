import psycopg2


def create_table(db_connect):
    """Create a table in the database."""
    # PostgreSQL doesn't support float64 and int64, so we need to convert them to float8 and int respectively
    # PostgreSQL doesn't support some characters such as brackets, so we need to remove them
    # For these reasons, we need to use the below query
    create_table_query = """
    CREATE TABLE IF NOT EXISTS iris_data (
        id SERIAL PRIMARY KEY,
        timestamp timestamp,
        sepal_length float8,
        sepal_width float8,
        petal_length float8,
        petal_width float8,
        target int
    );"""
    print(create_table_query)
    with db_connect.cursor() as cur:
        cur.execute(create_table_query)
        db_connect.commit()


if __name__ == "__main__":
    # Connect to the database
    db_connect = psycopg2.connect(
        user="myuser",
        password="mypassword",
        host="localhost",
        port="5432",
        database="mydatabase",
    )

    # Create a table in the database
    create_table(db_connect)
