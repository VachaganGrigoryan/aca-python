
def encoder(string):
    return ''.join(f'{ord(letter):08b}' for letter in string)


def decoder(byte_str):
    return ''.join(chr(int(byte_str[i:i+8], 2)) for i in range(0, len(byte_str), 8))
