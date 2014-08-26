DEBUG = True

# Make these unique, and don't share it with anybody.
SECRET_KEY = "20eb5cef-0398-4c10-a50c-8dbe43cd2137cb184c97-4c39-4238-a84b-dbb8ada62c166f34b142-a194-4bbe-af42-ea714c91918f"
NEVERCACHE_KEY = "b124764d-c2fd-4e2d-9fa0-99ea92f7d226e6ecdb89-30e1-4907-b210-9b455f9637fbc77f17c6-7daa-4d1a-b8b8-0df8499b18e9"

DATABASES = {
    "default": {
        # Ends with "postgresql_psycopg2", "mysql", "sqlite3" or "oracle".
        "ENGINE": "django.db.backends.sqlite3",
        # DB name or path to database file if using sqlite3.
        "NAME": "dev.db",
        # Not used with sqlite3.
        "USER": "",
        # Not used with sqlite3.
        "PASSWORD": "",
        # Set to empty string for localhost. Not used with sqlite3.
        "HOST": "",
        # Set to empty string for default. Not used with sqlite3.
        "PORT": "",
    }
}
