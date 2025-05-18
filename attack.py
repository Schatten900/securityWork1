from vigenere import Vigenere
from collections import deque
import math
from functools import reduce

class VigenereAttack():
    def __init__(self, portuguese=False):
        frequencyEnglish = {
            'A': 8.167,'B': 1.492,'C': 2.78,'D': 4.253,
            'E': 12.702,'F': 2.228,'G': 2.015,'H': 6.094,'I': 6.966,'J': 0.153,
            'K': 0.772,'L': 4.025,'M': 2.406,'N': 6.749,'O': 7.507,'P': 1.929,
            'Q': 0.095,'R': 5.987,'S': 6.327,'T': 9.056,'U': 2.758,
            'V': 0.978,'W': 2.360,'X': 0.150,'Y': 1.974,'Z': 0.074
        }
        frequencyPortuguese = {
            'A': 14.63,'B': 1.04,'C': 3.88,'D': 4.99,'E': 12.57,
            'F': 1.02,'G': 1.30,'H': 1.28,'I': 6.18,'J': 0.40,'K': 0.02,
            'L': 2.78,'M': 4.74,'N': 5.05,'O': 10.73,'P': 2.52,'Q': 1.20,'R': 6.53,
            'S': 7.81,'T': 4.34,'U': 4.63,'V': 1.67,'W': 0.01,'X': 0.21,'Y': 0.01,'Z': 0.47
        }
        self.frequency = frequencyPortuguese if portuguese else frequencyEnglish

    def getFrequency(self):
        return self.frequency

    def indexCoincidences(self, text):
        # calculates index of coincidences in the encrypt text
        textSize = len(text)
        if textSize <= 1:
            return 0
        freqs = {}
        for ch in text:
            freqs[ch] = freqs.get(ch, 0) + 1

        # Uses IC formula
        ic = sum(f * (f - 1) for f in freqs.values()) / (textSize * (textSize - 1))
        return ic

    def findBestKeysizeByIc(self, encrypt, min_keysize=1, max_keysize=20):
        ic_scores = []
        for keysize in range(min_keysize, max_keysize + 1):
            # Create groups with size of range(min,max) from encrypt text
            groups = ['' for _ in range(keysize)]
            for i, ch in enumerate(encrypt):
                groups[i % keysize] += ch

            # Calculates the avarage IC of all groups and store 
            group_ics = [self.indexCoincidences(group) for group in groups]
            avg_ic = sum(group_ics) / keysize
            ic_scores.append((keysize, avg_ic))

        # IC next to 1 is a natural language indicate
        ic_scores.sort(key=lambda x: -x[1])
        return ic_scores

    def getTopKeySizes(self, encrypt, top=5):
        #Return the bests choices for key sizes
        keysize_guesses = self.findBestKeysizeByIc(encrypt, 1, 16)
        return [k[0] for k in keysize_guesses[:top]]

    def separeteBlocks(self, encrypt, keySize):
        return [encrypt[i:i+keySize] for i in range(0, len(encrypt), keySize)]

    def findingDislocationsBLocks(self, encrypt, keySize):
        # Separate encrypt text in blocks and group the dislocations
        blocks = self.separeteBlocks(encrypt, keySize)
        dislocations = []
        for i in range(keySize):
            aux = []
            for block in blocks:
                if i < len(block):
                    aux.append(block[i])
            dislocations.append(aux)
        return dislocations

    def shift_letter(self, ch, shift):
        return chr((ord(ch.upper()) - ord('A') - shift) % 26 + ord('A'))

    def estimateKey(self, encrypt, keySize):
        # Take all dislocations group 
        dislocations = self.findingDislocationsBLocks(encrypt, keySize)
        freqEnglish = self.getFrequency()
        estimateKey = []
        for block in dislocations:
            best_score = float('-inf')
            best_shift = 0
            for shift in range(26):
                # Shift all letters in block and apply dislocations freq analysis
                shifted = [self.shift_letter(ch, shift) for ch in block]
                freq = {}
                for ch in shifted:
                    freq[ch] = freq.get(ch, 0) + 1
                total = sum(freq.values())
                if total == 0:
                    continue
                score = 0
                for ch in freq:
                    freq_percent = freq[ch] / total
                    score += freq_percent * (freqEnglish.get(ch.upper(), 0) / 100)

                # Best score is the choice to find how many dislocations key had
                if score > best_score:
                    best_score = score
                    best_shift = shift

            estimateKey.append(best_shift)
        return estimateKey

    def originalText(self, encrypt):
        topKeySize = self.getTopKeySizes(encrypt)
        possiblesText = []

        # Apply for all possibles key sizes frequency algorithm 
        for keySize in topKeySize:
            print(f"Estimated key size: {keySize}")
            estimateKey = self.estimateKey(encrypt, keySize)
            key = "".join(chr(shift + ord('A')) for shift in estimateKey)
            print(f"Estimated key: {key}")

            #Decrypted mensage with estimated key
            decrypted = ""
            q = deque(estimateKey)
            for ch in encrypt:
                if ch.isalpha():
                    decrypted_ch = chr((ord(ch) - ord('A') - q[0]) % 26 + ord('A'))
                    decrypted += decrypted_ch
                    q.rotate(-1)
                else:
                    decrypted += ch
            print(f"Estimated decrypt text: {decrypted} \n")
            possiblesText.append(decrypted)

        return possiblesText
