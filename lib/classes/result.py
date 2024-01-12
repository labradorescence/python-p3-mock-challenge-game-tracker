class Result:

    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        Result.all.append(self)

        player.results(self) 
        player.games_played(game)

        game.results(self)
        game.players(player)

    @property 
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        if isinstance(score, int) and 1<= score <= 5000 and not hasattr(self, 'score'):
            self._score = score 
        else:
            raise Exception("Scores must be of type int/Scores must be between 1 and 5000, inclusive/Should not be able to change after the result is instantiated")
        
    @property 
    def player(self): # getter 
        return self._player 
    @player.setter
    def player(self, player): #setter 
        from classes.player import Player #1. import the player class #inside of the setter 
        if isinstance(player, Player): # check if the #player parameter is the instance of the Player
            self._player = player # set the payer 

        else:
            raise Exception("Must be of instance of  Player class ")
        
    @property
    def game(self):
        return self._game
    @game.setter 
    def game(self, game):
        from classes.game import Game 
        if isinstance(game, Game): 
            self._game = game 
        else: 
            raise Exception(" Game must be an instance of class ")