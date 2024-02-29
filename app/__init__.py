import os
from app.commands import CommandHandler
from app.plugins.menu import MenuCommand

class App:
    def __init__(self):
        self.command_handler = CommandHandler()
        self.load_commands()

    def load_commands(self):
        command_directory = "app/plugins"

        for subdirectory in os.listdir(command_directory):
            subdirectory_path = os.path.join(command_directory, subdirectory)
            if os.path.isdir(subdirectory_path):
                try:
                    if subdirectory.lower() == "menu":
                        command_instance = MenuCommand(self.command_handler)
                    else:
                        module = __import__(f"app.plugins.{subdirectory}", fromlist=["*"])
                        command_class = getattr(module, f"{subdirectory.capitalize()}Command")
                        command_instance = command_class()

                    self.command_handler.register_command(subdirectory, command_instance)
                except Exception as e:
                    print(f"Error loading command from {subdirectory_path}: {str(e)}")

    def start(self):
        print("Type 'exit' to exit.")
        while True:
            user_input = input(">>> ").strip().split()
            if not user_input:
                print("Please enter a command.")
                continue

            command_name, args = user_input[0].lower(), user_input[1:]
            try:
                self.command_handler.execute_command(command_name, args)
            except Exception as e:
                print(f"Error: {str(e)}")
