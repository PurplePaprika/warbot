import random as rnd
import repository as rep


def generateWorld():
    players = rep.players

    for c in rep.connections:
        findByName(c[0], players).neighbours.append(findByName(c[1], players))
        findByName(c[1], players).neighbours.append(findByName(c[0], players))

    return players


def findByName(name, players):
    for p in players:
        if p.name == name:
            return p


def attack(players, iterations):
    possibleAttackers = players[:]
    attacker = possibleAttackers[rnd.randrange(0, len(possibleAttackers))]
    possibleVictims = []
    available = False
    while not available:
        for n in attacker.neighbours:
            if n not in attacker.owner.territories:
                possibleVictims.append(n)
                available = True
        if not available:
            possibleAttackers.remove(attacker)
            attacker = possibleAttackers[rnd.randrange(0, len(possibleAttackers))]
            possibleVictims = []

    victimNumber = rnd.randrange(0, len(possibleVictims))
    victim = possibleVictims[victimNumber]

    print(attacker.owner.name, ', via', attacker.name, ', ataca', victim.name, 'sob dominio de', victim.owner.name)

    attacker.owner.territories.append(victim)
    victim.owner.territories.remove(victim)
    victim.owner.tryAssigningDefeat(iterations + 1)
    victim.owner = attacker.owner
    attacker.owner.setHighlight()
    return victim.name


def maybeRebel(players):
    probability = rnd.randrange(0, 100)
    if probability > 30:
        return ''
    rebel = players[rnd.randrange(0, len(players))]
    if rebel.owner != rebel:
        rebel.owner.territories.remove(rebel)
        rebel.territories.append(rebel)
        rebel.owner = rebel
        rebel.rebellions += 1
        return rebel.name
    return ''


def noWinner(players):
    p = 1
    while p < len(players):
        if players[p].owner != players[p-1].owner:
            return True
        p = p + 1
    return False


def writeReport (players, iterations):
    print("--------------------------------------RELATORIO--------------------------------------\n")
    cabecalho = players[0].owner.name + " venceu a guerra na rodada " + str(iterations) + "\n"
    print(cabecalho)

    for n in players:
        status = n.name + "\n- Maximo de territorios: " + str(n.highlight) + "  Rebelioes: " + str(n.rebellions) + "  Defesas: " + str(n.resists)
        if len(n.roundsOfDefeat) == 1:
            status = status + "  Derrotado na rodada " + str(n.roundsOfDefeat[0])
        elif len(n.roundsOfDefeat) > 1:
            status = status + "  Derrotado nas rodadas " + str(n.roundsOfDefeat)
        status = status +"\n"

        print (status)


def main():

    players = generateWorld()

    inicio = ''
    for p in players:
        inicio = inicio + ' ' + p.owner.name

    print("INICIO:", inicio, '\n')

    iterations = 0
    while noWinner(players):
        victimName = attack(players, iterations)
        rebelName = maybeRebel(players)
        iterations = iterations + 1
        status = ''
        for p in players:
            status = status + ' ' + p.owner.name

        if rebelName != '':
            if rebelName == victimName:
                status = status + ' - ' + rebelName + ' RESISTIU AO ATAQUE!'
                findByName(rebelName, players).resists += 1
            else:
                status = status + ' - ' + rebelName + ' REBELOU-SE!'
        print("FIM DA RODADA ", iterations, " :", status, "\n")

    print('VENCEDOR: ', players[0].owner.name, '\n')

    writeReport(players, iterations)

main()
