import sys; from app.commands import Command; 
class ExitCommand(Command): 
    def execute(self, *a, **k): 
        e = "Terminating..." if a else "Terminating..."; c = k.get('exit_code', 0); sys.exit(f"{e}\nCode: {c}")
