def select_menu() -> str:
    options = ["decimal", "hexadecimal", "octal", "binária"]

    print("Para começar, selecione a base do número que deseja converter:")

    for index, option in enumerate(options):
        print(f"{index + 1} - {option}")

    print("\nDigite 'x' para saír \n")
   
    is_running = True

    while is_running:
        user_input = input()

        if user_input == "x":
            is_running = False

        if not user_input.isnumeric():
            print("\nVocê deve digitar um valor numérico\n")
            continue
        elif not (int(user_input) > 0 and int(user_input) <= len(options)):
            print(f"\nOpção inválida, selecione um valor entre '1' e '{len(options)}' ou 'x' para sair...\n")
            continue
        else:
            return options[int(user_input)-1]
