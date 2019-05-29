class Player:
    def __init__(self, name):
        self.name = name
        self.owner = self
        self.neighbours = []
        self.territories = [self]
        self.highlight = 1
        self.rebellions = 0
        self.resists = 0
        self.roundsOfDefeat = []

    def setHighlight(self):
        if len(self.territories) > self.highlight:
            self.highlight = len(self.territories)

    def tryAssigningDefeat(self, round):
        if len(self.territories) == 0:
            self.roundsOfDefeat.append(round)
