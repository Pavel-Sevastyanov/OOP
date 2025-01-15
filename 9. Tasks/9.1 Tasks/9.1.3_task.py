from itertools import cycle
import string


class CaesarCipher:
    def __init__(self, shift):
        self.shift = shift

    def encode(self, text):
        encode_text = CaesarCipher.code('encode', text, self.shift)
        return encode_text

    def decode(self, text):
        decode_text = CaesarCipher.code('decode', text, self.shift)
        return decode_text

    @staticmethod
    def code(name_func, text, shift, low=string.ascii_lowercase, up=string.ascii_uppercase):
        if name_func == 'decode':
            low, up = low[::-1], up[::-1]
        new_text = ''
        for c in text:
            if c in string.ascii_letters:
                register, iter_letters = (low[0], cycle(low)) if c.islower() else (up[0], cycle(up))
                for i in range(abs(ord(c) - ord(register)) + shift):
                    next(iter_letters)
                c = next(iter_letters)
            new_text += c
        return new_text
