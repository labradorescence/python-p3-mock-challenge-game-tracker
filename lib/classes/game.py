class Game:

    #constructor 
    def __init__(self, title): 
        self.title = title #set the title
        self._results = []
        self._players = []

    #getter/setter option 1
    # def get_title(self):
    #     return self._title
    
    # def set_title(self, title):
    #     self._title = title

    # title = property(get_title, set_title)

    #getter/setter option 2
    @property #property decorator
    def title(self): #getter 
        return self._title #return title property
    
    @title.setter  #setter
    def title(self, title):
        #check if inputted title is a string and length greater than 0
        #hasattr: false, if that attribute doesn't exist
        if isinstance(title, str) and len(title) > 0 and not hasattr(self, 'title'): 
            self._title = title #set the property with the inputted parameter, title
        else: #other wise
            raise Exception("1. Title must be a string of 0 character. 2. Title cannot be changed. ") 

    def results(self, new_result=None):
        from classes.result import Result
        if new_result and isinstance(new_result, Result): #1. if `new_result` exists.
            self._results.append(new_result) #2. Adds new results to instance attribute `game._results`
        return self._results #3. Returns a list of `Result` instances associated with the `Game` instance.
    
    def players(self, new_player=None):
        from classes.player import Player #1. import player class
        if new_player and isinstance(new_player, Player):
            #2. if new_player, in Player class
            self._players.append(new_player) #3. add the new player to the game.players list
        return self._players #4. return a list of 'Player' instances associated with the 'Game instance
        pass
    
    def average_score(self, player):
        player_scores = [r.score for r in self._results if r.player == player]
        if player_scores:
            return sum(player_scores) / len(player_scores)
        return 0
    


