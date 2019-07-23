### This program develps a schedule for the League "Indiana's Finest"

import random

### Create Variables and Sets
### Team Schedules (start w/ neg ints to debug), eventually will be filled out with strings of opponents
David = [-10,-2,-3,-4,-5,-6,-7]
Daniel = [-1,-20,-3,-4,-5,-6,-7]
Zech = [-1,-2,-30,-4,-5,-6,-7]
Mitch = [-1,-2,-3,-40,-5,-6,-7]
MikeM = [-1,-2,-3,-4,-50,-6,-7]
Mark = [-1,-2,-3,-4,-5,-60,-7]
MikeA = [-1,-2,-3,-4,-5,-6,-70]
Chris = [-1,-2,-3,-4,-5,-6,-7]
Ryan = [-100,-2,-3,-4,-5,-6,-7]
Matt = [-1,-200,-3,-4,-5,-6,-7]
Alex = [-1,-2,-300,-4,-5,-6,-7]
Nick = [-1,-2,-3,-400,-5,-6,-7]
allTeamsSched = [David, Daniel, Zech, Mitch, MikeM, Mark, MikeA, Chris, Ryan, Matt, Alex, Nick]
teamDict = {"David": David, "Daniel": Daniel, "Zech": Zech, "Mitch": Mitch, "MikeM": MikeM, "Mark": Mark,
            "MikeA": MikeA, "Chris": Chris, "Ryan": Ryan, "Matt": Matt, "Alex": Alex, "Nick": Nick}
### Divisions
Boosh = ["David", "Daniel", "Zech", "Mitch"]
BooshSched = [David, Daniel, Zech, Mitch]
Kakow = ["MikeM", "Mark", "MikeA", "Chris"]
KakowSched = [MikeM, Mark, MikeA, Chris]
MasterCylinder = ["Ryan", "Matt", "Alex", "Nick"]
MasterCylinderSched = [Ryan, Matt, Alex, Nick]

#creates lists for editing
allTeams = []
allTeams = Boosh + Kakow + MasterCylinder

oppBoosh = []
oppBoosh = Kakow + MasterCylinder

oppBooshSched = []
oppBooshSched = KakowSched + MasterCylinderSched

oppKakow = []
oppKakow = Boosh + MasterCylinder

oppKakowSched = []
oppKakowSched = BooshSched + MasterCylinderSched

oppMasterCylinder = []
oppMasterCylinder = Boosh + Kakow

oppMasterCylinderSched = []
oppMasterCylinderSched = BooshSched + KakowSched

teamSched = [0,0,0,0,0,0,0]
count = 0
a = False
b = False
c = False


# Build functions
# Prints all schedules
def printAllSched():
    print
    print("David", David)
    print("Daniel", Daniel)
    print("Zech", Zech)
    print("Mitch", Mitch)
    print("MikeM", MikeM)
    print("Mark", Mark)
    print("MikeA", MikeA)
    print("Chris", Chris)
    print("Ryan", Ryan)
    print("Matt", Matt)
    print("Alex", Alex)
    print("Nick", Nick)


# clears schedule for all teams
def clearAllSched():
    for i in range(0,12):
        team = allTeamsSched[i]
        for j in range(0,7):
            team[j] = 0


# removes all previously-scheduled games for given week to avoid scheduling conflict
def removeWeekGames(week,oppTeams,allSchedule):
    for i in range(0,12):
        team = allSchedule[i]
        if team[week] in oppTeams:
            oppTeams.remove(team[week])
    return oppTeams


# add function to assign game to opp sched
def oppScheduler(week, team, oppTeam):
    oppTeamSched = teamDict[oppTeam]
    oppTeamSched[week] = team


# prevents overwriting a previously scheduled game
def alreadyScheduled(team, week):
    if type(team[week]) == str:
        return True
    else:
        return False


# assigns games for entire division
def divScheduler(dSched, Div, dOpp):
    for i in range(0,4):
        teamSched = dSched[i]
        team = Div[i]
        #print "team", team
        opp = dOpp[:]
        for j in range(0,7):
            #print "week", j
            weekOpponents = removeWeekGames(j,opp[:],allTeamsSched[:])
            #print "week opp", weekOpponents
            if not alreadyScheduled(teamSched, j):
                if len(weekOpponents) == 0:
                    return False
                y = len(weekOpponents)-1
                z = weekOpponents[random.randint(0,y)]
                teamSched[j] = z
                oppScheduler(j, team, z)
                opp.remove(teamSched[j])
                #print "opp", z
            #else:
                #print team, j, "already sched'd"
    return True


# Base Program
while not (a and b and c): #check function needs to be only test variable
    count += 1
    print("Attempt:", count)
    clearAllSched()
    a = divScheduler(BooshSched, Boosh, oppBoosh)
    b = divScheduler(KakowSched, Kakow, oppKakow)
    c = divScheduler(MasterCylinderSched, MasterCylinder, oppMasterCylinder) #redundant, replace with sched check function


print("And the final schedule is....")
printAllSched()



