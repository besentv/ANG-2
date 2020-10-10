import random
import datetime

class Idd:

    iddChars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'C', 'F',
                'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'R', 'T', 'V', 'W', 'X', 'Y', 'Z']

    iddCharsDict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'G': 16, 'H': 17,
                    'I': 18, 'J': 19, 'K': 20, 'L': 21, 'M': 22, 'N': 23, 'O': 24, 'P': 25, 'Q': 26, 'R': 27, 'S': 28, 'T': 29, 'U': 30, 'V': 31, 'W': 32, 'X': 33, 'Y': 34, 'Z': 35}

    def __init__(self, authorityId :str, countingId :str, birthdate :datetime, expirationDate :datetime):
        self.authorityId :str = authorityId
        self.countingId :str = countingId
        self.birthdate = birthdate
        self.expirationDate = expirationDate
    
    #Creates a random valid 18+ IDD.
    @classmethod
    def createRandom(cls):
        authorityId :str = Idd.createRandomIddString(4)
        countingId :str = Idd.createRandomIddString(5)
        today = datetime.datetime.today()
        deltaBirthday = datetime.timedelta(weeks=random.randint(1038,1042)) #~20 years
        deltaValidDate = datetime.timedelta(weeks=random.randint(200,220)) #~4 years
        birthdate = today - deltaBirthday #Select a birthday 20 years ago
        expirationDate = today + deltaValidDate #Set expiration date to be in 4 yearss

        return cls(authorityId,countingId, birthdate, expirationDate)

    @classmethod
    def createRandomIddString(self, len: int):
        iddString = ""

        for _ in range(len):
            iddString += random.choice(self.iddChars)
        
        return iddString
    
    def getChecksumOf(self, string: str):
        multiplyer = [7,3,1]
        multiplyIndex = 0
        checksum = 0

        for s in string:
            checksum += ((self.iddCharsDict[s] * multiplyer[multiplyIndex]) % 10)
            #print("Checksum for " + s + " -> " + str((self.iddCharsDict[s] * multiplyer[multiplyIndex]) % 10) + " Multiply Index: " + str(multiplyIndex) + "=" + str(multiplyer[multiplyIndex]))
            multiplyIndex = ((multiplyIndex + 1) % 3) #Index range: 0-2
            
        
        return str((checksum % 10))
    
    def dateToIddStr(self, date: datetime):
        return date.strftime('%y%m%d')

    #First "number" of the IDD
    def generateIdentificationPart(self):
        identificationPart: str = ""
        identificationPart += self.authorityId
        identificationPart += self.countingId
        identificationPart += self.getChecksumOf(identificationPart)

        return identificationPart

    #Second "number" of the IDD
    def generateBirtdayPart(self):
        birthdayStr: str = ""
        birthdayStr += self.dateToIddStr(self.birthdate)
        birthdayStr += self.getChecksumOf(birthdayStr)

        return birthdayStr

    #Third "number" of the IDD
    def generateExpirationPart(self):
        exprStr: str = ""
        exprStr += self.dateToIddStr(self.expirationDate)
        exprStr += self.getChecksumOf(exprStr)

        return exprStr

    def __str__(self):

        iddString: str = ""

        iddString += ("IDD<<" + self.generateIdentificationPart() + "<<<<<<<<<<<<<<<\n")
        iddString += (self.generateBirtdayPart() + "<" + self.generateExpirationPart() + "D" + "<<<<<<<<<<<<<")
        iddString += self.getChecksumOf(self.generateIdentificationPart() + self.generateBirtdayPart() + self.generateExpirationPart())

        return iddString
    
