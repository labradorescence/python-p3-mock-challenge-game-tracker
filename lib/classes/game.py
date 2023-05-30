class Game:
    # init method / constructor 
    def __init__(self, title): 
        self.title = title #setting the title
        self._results = []
        self._players = []

    # #getter / setter option 1
    # def get_title(self): #getter
    #     return self._title #returning the title property
    
    # def set_title(self, title) #setter
    #     self._title = title #setting up the title property with the inputted title param

    # title = property(get_title, set_title) # compile getter and setter 


    # option 2: property decorator
    #getter
    @property #1. property decorator using the pie symbol
    def title(self): #2. getter function 
        return self._title  #3. return the title property
    
    #setter 
    @title.setter #1. setter 
    def title(self, title): # 2. function to add property
        #3. if the inputted title is a string
        #4. if the length is greater than 0
        #5. has attr : false the attr doesn't exist 
        #    if it's true the attr exist
        if isinstance(title, str) and len(title) > 0 and not hasattr(self, 'title'):
            self._title = title #set the title
        else:
            raise Exception("Title must be string greater than 0 character. Title cannot be changed after the game is initialized ")


    def results(self, new_result=None):
        from classes.result import Result
        if new_result and isinstance(new_result, Result):
            #1. if new result exist
            self._results.append(new_result)
             #2. add new results to instance att

        return self._results
            #3. return the lst of result instance associated with the game instance
        pass
    
    def players(self, new_player=None):
        from classes.player import Player
        if new_player and isinstance(new_player, Player):
            self._players.append(new_player) # add the new player to the game.player list 
        return self._players
        #return a list of players instance associated with this particular game 
        pass
    
    def average_score(self, player):
        pass