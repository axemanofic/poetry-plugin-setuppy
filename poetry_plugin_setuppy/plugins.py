from poetry.console.application import Application
from poetry.plugins.application_plugin import ApplicationPlugin

from .commands import SetupPyCommand


class SetupPyPlugin(ApplicationPlugin):
    def activate(self, application: Application) -> None:
        application.command_loader.register_factory('setuppy', lambda: SetupPyCommand())
        return
