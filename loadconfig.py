with open("HemBotConfig", "r") as configFile:
    for line in configFile:
        if "name" in line:
            botName = line[5:]
        elif "avatar" in line:
            avatarUrl = line[7:]
        elif "auth_token" in line:
            authToken = line[11:]
