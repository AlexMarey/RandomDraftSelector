import time
import sys
import random

def sleepOneSecond():
    time.sleep(1)

def sleepInSeconds(timeInSeconds):
    time.sleep(timeInSeconds)

def getDraftTeamsFromFile(filename):
    with open(filename) as draftTeamFile:
        data = draftTeamFile.readlines()
    return [team.strip() for team in data]

def printDraftPick(draftSpot):
    ordinal = "th"
    if(draftSpot == 3):
        ordinal = "rd"
    elif(draftSpot == 2):
        ordinal = "nd"
    elif(draftSpot == 1):
        ordinal = "st"
    print("The {}{} overall draft pick goes to...".format(draftSpot, ordinal))

def printDraftTeam(team):
    print(team)

def printDraftRound(draftPick, team):
    printDraftPick(draftPick)
    sleepInSeconds(2)
    printDraftTeam(team)
    sleepInSeconds(2)
    print()

if __name__ == "__main__":
    filename = sys.argv[1]

    print('Retrieving Managers...')
    draftTeams = getDraftTeamsFromFile(filename)
    print('Managers have been gathered!')
    sleepOneSecond()

    print('Shuffling the draft order around...')
    random.shuffle(draftTeams)
    print('Shuffling complete!')
    sleepOneSecond()

    sleepOneSecond()
    print('The draft order for the 2019 Palmetto League will be announced shortly...\n')
    sleepInSeconds(5)
    draftPick = len(draftTeams)
    for team in draftTeams:
        printDraftRound(draftPick, team)
        draftPick -= 1
