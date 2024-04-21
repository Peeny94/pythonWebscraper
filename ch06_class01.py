
class Player:
            
    def __init__(self,name,team):
        self.name = name
        self.xp =1500
        self.team =team
        
    def introduce(self):
        print(f"Hello! {self.team},{self.name},{self.xp}")

class Team:
    
    def __init__(self,team_name):
        self.name =team_name
        self.players =[]
        
        
    def show_players(self):
        for player in self.players:
            player.introduce()
        
        
    def add_player(self,name):
        new_player =Player(name,self.name)
        self.players.append(new_player)
        
    def del_player(self, name):
        for player in self.players:
            if player.name == name:
                self.players.remove(player)
                print(f"{name} has been removed from Team {self.name}")
                return
        print(f"{name} is not in Team {self.name}") 
               
    def total_xp(self):
        total_xp = sum(player.xp for player in self.players)
        return total_xp 

team_x =Team("Team X")
team_blue =Team("Team_blue")
team_blue.add_player("Lynn")
team_blue.add_player("Lion")
team_blue.show_players()
total_xp = team_blue.total_xp()  # 팀의 총 XP 값을 가져옵니다.
print(f"Total XP in Team {team_blue.name}: {total_xp}")
team_blue.del_player("Lynn")  # "Lynn" 플레이어를 삭제합니다.
team_blue.show_players()