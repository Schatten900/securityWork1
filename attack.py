from vigenere import Vigenere,deque
import math
from functools import reduce

class VigenereAttack():
    def __init__(self,encrypt,portuguese=None):
        self.frequencyMessage = {}
        #get frequency of each letter on encrypt message
        mp = {}
        if encrypt:
            mp = {}
            for ch in encrypt:
                if ch in mp:
                    mp[ch] += 1
                else:
                    mp[ch] = 1

            self.frequencyMessage = mp

            self.frequencyEnglish = {
                'a': 8.167,'b': 1.492,'c': 2.78,'d': 4.253,
                'e': 12.702,'f': 2.228,'g': 2.015,'h': 6.094,'i': 6.966,'j': 0.153,
                'k': 0.772,'l': 4.025,'m': 2.406,'n': 6.749,'o': 7.507,'p': 1.929,
                'q': 0.095,'r': 5.987,'s': 6.327,'t': 9.056,'u': 2.758,
                'v': 0.978,'w': 2.360,'x': 0.150,'y': 1.974,'z': 0.074
            }

            if portuguese:
                self.portuguese = True
                self.frequencyPortuguese = {
                'a': 14.63,'b': 1.04,'c': 3.88,'d': 4.99,'e': 12.57,
                'f': 1.02,'g': 1.30,'h': 1.28,'i': 6.18,'j': 0.40,'k': 0.02,
                'l': 2.78,'m': 4.74,'n': 5.05,'o': 10.73,'p': 2.52,'q': 1.20,'r': 6.53,
                's': 7.81,'t': 4.34,'u': 4.63,'v': 1.67,'w': 0.01,'x': 0.21,'y': 0.01,'z': 0.47
                }
            else:
                self.frequencyPortuguese = {}

    def getFrequencyEncrypt(self):
        return self.frequencyMessage
    
    def getFrequencyEnglish(self):
        return self.frequencyEnglish
    
    def getFrequencyPortuguese(self):
        return self.frequencyPortuguese

    def getKeySize(self,encrypt):
        q = deque(encrypt)

        shifted = []
        for _ in range(len(encrypt)):
            shifted.append(list(q))
            q.rotate(1)  

        coincidences = []
        for i in range(1, len(encrypt)):  
            cont = 0
            for j in range(len(encrypt)):
                if j < len(shifted[i]):  
                    if encrypt[j] == shifted[i][j]:
                        cont += 1
            coincidences.append(cont)

        print("\nCoincidências por deslocamento:")
        for i, c in enumerate(coincidences):
            print(f"Deslocamento {i}: {c} coincidências")

        keySize = self.estimateKeySize(coincidences)
        return keySize

    
    def estimateKeySize(self,coincidences):
        media = sum(coincidences)/len(coincidences)
        highers = []
        for i in range(len(coincidences)):
            if coincidences[i] > media:
                highers.append(i)

        distances = []
        for i in range(len(highers)-1):
            distance = highers[i+1] - highers[i]
            distances.append(distance)

        if distances:
            keySize = reduce(math.gcd, distances)
            return keySize
        
        else:
            print("Not found any coincidence")
            return None


    def separeteBlocks(self,encrypt,keySize):
        # break ciphertext in blocks of key size
        
        blocks = []
        for i in range(0,len(encrypt),keySize):
            block = encrypt[i:i+keySize]
            blocks.append(block)
        print(blocks)

    def getDislocation(self):
        # 
        pass

    def createKey(self):
        # using the new key gerate
        pass


algoritimo = Vigenere()
mensage = "ATTACK AT DAWN"
key = "LEMON"
encrypt = algoritimo.encrypt(mensage,key)
decrypt = algoritimo.decrypt(encrypt,key)
print(encrypt)
print(decrypt)

attack = VigenereAttack(encrypt)
keySize = attack.getKeySize(encrypt)
attack.separeteBlocks(encrypt,keySize)