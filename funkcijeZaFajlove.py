with open("HemBotConfig", "r") as configFile:
    for line in configFile:
        if "name" in line:
            botName = line[5:]
        elif "avatar" in line:
            avatarUrl = line[7:]
        elif "auth_token" in line:
            authToken = line[11:]

def readLinesFromBellow(brojLinija, fileName):
    with open(fileName, "r") as datiFile:
        loopCount = 0
        arrayObavestenja = []
        for line in reversed(list(datiFile)):
            if loopCount >= 99 or loopCount >= int(brojLinija):
                return arrayObavestenja
            arrayObavestenja.append(line) 
            loopCount += 1
        return arrayObavestenja
            #print(line.rstrip())

def readObjectString(fileName, objectName, readStart=0, readEnd=-1):
    with open(fileName, "r") as datiFile:
        for line in datiFile:
            if objectName in line:
                objectValue = line[readStart:readEnd]
                return objectValue

def writeLineToFile(fileName, niskaZaPisanje):
    with open(fileName, "a") as datiFile:
        datiFile.write(niskaZaPisanje)
            