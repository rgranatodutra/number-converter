from converters import Converters as C

def convert_input(type: str, n: str):
    if type == "binária":
        oct, dec, hex = C.bin_to_oct(n), C.bin_to_dec(n), C.bin_to_hex(n)
        print(f"\nConversão do número binário {n} ->")
        print(f"- octal: {oct}")
        print(f"- decimal: {dec}")
        print(f"- hexadecimal: {hex}")
    if type == "octal":
        bin = C.oct_to_bin(n)
        dec, hex = C.bin_to_dec(bin), C.bin_to_hex(bin)
        print(f"\nConversão do número octal {n} ->")
        print(f"- binário: {bin}")
        print(f"- decimal: {dec}")
        print(f"- hexadecimal: {hex}")
    if type == "decimal":
        bin = C.dec_to_bin(n)
        oct, hex = C.bin_to_oct(bin), C.bin_to_hex(bin)
        print(f"\nConversão do número decimal {n} ->")
        print(f"- binário: {bin}")
        print(f"- octal: {oct}")
        print(f"- hexadecimal: {hex}")
    if type == "hexadecimal":
        bin = C.hex_to_bin(n)
        oct, dec = C.bin_to_oct(bin), C.bin_to_dec(bin)
        print(f"\nConversão do número hexadecimal {n} ->")
        print(f"- binário: {bin}")
        print(f"- octal: {oct}")
        print(f"- decimal: {dec}")

    