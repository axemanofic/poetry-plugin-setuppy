from cleo.commands.command import Command
from .services import *


class SetupPyCommand(Command):
    name = "setuppy"
    help = "This command will generate a setup.py file. And the next time you use it will update it."
    description = "This command will generate a setup.py file. And the next time you use it will update it."

    def handle(self) -> int:
        return 0
