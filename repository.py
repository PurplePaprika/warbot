"""
@author: PurplePaprika
"""

from Player import Player

playerNames = ['Titanic','Bandejao','Elefante Branco','Biblioteca','CB','Cantina','Auditorios','Estacionamento','Ginasio',
               'Portaria da Ayrton Senna','Portaria do metro']
'''
playerNames = ['A','B','C']
'''
players = []

for p in playerNames:
    players.append(Player(p))

connections = [('Titanic', 'Bandejao'), ('Titanic', 'Estacionamento'), ('Biblioteca','Auditorios'), ('Auditorios', 'Titanic'),
               ('CB','Elefante Branco'),('CB','Cantina'),('Titanic','Cantina'),('Biblioteca','Cantina'),('Biblioteca','CB'),
               ('Ginasio','CB'), ('Ginasio','Cantina'), ('Ginasio','Biblioteca'), ('Ginasio','Portaria do metro'),
               ('Portaria do metro','Biblioteca'), ('Portaria do metro','Auditorios'), ('Auditorios','Portaria da Ayrton Senna'),
               ('Portaria da Ayrton Senna','Biblioteca'), ('Portaria da Ayrton Senna','Estacionamento'),
               ('Portaria da Ayrton Senna','Titanic')]
'''

connections = [('A','B'),('A','C'),('B','C')]
'''
