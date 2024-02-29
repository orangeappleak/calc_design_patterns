from app.commands import Command

class Addition(Command):
    def execute(self, args):
        result = sum(map(float, args))
        print(f"Result: {result}") if len(args) == 2 else print("Invalid number of arguments for 'add' command.")
