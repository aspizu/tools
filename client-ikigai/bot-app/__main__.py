# CONFIGURATION:
TOKEN = "MTAwMDc4MDM4NTU1NjM4NTg3Mg.GoajWI.xriQLnrk37QwOTpBc4PUJ6eDqF9lyFue06RUAo"
DATABASE_FILE = "bot-app-database.db"
TARGET_CHANNEL_ID = 1000782014984761404
ADMIN_ROLE_ID = 1000848627532566669


def main():
    from client import Client
    import sqlite3

    with sqlite3.connect(DATABASE_FILE) as conn:
        client = Client(conn)
        client.run(TOKEN)


if __name__ == "__main__":
    main()
