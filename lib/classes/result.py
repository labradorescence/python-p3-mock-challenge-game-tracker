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
        if isinstance(score, int) and 1 <= score <= 5000:
            self._score = score
        else:
            raise Exception("Score must be an integer between 1 and 5000, inclusive")
        

    @property
    def player(self):
        return self._player
    
    @player.setter
    def player(self, player):
        from classes.player import Player #1. import Player class
        if isinstance(player, Player): #2. check if the player parameter is an instance of the PLAYER class
            self._player = player #3. setter
        else:
            raise Exception("Player must be an instance of Result class <3 ")
        
    @property
    def game(self):
        return self._game
    
    @game.setter
    def game(self, game):

        from classes.game import Game #1. import Game class inside of the setter

        if isinstance(game, Game): #2. check if the game parameter is an instance of the GAME class, if it is
            self._game = game #3. set the game 
        else:
            raise Exception("Game must be an instance of Result class! ^_^ ")

    