class Game:
    def __init__(self, title):
        self.title = title
        self._results = []
        self._players = []
        
    @property
    def title(self):
        return self._title
    @title.setter
    def title(self, title):
        if isinstance(title, str) and len(title) > 0 and not hasattr(self, 'title'):
            self._title = title 
        else:
            raise Exception("Title must be a string of 0 character.")

    def results(self, new_result=None):
        from classes.result import Result #0. import result class
        if new_result and isinstance(new_result, Result): 
              #1. if `new_result` exists.
#check if the new result is not already in the list 
            if new_result not in self._results:
                self._results.append(new_result) 
                #2. Adds new results to instance attribute `game._results`
        return self._results 
              #3. Returns a list of `Result` instances associated 
                # with the `Game` instance.
    
    def players(self, new_player=None):
        from classes.player import Player
        if new_player and isinstance(new_player, Player):
            self._players.append(new_player)
        return self._players
        pass
    
    def average_score(self, player):
        player_scores = [r.score for r in self._results if r.player == player]
        if player_scores:
            return sum(player_scores) / len(player_scores)
        return 0
        pass