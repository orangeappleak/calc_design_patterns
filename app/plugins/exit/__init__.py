import sys
from app.commands import Command

class ExitCommand(Command):
    def execute(self, *args, **kwargs):
        exit_msg = "Terminating..." if args else "Terminating..."
        exit_code = kwargs.get('exit_code', 0)
        sys.exit(f"{exit_msg}\nCode: {exit_code}")
