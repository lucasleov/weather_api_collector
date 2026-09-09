from pathlib import Path
import sqlite3

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data"
DATABASE_PATH = DATA_DIR / "weather_api.db"

def initialize_database() -> None:
    DATA_DIR.mkdir(exist_ok=True)

    with sqlite3.connect(DATABASE_PATH) as connection:
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


def save_city(city: dict) -> None:
    values = (
        city['name'],
        city['country_code'],
        city['country'],
        city['timezone'],
        city['latitude'],
        city['longitude']
    )
    with sqlite3.connect(DATABASE_PATH) as connection:
        cursor = connection.cursor()
        try:
            cursor.execute(
                'INSERT INTO saved_cities (name, country_code, country, timezone, latitude, longitude) VALUES (?, ?, ?, ?, ?, ?)',
                values)
            connection.commit()
        except sqlite3.IntegrityError:
            return


def get_saved_cities() -> list[dict]:
    with sqlite3.connect(DATABASE_PATH) as connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.execute('SELECT * FROM saved_cities ORDER BY id')
        saved_city_list = cursor.fetchall()
    return [dict(row) for row in saved_city_list]


if __name__ == '__main__':
    initialize_database()

##    save_city({'name' : 'test_city',
##            'country_code' : 'test_country_code',
##            'country' : 'test_country',
##            'timezone' : 'test_timezone',
##            'latitude' : 25.5,
##            'longitude' : 35.55})

    print(get_saved_cities())
