CREATE DATABASE tournament;
\c tournament;

CREATE TABLE players ( name text, id serial primary key
);

CREATE TABLE matches ( match_id serial,
  winner integer REFERENCES players(id),
  loser integer REFERENCES players(id)
);

CREATE VIEW view_wins  AS
  SELECT players.id AS player, count(matches.winner) AS wins
  FROM players LEFT JOIN matches
  ON players.id = matches.winner
  GROUP BY players.id, matches.winner
  ORDER BY players.id;

CREATE VIEW view_match   AS
  SELECT players.id as player, count(matches) AS matches
  FROM players LEFT JOIN matches
  ON ((players.id = matches.winner) OR (players.id = matches.loser))
  GROUP BY players.id
  ORDER BY players.id;
