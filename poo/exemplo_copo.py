class Copo:
    def __init__(self, volume):
        self.volume = volume
 
    def encher(self):
        print("O copo está cheio.")
 
    def beber(self):
        print("Você bebeu a água.")
 
meu_copo = Copo(300)
meu_copo.encher()
meu_copo.beber()