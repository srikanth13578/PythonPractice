# SBIVM
# Encryption Key = 1
# Decryption key = -1

name = "SBIVM"
key = -1

finalDecryptedString = ''
for ch in name:
   shifted = (ord(ch) - ord('A') + key) % 26
   resultchar = ord('A') + shifted
   finalDecryptedString+= chr(resultchar)

print(finalDecryptedString)