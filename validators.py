def validate_base(valid_digits, n, base):
    for digit in n:
        if not str(digit).upper() in valid_digits:
            print(f"\nNúmero inválido, digite um valor na base {base}: \n")
            return False
    return True

class Validators:
    @staticmethod
    def decimal(n: str):
        return validate_base("0123456789", n, "decimal")
        
    @staticmethod
    def hexadecimal(n: str):
        return validate_base("0123456789ABCDEF", n, "hexadecimal")
            
    @staticmethod
    def octal(n: str):
        return validate_base("01234567", n, "octal")
    
    @staticmethod
    def binary(n: str):
        return validate_base("01", n, "binary")
            
