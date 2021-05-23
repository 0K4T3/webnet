from .base import BaseCommand
from ..server import server


class StartCommand(BaseCommand):
    def process(self, port: int):
        server.run()
