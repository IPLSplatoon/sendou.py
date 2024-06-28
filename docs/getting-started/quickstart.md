# Quick Start

This quickstart assumes you know how to use AsyncIO and write asynchronous code in Python.

## [Getting Player Info](/References/client/#sendou.client.Client.get_user)

```python
from sendou import Client
client = Client("API_KEY")
player = await client.get_user("USER_ID")
```

## [Getting Tournament Info](/References/client/#sendou.client.Client.get_tournament)

```python
from sendou import Client
client = Client("API_KEY")
tournament = await client.get_tournament("TOURNAMENT_ID")
```

### [Getting Tournament Teams](/References/models/tournament.md#sendou.models.Tournament.get_teams)

```python
from sendou import Client
client = Client("API_KEY")
tournament = await client.get_tournament("TOURNAMENT_ID")
teams = await tournament.get_teams()
```

### Get Player from Team member

```python
from sendou import Client
client = Client("API_KEY")
tournament = await client.get_tournament("TOURNAMENT_ID")
teams = await tournament.get_teams()
for team in teams:
    for member in team.members:
        player = await member.get_player()
```

### Getting Tournament Bracket(s)

```python
from sendou import Client
client = Client("API_KEY")
tournament = await client.get_tournament("TOURNAMENT_ID")
for bracket in tournament.brackets:
    bracket_data = await bracket.get_data()
```

## Getting Tournament Match Info
**Note:** This is not linked to the bracket. You need to know the match ID.

(*This will be updated in future when documentation is updated*)

```python
from sendou import Client
client = Client("API_KEY")
match = await client.get_tournament_matches("Match_ID")
```