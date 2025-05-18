from collections import deque
import unicodedata

class Vigenere:
    def __init__(self):  
        letters = []
        base = deque()
        for i in range(ord('A'), ord('Z') + 1):
            letters.append(chr(i))
            base.append(chr(i))

        mp = {}
        cont = 0
        for left in letters:
            q = deque(base)
            q.rotate(-int(cont))
            for right in letters:
                pair = (left,right)
                mp[pair] = q[0]
                q.rotate(-1)
            cont+=1

        self.table = mp


        reverse_mp = {}
        for (original,keyword),encrypt in self.table.items():
            pair = (encrypt,keyword)
            reverse_mp[pair] = original

        self.reverse_table = reverse_mp


    def getTable(self):
        return self.table
    
    def getReverseTable(self):
        return self.reverse_table
    
    def normalizeMensage(self,mensage):
        mensage = mensage.upper()
        mensage = mensage.replace(" ","")
        mensage = ''.join(c for c in unicodedata.normalize('NFD', mensage) if unicodedata.category(c) != 'Mn')
        mensage = "".join(c for c in mensage if c.isalpha())
        return mensage

    def encrypt(self,mensage,keyword) -> str:
        mensage = self.normalizeMensage(mensage)
        keyword = self.normalizeMensage(keyword)
        keystream = keyword
        cipherText = ""

        q = deque()
        for i in range(len(keyword)):
            q.append(keyword[i])

        while len(mensage) != len(keystream):
            keystream += q[0]
            q.rotate(-1)

        for i in range(len(keystream)):
            actual_encrypt = (mensage[i],keystream[i])
            table = self.getTable()
            cipherText += table[actual_encrypt]

        return cipherText


    def decrypt(self,encrypt,keyword) -> str:
        encrypt = encrypt.replace(" ","").upper()
        keyword = keyword.replace(" ","").upper()
        keystream = keyword
        original = ""

        q = deque()
        for i in range(len(keyword)):
            q.append(keyword[i])

        while len(encrypt) != len(keystream):
            keystream += q[0]
            q.rotate(-1)

        for i in range(len(keystream)):
            actual_pair = (encrypt[i],keystream[i])
            reverseTb = self.getReverseTable()
            original += reverseTb[actual_pair]
        
        return original
    