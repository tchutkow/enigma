

#when key is pressed, the rotors first rotate, then the signal is passed through
#https://www.ciphermachinesandcryptology.com/en/enigmatech.htm

class enigma_machine():
    
    def __init__(self,plugs,rotors):
        self.plugs = plugs
        self.rotors = rotors
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.reflection = "YRUHQSLDPXNGOKMIEBFZCWVJAT"
        self.rotation1 = self.alphabet.index(self.rotors[3])
        self.rotation2 = self.alphabet.index(self.rotors[4])
        self.rotation3 = self.alphabet.index(self.rotors[5])
        if self.rotors[0:3] == "123":
            self.orientation1 = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
            self.orientation2 = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
            self.orientation3 = "BDFHJLCPRTXVZNYEIWGAKMUSQO"
        elif self.rotors[0:3] == "132":
            self.orientation1 = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
            self.orientation2 = "BDFHJLCPRTXVZNYEIWGAKMUSQO"
            self.orientation3 = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
        elif self.rotors[0:3] == "213":
            self.orientation1 = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
            self.orientation2 = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
            self.orientation3 = "BDFHJLCPRTXVZNYEIWGAKMUSQO"
        elif self.rotors[0:3] == "231":
            self.orientation1 = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
            self.orientation2 = "BDFHJLCPRTXVZNYEIWGAKMUSQO"
            self.orientation3 = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
        elif self.rotors[0:3] == "312":
            self.orientation1 = "BDFHJLCPRTXVZNYEIWGAKMUSQO"
            self.orientation2 = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
            self.orientation3 = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
        elif self.rotors[0:3] == "321":
            self.orientation1 = "BDFHJLCPRTXVZNYEIWGAKMUSQO"
            self.orientation2 = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
            self.orientation3 = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"

    def reset(self):
        self.rotation1 = self.alphabet.index(self.rotors[3])
        self.rotation2 = self.alphabet.index(self.rotors[4])
        self.rotation3 = self.alphabet.index(self.rotors[5])

    def cipher(self,plaintext):

        ciphertext = ""
        for i in plaintext:
            self.rotate()
            step0 = self.plugboard(i)
            step1 = self.rotor1(step0)
            step2 = self.rotor2(step1)
            step3 = self.rotor3(step2)
            step4 = self.reflector(step3)
            step5 = self.rotor3_(step4)
            step6 = self.rotor2_(step5)
            step7 = self.rotor1_(step6)
            step8 = self.plugboard(step7)
            ciphertext += step8
            if len(ciphertext) == 6:
                if ciphertext[0:3] == ciphertext[3:6]:
                    key = ciphertext[0:3]
                elif plaintext[0:3] == plaintext[3:6]:
                    key = plaintext[0:3]
                self.rotation1 += self.alphabet.index(key[0])
                self.rotation2 += self.alphabet.index(key[1])
                self.rotation3 += self.alphabet.index(key[2])

        return ciphertext


    def rotate(self):
        self.rotation1 += 1
        if self.rotation1 == 26:
            self.rotation1 = 0
            self.rotation2 += 1
        if self.rotation2 == 26:
            self.rotation2 = 0
            self.rotation3 += 1
        if self.rotation3 == 26:
            self.rotation3 = 0
            

    def plugboard(self,inputtext):
        if inputtext in self.plugs:
            if self.plugs.index(inputtext) % 2 == 0:
                return self.plugs[(self.plugs.index(inputtext) + 1) % 26]
            else:
                return self.plugs[(self.plugs.index(inputtext) - 1) % 26]
        else:
            return inputtext

    def rotor1(self,inputtext):
        return self.orientation1[(self.alphabet.index(inputtext) + self.rotation1) % 26]

    def rotor2(self,inputtext):
        return self.orientation2[(self.alphabet.index(inputtext) + self.rotation2) % 26]

    def rotor3(self,inputtext):
        return self.orientation3[(self.alphabet.index(inputtext) + self.rotation3) % 26]

    def reflector(self,inputtext):
        return self.reflection[self.alphabet.index(inputtext)]

    def rotor3_(self,inputtext):
        return self.alphabet[(self.orientation3.index(inputtext) - self.rotation3) % 26]

    def rotor2_(self,inputtext):
        return self.alphabet[(self.orientation2.index(inputtext) - self.rotation2) % 26]

    def rotor1_(self,inputtext):
        return self.alphabet[(self.orientation1.index(inputtext) - self.rotation1) % 26]




enigma = enigma_machine("ENDKJO","231AQX")
        
