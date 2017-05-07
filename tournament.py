import psycopg2

def connect():
    return psycopg2.connect("dbname=tournament")

def deleteMatches():
    db = connect()
    c = db.cursor()
    c.execute("DELETE FROM matches")
    db.commit()
    db.close()

def deletePlayers():
    db = connect()
    c = db.cursor()
    c.execute("DELETE FROM players")
    db.commit()
    db.close()

def countPlayers():
    db = connect()
    c = db.cursor()
    c.execute("SELECT count(*) FROM players")
    playerCount = c.fetchone()[0]
    db.close()
    return playerCount

def registerPlayer(name):
    db = connect()
    c = db.cursor()
    c.execute("INSERT INTO players VALUES (%s)",(name,))
    db.commit()
    db.close()

def playerStandings():
    db = connect()
    c = db.cursor()
    c.execute("SELECT id, name, view_wins.wins, view_match.matches FROM players LEFT JOIN view_wins ON (players.id = view_wins.player) LEFT JOIN view_match ON players.id = view_match.player GROUP BY players.id, players.name, view_wins.wins, view_match.matches ORDER BY view_wins.wins DESC")
    standings = c.fetchall();
    db.close()
    return standings

def reportMatch(winner, loser):
    db = connect()
    c = db.cursor()
    c.execute("INSERT INTO matches (winner,  loser) VALUES (%s,%s)",(int(winner),int(loser)))
    db.commit()
    db.close()

def swissPairings():
    standings = playerStandings()
    num = int(countPlayers())
    match_pair = []
    if (num>0):
        for i in range (num):
            if (i%2 == 0):
                id1 = standings[i][0]
                name1 = standings[i][1]
                id2 = standings[i+1][0]
                name2 = standings[i+1][1]
                pair = (id1, name1, id2, name2)
                match_pair.append(pair)
    return match_pair
