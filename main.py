import argparse
from py.server import DarvesterAPI
from py.routes import guilds
from py.database import Database

argparser = argparse.ArgumentParser(description='Darvester API backend server.')
argparser.add_argument('--host', type=str, default='0.0.0.0', help='Host to bind to. (default: 0.0.0.0)')
argparser.add_argument('--port', type=int, default=8080, help='Port to listen on. (default: 8080)')
argparser.add_argument('--debug', action='store_true', help='Enable debug mode. (default: false)')
argparser.add_argument('--db', type=str, default='harvested.db', help='Database file to use. (default: harvested.db)')
args = argparser.parse_args()

db = Database(args.db)
server = DarvesterAPI(
    host=args.host,
    port=args.port,
    debug=args.debug,
    db=db
)

guilds.setup(server)

server.setup()
