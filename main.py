from select_menu import select_menu
from validate_input import validate_input
from convert_input import convert_input

print("Bem vindo(a) ao conversor de bases numéricas! \n")
selected_base = select_menu()
selected_number = validate_input(selected_base)
converted_number = convert_input(selected_base, selected_number)