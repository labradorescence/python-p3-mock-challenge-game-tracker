class Result:

    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        Result.all.append(self)

        player.results(self) #add this result instance in the player.result 
        player.games_played(game)

        game.results(self) #add the result
        game.players(player) #collect all the players with the new player

    @property #getter 
    def score(self):
        return self._score

    @score.setter #setter 
    def score(self, score):
        if isinstance(score, int) and 1 <= score <= 5000:
            self._score = score
        else: 
            raise Exception("Scores must be integers between 1 and 5000, inclusive.")
        
    ###### player ########
    @property #getter 
    def player(self):
        return self._player
    
    @player.setter #setter 
    def player(self, player):
        from classes.player import Player   #1. import the Player class 
        #inside of the setter

        if isinstance(player, Player): #2. check if the player param is an instance of the PLAYER class 
            self._player = player #3. set the player 
        else:
            raise Exception("Player must be an instance of Result Class <3 ")

    ###### game ########   
    @property
    def game(self):
        return self._game
    
    #setter 
    @game.setter
    def game(self, game):
        from classes.game import Game #1. import the game class 
        if isinstance(game, Game): #2. check if the game param is in the class 
            self._game = game #set it up 
        else:
            raise Exception("Game must be an instance! ")