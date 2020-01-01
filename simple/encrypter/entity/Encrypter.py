from simple.encrypter.decorator.Singleton import Singleton

@Singleton
class Encrypter:
    def __init__(self):
        ascii_uppercase = range(65, 90)
        ascii_lowercase = range(97, 122)
        encryption_dict = dict()
        for i in ascii_uppercase:
            encryption_dict[chr(i)] = chr(i+1)
        encryption_dict['Z'] = 'A'
        for i in ascii_lowercase:
            encryption_dict[chr(i)] = chr(i+1)
        encryption_dict['z'] = 'a'
        self.encrypter_dict = encryption_dict
        decryption_dict = dict()
        for i in reversed(ascii_uppercase):
            decryption_dict[chr(i)] = chr(i-1)
        decryption_dict['A'] = 'Z'
        for i in reversed(ascii_lowercase) :
            decryption_dict[chr(i)] = chr(i-1)
        decryption_dict['a'] = 'z'
        self.decrypter_dict = decryption_dict

    def get_encrypter_dict(self) -> dict:
        return self.encrypter_dict

    def encrypt_string(self, input: str = "") -> str:
        return "".join(self.get_encrypter_dict()[key] if key in self.get_encrypter_dict() else key for key in input)

    def get_decrypter_dict(self) -> dict:
        return self.decrypter_dict

    def decrypt_string(self, input: str = "") -> str:
        return "".join(self.get_decrypter_dict()[key] if key in self.get_decrypter_dict() else key for key in input)