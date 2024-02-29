from app.commands import Command

class Subtraction(Command):
    def execute(self, args):
        print(f"Result: {float(args[0]) - float(args[1])}") if len(args) == 2 else print("Invalid number of arguments for 'subtract' command.")
