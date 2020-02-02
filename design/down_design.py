#up_execute
from random import*

def printinfo():
    print("this exe will Simulate some kind of competitive game between two players A and B")
    print("the exe needs the capacity of A and B (indicated by float:0~1)")

def getInputs():
    a=eval(input("please input the capacity of A:"))
    b=eval(input("please input the capacity of B:"))
    n=eval(input("simulation times:"))
    return a,b,n

def gameOver(scoreA,scoreB):
    if scoreA==15 or scoreB == 15:
        return True
    else:
        return False

def simOneGame(proA,proB):
    scoreA,scoreB=0,0
    serving="A"
    while not gameOver(scoreA,scoreB):
        if serving=="A":
            if random()<proA:
                scoreA+=1
            else:
                serving="B"
        else:
            if random()<proB:
                scoreB+=1
            else:
                serving="A"
    return scoreA,scoreB

def simNGames(n,proA,proB):
    winsA,winsB=0,0
    for i in range(n):
        scoreA,scoreB=simOneGame(proA,proB)
        if scoreA>scoreB:
            winsA+=1
        else:
            winsB+=1
    return winsA,winsB

def printSummary(winsA,winsB):
    n=winsA+winsB
    print("total times of the game is {} and his winrate is".format(n))
    print("player A have won {} times and his winrate is {:0.1%}".format(winsA,winsA/n))
    print("player B have won {} times and his winrate is {:0.1%}".format(winsB,winsB/n))    

def main():
    printinfo()
    proA,proB,n=getInputs()
    winsA,winsB=simNGames(n,proA,proB)
    printSummary(winsA,winsB) 

main()