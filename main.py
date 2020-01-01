from simple.encrypter.entity.Encrypter import Encrypter

message1 = "This is original message"
print("Original message:", message1)
encrypted1 = Encrypter.Instance().encrypt_string(input = message1)
print("Encrypted message:", encrypted1)
decrypted1 = Encrypter.Instance().decrypt_string(input = encrypted1)
print("Decrypted message:", decrypted1)