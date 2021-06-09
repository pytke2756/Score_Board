from Player import Player

def DataIn(point, name): #point and name input
    line = str(point) + " - " + name
    return line

def main():

    
    f = open("score.txt", "a", encoding="UTF-8")

    f.write(DataIn(1000, "Levente") + "\n")
    f.close

main()
