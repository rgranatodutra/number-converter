class Converters:
    @staticmethod
    def bin_to_dec(n: str):
        return int(n, 2)
    
    @staticmethod
    def bin_to_oct(n: str):
        return oct(int(n, 2))[2:]
    
    @staticmethod 
    def bin_to_hex(n: str):
        return hex(int(n, 2))[2:]
    
    @staticmethod
    def oct_to_bin(n: str):
        return bin(int(n, 8))[2:]
    
    @staticmethod
    def dec_to_bin(n: str):
        return bin(int(n))[2:]
    
    @staticmethod
    def hex_to_bin(n: str):
        return bin(int(n, 16))[2:]