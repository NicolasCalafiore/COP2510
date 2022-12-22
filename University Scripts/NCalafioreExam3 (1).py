## Nicolas Calafiore
## U94446501
## Created class Player which inherits Person. Player requires paremeters userName, teamName, ranking, realName and Person is init when Player is init with paremeter name
## Class Player contains the necessary functions to determine prize and prize bonus depending on rank.
## Once the instance of Player is created after all the inputs the __str__ function is called which calls on these inner methods to calculate the prize and bonus.
## The string calls the necessary functions or variables and is then printed


class Person:
    
    def __init__(self, name):
        self.realName = name

    def getRealName(self):
        return realName


class Player(Person):
    
    def __init__(self, user, team, rank, name):
        Person.__init__(self, name)
        self.username = user
        self.teamName = team
        self.teamRank = rank
        
    def playerEarnings(self):
        earnings = self.baseEarnings() * (self.bonusEarnings()/100)
        return int(earnings)
        

    def __str__(self):
        a = 10
        
    def baseEarnings(self):

        reward = 0

        rewards = {
            "1" : 486500,
            "2" : 333750,
            "3" : 178000,
            "4" : 100125,
            "5" : 55625
            }
   
        if self.teamRank == "1" or self.teamRank == "2" or self.teamRank == "3" or self.teamRank == "4" or self.teamRank == "5":
            reward = rewards[self.teamRank]
            
        return reward


    def bonusEarnings(self):
        reward = 0
        
        rewards = {
        "1" : 25,
        "2" : 20,
        "3" : 15,
        "4" : 10,
        "5" : 5
        }

        if self.teamRank == "1" or self.teamRank == "2" or self.teamRank == "3" or self.teamRank == "4" or self.teamRank == "5":
            reward = rewards[self.teamRank]
        
        return reward
    

    def __str__(self):
        
        rankEnd = ''

     
        if self.teamRank == "1":
            rankEnd = "st"
        elif self.teamRank == "2":
            rankEnd = "nd"
        elif self.teamRank == "3":
            rankEnd = "rd"
        else:
            rankEnd = "th"
            
        print("Team " + self.teamName + " placed " + self.teamRank + rankEnd + " so they win $" + str(self.baseEarnings()) + ".00 with a bonus of " + str(self.bonusEarnings()) + ".0%")
        print(self.getRealName() + " (aka " + self.username + ")'s earnings is: $" + str(self.playerEarnings()) + ".00")


    



realName = str(input("Enter the player's real name: "))
userName = str(input("Enter the player's game name: "))
teamName = str(input("Enter the team's name: "))
ranking = str(input("How did the team do (Integer)?: "))

player = Player(userName, teamName, ranking, realName)
player.__str__()





































    
