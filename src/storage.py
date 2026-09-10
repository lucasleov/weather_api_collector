import sqlite3



def initialize_database(database_path) -> None:
    database_path.parent.mkdir(parents=True, exist_ok=True)

    with sqlite3.connect(database_path) as connection:
        connection.executescript(
            '''
            CREATE TABLE IF NOT EXISTS saved_cities (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                country_code TEXT NOT NULL,
                country TEXT NOT NULL,
                timezone TEXT NOT NULL,
                latitude REAL NOT NULL,
                longitude REAL NOT NULL,
                UNIQUE(name, country, latitude, longitude)
            );
            '''
        )
        connection.commit()


def save_city(city: dict, database_path) -> None:
    values = (
        city['name'],
        city['country_code'],
        city['country'],
        city['timezone'],
        city['latitude'],
        city['longitude']
    )
    with sqlite3.connect(database_path) as connection:
        cursor = connection.cursor()
        try:
            cursor.execute(
                'INSERT INTO saved_cities (name, country_code, country, timezone, latitude, longitude) VALUES (?, ?, ?, ?, ?, ?)',
                values)
            connection.commit()
        except sqlite3.IntegrityError:
            return


def get_saved_cities(database_path) -> list[dict]:
    with sqlite3.connect(database_path) as connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.execute('SELECT * FROM saved_cities ORDER BY id')
        saved_city_list = cursor.fetchall()
    return [dict(row) for row in saved_city_list]
