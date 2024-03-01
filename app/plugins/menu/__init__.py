from app.commands import Command

class MenuCommand(Command):
    def __init__(self, command_handler):
        self.command_handler = command_handler

    def execute(self, *args):
        print("Available Commands:")
        print("\n".join([f"- {command_name}" for command_name in self.command_handler.commands]))
