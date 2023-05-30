from random import *
class RandomGen:

    CapLetter = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    NorLetter = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    num = ["0","1","2","3","4","5","6","7","8","9"]
    SpeChar = ["!","\"","#","$","%","&","\'","(",")","*","+",",","-",".","/",":",";","<","=",">","?","@","[","]","^","_","`","{","|","}","~"]
    length = 0
    password = []
    finalPass = ""


    def RandomLength(self):
        self.length = 0
        self.length = randrange(8,20)
        for i in range(self.length):
            self.password.append("t")
        self.finalPass = self.ChangePassword()

    def ChangePassword(self):
        for i in range(len(self.password)):
            temp = randrange(1,5)
            if temp == 1:
                j = randrange(0,len(self.CapLetter))
                self.password[i] = self.CapLetter[j]
            elif temp == 2:
                 j = randrange(0,len(self.CapLetter))
                 self.password[i] = self.NorLetter[j]
            elif temp == 3:
                j = randrange(0,len(self.CapLetter))
                self.password[i] = self.num[j]
            elif temp == 4:
                j = randrange(0,len(self.CapLetter))
                self.password[i] = self.SpeChar[j]

        finalPassword = "".join(self.password)
        return finalPassword

