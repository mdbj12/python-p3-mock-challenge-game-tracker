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
        if type(title) == str and not hasattr(self, 'title') and len(title) >= 1:
            self._title = title
        else:
            raise Exception

    def results(self, new_result=None):
        from classes.result import Result
        if new_result and isinstance(new_result, Result):
            self._results.append(new_result)
        return self._results
    
    def players(self, new_player=None):
        from classes.player import Player
        if new_player and isinstance(new_player, Player):
            self._players.append(new_player)
        return self._players
    
    def average_score(self, player):
        sum = 0 
        for result in self._results:
            sum += result.score
        return sum/len(self._players)