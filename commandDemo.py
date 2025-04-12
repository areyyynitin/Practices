def user_input_gen():
    while True:
        command = input("Enter a command(type 'exit' to quit):")
        if command.lower() == 'exit':
            break
        yield command

def process_commands():
    for command in user_input_gen():
        print(f"execute command : {command}")


process_commands()
