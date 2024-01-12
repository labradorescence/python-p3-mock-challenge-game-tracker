class Result:

    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score

        player.results(self)
        player.games_played(game)

        game.results(self)
        game.players(player)

    @property
    def player(self):
        return self._player
    
    @player.setter
    def player(self, player):
        from classes.player import Player

        if isinstance(player, Player):
            self._player = player 
        else:
            raise Exception("Player must be an instance of Result class <3")
        
    @property
    def game(self):
        return self._game
    
    @game.setter
    def game(self, game):
        from classes.game import Game #1. import Game class
        if isinstance(game, Game): #2. check if the game parameter is an instance of the GAME class, if it is
            self._game = game #3. set the game 
        else:
            raise Exception("Game must be an instance of Result class! ^_^ ")