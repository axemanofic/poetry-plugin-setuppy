from cleo.commands.command import Command
from .services import *


class SetupPyCommand(Command):
    name = "setuppy"
    help = "This command will generate a setup.py file. And the next time you use it will update it."
    description = "This command will generate a setup.py file. And the next time you use it will update it."

    def handle(self) -> int:
        meta_data: dict = PackageService.collect_meta_data(self.application.poetry.package)
        generator = SetupPyGenerator(meta_data)
        generator.generate_file_py()
        return 0
