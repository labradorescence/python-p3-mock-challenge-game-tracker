class Player:

    all = []

    #initializer
    def __init__(self, username):
        self.username = username
        self._results = []
        self._games_played = []

    #properties
    @property #getter 
    def username(self):
        return self._username #return the username property
    
    @username.setter #setter property
    def username(self, username):
        if isinstance(username, str) and 2 <= len(username) <= 16: #if the username is string and length between 2 and 16 inclusive
                self._username = username #username property = username param
        else:
            raise Exception("Usernames must be strings between 2 and 16 characters, inclusive.")
        
    ### Object Relationship Attributes and Properties
    def results(self, new_result=None):
        from classes.result import Result #1. import the result class
        if new_result and isinstance(new_result, Result): # 2. if new_result exists
            self._results.append(new_result)
            #3. add new result to instance 
        return self._results #returns a list of result associated w the player
    
        #4. in the result class add it in the init method 
        pass
    
    def games_played(self, new_game=None):
        from classes.game import Game #import the game class
        if new_game and isinstance(new_game, Game): #if the game exists
            self._games_played.append(new_game) 
        return self._games_played #return a list of game instance 
    
        # go to result class and add the games_played
        pass


    ### Aggregate and Association Methods 
    def played_game(self, game):
        # for each in self._results:
        #     if each.player == self and each.game ==game:
        #         return True
        #     return False
        # pass
        return game in self._games_played
        #if the player has played this game before 

    def num_times_played(self, game):
        return len([ each_r for each_r in self._results if each_r.game == game])
        pass
    
#### Bonus: Aggregate and Association Method
    @classmethod
    def highest_scored(cls, game): #cls == class 
        if cls.all: 
            max_p = None
            max_score = 0

            for pl in cls.all:
                if game.average_score(pl) > max_score: 
                    max_p = pl
                    max_score = game.average_score(pl)
            return max_p
        return None
        pass
        
