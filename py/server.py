import asyncio
import logging

from fastapi import FastAPI
from uvicorn import Config, Server

from py.cache import Caches
from py.database import Database

logger = logging.getLogger("api_server")


class DarvesterAPI:
    def __init__(self, **kwargs):
        """
        Darvester API backend server.

        :param host: The host to bind to. (default: '0.0.0.0')
        :type host: str
        :param port: The port to listen on. (default: 8080)
        :type port: int
        :param debug: Enable debug mode. (default: false)
        :type debug: bool
        :param caches: The caches to use.
        :type caches: Caches
        """
        self._loop: asyncio.AbstractEventLoop = asyncio.get_event_loop()

        self.api: FastAPI = FastAPI()
        self.host: str = kwargs.get('host', '0.0.0.0')
        self.port: int = kwargs.get('port', 8080)
        self.debug: bool = kwargs.get('debug', False)
        self.config: Config = Config(
            app=self.api,
            host=self.host,
            port=self.port,
            debug=self.debug
        )
        self.server: Server = Server(self.config)

        self.db: Database = kwargs.get('db', Database("harvested.db"))

        # Method aliases
        self.get = self.api.get
        self.post = self.api.post
        self.delete = self.api.delete
        self.put = self.api.put
        self.options = self.api.options
        self.head = self.api.head
        self.patch = self.api.patch
        self.trace = self.api.trace

        if kwargs.get("caches", False) and isinstance(kwargs.get("caches"), Caches):
            self.caches: Caches = kwargs.get("caches")
        else:
            self.caches: Caches = Caches()

    def setup(self):
        # Start the uvicorn server
        self._loop.run_until_complete(self.server.serve())
