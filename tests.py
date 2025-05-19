from attack import VigenereAttack
from vigenere import Vigenere


class Testes():
    def __init__(self):
        self.vigenere = Vigenere()
        self.attackEN = VigenereAttack(portuguese=False)
        self.attackPT = VigenereAttack(portuguese=True)

    def encryptLongTextEnglish(self):
        mensage = "THEFORTRESSSTOODTALLAGAINSTTHEINVADINGARMIESITWASBUILTTOENDUREWARSANDSIEGESITSWALLSWERETHICKANDSTRONGANDTHEGATESWEREREINFORCEDWITHTHEBESTIRONFROMTHENORTHERNMOUNTAINSTHESOLDIERSWITHINTHEFORTRESSWEREBRAVETRAINEDANDSKEPTICALOFTHEENEMYSNEAKYTACTICSBUTTHEYKNEWTHEIRCAUSEWASJUSTANDTHEYWEREPREPAREDTOFIGHTTOTHELASTBREATH"
        key = "CASTLE"
        encrypt = self.vigenere.encrypt(mensage,key)
        print(f"Normal text: {mensage}")
        print(f"Encrypt text: {encrypt}")

    def decryptLongTextEnglish(self):
        mensage = "THEFORTRESSSTOODTALLAGAINSTTHEINVADINGARMIESITWASBUILTTOENDUREWARSANDSIEGESITSWALLSWERETHICKANDSTRONGANDTHEGATESWEREREINFORCEDWITHTHEBESTIRONFROMTHENORTHERNMOUNTAINSTHESOLDIERSWITHINTHEFORTRESSWEREBRAVETRAINEDANDSKEPTICALOFTHEENEMYSNEAKYTACTICSBUTTHEYKNEWTHEIRCAUSEWASJUSTANDTHEYWEREPREPAREDTOFIGHTTOTHELASTBREATH"
        key = "FOREST"
        encrypt = self.vigenere.encrypt(mensage,key)
        decrypt = self.vigenere.decrypt(encrypt,key)
        print(f"Encrypt text: {encrypt}")
        print(f"Decrypt text: {decrypt}")

    def encryptLongTextPortuguese(self):
        mensage = "O sertanejo é, antes de tudo, um forte. Não tem o raquitismo exaustivo dos mestiços neurastênicos do litoral. A sua compleição é rija, a sua disposição, altiva. É um homem que, ao invés de se curvar às adversidades do clima e da terra, aprende a resistir a elas com coragem e resignação. Nas vastidões áridas do interior, entre caatingas e veredas, ele ergue a sua vida com esforço e dignidade. Alimenta-se do pouco que a terra lhe dá, mas com isso basta-se. Sua fé é inabalável, sua esperança é constante, e seu espírito, embora rude, revela uma sabedoria ancestral que o tempo não apagou."
        key = "TRANQUILIDADE"
        encrypt = self.vigenere.encrypt(mensage,key)
        print(f"Normal text: {mensage}")
        print(f"Encrypt text: {encrypt}")

    def decryptLongTextPortuguese(self):
        mensage = "O sertanejo é, antes de tudo, um forte. Não tem o raquitismo exaustivo dos mestiços neurastênicos do litoral. A sua compleição é rija, a sua disposição, altiva. É um homem que, ao invés de se curvar às adversidades do clima e da terra, aprende a resistir a elas com coragem e resignação. Nas vastidões áridas do interior, entre caatingas e veredas, ele ergue a sua vida com esforço e dignidade. Alimenta-se do pouco que a terra lhe dá, mas com isso basta-se. Sua fé é inabalável, sua esperança é constante, e seu espírito, embora rude, revela uma sabedoria ancestral que o tempo não apagou."
        key = "TRANQUILIDADE"
        encrypt = self.vigenere.encrypt(mensage,key)
        decrypt = self.vigenere.decrypt(encrypt,key)
        print(f"Encrypt text: {encrypt}")
        print(f"Decrypt text: {decrypt}")

    def encryptShortTextEnglish(self):
        mensage = "ATTACK AT THE DAWN"
        key = "WAR"
        encrypt = self.vigenere.encrypt(mensage,key)
        print(f"Normal text: {mensage}")
        print(f"Encrypt text: {encrypt}")

    def decryptShortTextEnglish(self):
        mensage = "ATTACK AT THE DAWN"
        key = "SUNFIRE"
        encrypt = self.vigenere.encrypt(mensage,key)
        decrypt = self.vigenere.decrypt(encrypt,key)
        print(f"Encrypt text: {encrypt}")
        print(f"Decrypt text: {decrypt}")

    def encryptShortTextPortuguese(self):
        mensage = "O AMOR PREVALECE"
        key = "VERDE"
        encrypt = self.vigenere.encrypt(mensage,key)
        print(f"Normal text: {mensage}")
        print(f"Encrypt text: {encrypt}")

    def decryptShortTextPortuguese(self):
        mensage = "O  AMOR P REVA LECE SEMPRE"
        key = "BONE"
        encrypt = self.vigenere.encrypt(mensage,key)
        decrypt = self.vigenere.decrypt(encrypt,key)
        print(f"Encrypt text: {encrypt}")
        print(f"Decrypt text: {decrypt}")

    def attackLongTextEnglish(self):
        mensage = "THEFORTRESSSTOODTALLAGAINSTTHEINVADINGARMIESITWASBUILTTOENDUREWARSANDSIEGESITSWALLSWERETHICKANDSTRONGANDTHEGATESWEREREINFORCEDWITHTHEBESTIRONFROMTHENORTHERNMOUNTAINSTHESOLDIERSWITHINTHEFORTRESSWEREBRAVETRAINEDANDSKEPTICALOFTHEENEMYSNEAKYTACTICSBUTTHEYKNEWTHEIRCAUSEWASJUSTANDTHEYWEREPREPAREDTOFIGHTTOTHELASTBREATH"
        key = "NATURE"
        encrypt = self.vigenere.encrypt(mensage,key)
        print(f"Encrypt text: {encrypt}")
        original_text = self.attackEN.originalText(encrypt)

    def attackShortTextEnglish(self):
        mensage = "ATTACK AT THE DAWN"
        key = "FIRE"
        encrypt = self.vigenere.encrypt(mensage,key)
        print(f"Encrypt text: {encrypt}")
        original_text = self.attackEN.originalText(encrypt)

    def attackLongTextPortuguese(self):
        mensage = "O sertanejo é, antes de tudo, um forte. Não tem o raquitismo exaustivo dos mestiços neurastênicos do litoral. A sua compleição é rija, a sua disposição, altiva. É um homem que, ao invés de se curvar às adversidades do clima e da terra, aprende a resistir a elas com coragem e resignação. Nas vastidões áridas do interior, entre caatingas e veredas, ele ergue a sua vida com esforço e dignidade. Alimenta-se do pouco que a terra lhe dá, mas com isso basta-se. Sua fé é inabalável, sua esperança é constante, e seu espírito, embora rude, revela uma sabedoria ancestral que o tempo não apagou."
        key = "EsPiRItO"
        encrypt = self.vigenere.encrypt(mensage,key)
        print(f"Encrypt text: {encrypt}")
        original_text = self.attackPT.originalText(encrypt)

    def attackShortTextPortuguese(self):
        mensage = "O  AMOR P REVA LECE SEMPRE"
        key = "BONE"
        encrypt = self.vigenere.encrypt(mensage,key)
        print(f"Encrypt text: {encrypt}")
        original_text = self.attackPT.originalText(encrypt)

def testAll():
    tests = Testes()
    methods = dir(tests)
    for method in methods:
        if callable(getattr(tests, method)) and (
            method.startswith("encrypt") or 
            method.startswith("decrypt") or 
            method.startswith("attack")
        ):
            print(f"\n===== Executing: {method} =====")
            try:
                getattr(tests, method)()
            except Exception as e:
                print(f"An error ocurried on {method}: {e}")
