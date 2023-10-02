class Player:
    def __init__(self: 'Player', player_id: int, player_name: str, car_number: int):
        self.player_id = player_id
        self.player_name = player_name
        self.car_number = car_number

    def __str__(self: 'Player'):
        return f"Player id: {self.player_id}, Player name: {self.player_name} (Car number: {self.car_number}, Team name: {self.team_name})"

    def set_team_name(self: 'Player', team_name: str):
        self.team_name = team_name

class Team:
    def __init__(self: 'Team', team_id: int, team_name: str, owner: str):
        self.team_id = team_id
        self.team_name = team_name
        self.owner = owner
        self.players = []

    def add_player(self: 'Team', player: 'Player', team_name: str):
        player.set_team_name(team_name)
        self.players.append(player)

    def __str__(self: 'Team'):
        return f"Team id: {self.team_id}, Team name: {self.team_name} (Owner: {self.owner})"


class League:
    def __init__(self: 'League', league_name: str, start_date: str):
        self.league_name = league_name
        self.start_date = start_date
        self.teams = {}

    def create_team(self: 'League', team_id: int, team_name: str, owner: str):
        team = Team(team_id, team_name, owner)
        self.teams[team_id] = team
        return team

    def get_team(self: 'League', team_id: int):
        return self.teams.get(team_id)

    def add_player_to_team(self: 'League', team_id: int, team_name: str,player: 'Player'):
        team = self.get_team(team_id)
        if team:
            team.add_player(player, team_name)
        else:
            print(f"Team with ID {team_id} not found.")

    def __str__(self):
        return f"Fantasy Racing Car League: {self.league_name} (Start Date: {self.start_date})"


# Example:
# Create a league
racing_league = League("Halifax Racing League", "2023-10-01")

# Create teams
team1 = racing_league.create_team(1, "Neural Network Team", "Dean")
team2 = racing_league.create_team(2, "Data Team", "Michael")

# Create players
player1 = Player(1, "Haidun", 58)
player2 = Player(2, "Laura", 22)
player3 = Player(3, "Avi", 5)
player4 = Player(4, "Sara", 7)

# Add players to teams
racing_league.add_player_to_team(1, "Neural Network Team", player1)
racing_league.add_player_to_team(1, "Neural Network Team", player2)
racing_league.add_player_to_team(2, "Data Team", player3)
racing_league.add_player_to_team(2, "Data Team",  player4)

# Display league, teams, and players
print(racing_league)
for team_id, team in racing_league.teams.items():
    print(team)
    for player in team.players:
        print(player)
