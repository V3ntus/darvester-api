from py.server import DarvesterAPI
from py.database import Database


def setup(api: DarvesterAPI):
    """
    Setup API routes for guilds

    :param api: The API server.
    :type api: DarvesterAPI
    :param db: The database instance.
    :type db: Database
    """

    @api.get("/guilds")
    def get_guilds():
        """
        Get all guilds.
        """
        return {"guilds": [_ for _ in api.db.conn.execute("SELECT * FROM guilds")]}
