from Player import Player

def DataIn(point, name): #point and name input
    line = str(point) + " - " + name
    return line

playersList = []

def main():

    fileIsEmpty = False
    with open("score.txt") as score:
        firstLine = score.read(1)
        if not firstLine:
            fileIsEmpty = True
        else:
            score.seek(0)
            allLines = score.readlines()
            for line in allLines:
                dataLine = line.rstrip().split("-")
                playerObj = Player(dataLine[0], dataLine[1])
                playersList.append(playerObj)


    for i in playersList:
        print(i)
    #f = open("score.txt", "a", encoding="UTF-8")

    #f.write(DataIn(1000, "Levente") + "\n")
    #f.close

main()
