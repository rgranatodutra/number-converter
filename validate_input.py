from validators import Validators

def validate_input(type: str) -> str:
    is_running = True
    print(f"\nDigite o numero de base {type} para continuar:\n")
    number_input = str("")

    while is_running:
        number_input = input()

        if type == "decimal":
            is_running = not Validators.decimal(number_input)
        elif type == "hexadecimal":
            is_running = not Validators.hexadecimal(number_input)
        elif type == "octal":
            is_running = not Validators.octal(number_input)
        elif type == "binária":
            is_running = not Validators.binary(number_input)

    return number_input

        
