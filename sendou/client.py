import aiohttp
from typing import Dict, List, Optional
from .models import Tournament, TournamentTeam, User, Match


class Client:
    __header: Dict[str, str]

    def __init__(self, api_key: str, headers: Dict[str, str] = {}, url: Optional[str] = None):
        self.__headers = headers
        if "User-Agent" not in self.__headers:
            self.__headers["User-Agent"] = "Battlefy.py"
        if url:
            self.url = url
        else:
            self.url = "https://sendou.ink"
        self.__headers["Authorization"] = f"Bearer {api_key}"

    async def get_user(self, user_id: str) -> Optional[User]:
        """
        Get Sendou.ink user
        :param user_id: user_id or discord_id
        :return: None or User
        """
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.url}/api/user/{user_id}", headers=self.__headers) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    return User(data)
                else:
                    return None

    async def get_tournaments(self, tournament_id: str) -> Optional[Tournament]:
        """
        Get a list of tournaments
        :param tournament_id:
        :return: List of Tournaments
        """
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.url}/api/tournament/{tournament_id}", headers=self.__headers) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    return Tournament(data)
                else:
                    return None

    async def get_tournament_teams(self, tournament_id: str) -> Optional[List[TournamentTeam]]:
        """
        Get a list of tournament teams
        :param tournament_id:
        :return: List of TournamentTeams
        """
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.url}/api/tournament/{tournament_id}/teams", headers=self.__headers) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    return [TournamentTeam(team) for team in data]
                else:
                    return None

    async def get_tournament_match(self, match_id: str) -> Optional[Match]:
        """
        Get info on a tournament match
        :param match_id:
        :return: List of TournamentTeams
        """
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.url}/api/tournament-match/{match_id}", headers=self.__headers) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    return Match(data)
                else:
                    return None


