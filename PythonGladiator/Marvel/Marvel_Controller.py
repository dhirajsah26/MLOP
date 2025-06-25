from Marvel.MarvelModel import Marvel_Player
import Connection.PGConn as PGConn
import pandas as pd


conn = PGConn.DBConnector()
# view = MarvelView.MarvelView()
player = Marvel_Player()

class Marvel_Controller:
    def marvel_controller(self):
        num = int(input("Enter the number of details you want to enter: "))
        i = 0
        while i < 5:
            print("Enter details of ",i+1, " player of Marvel")
            name = input("Enter Player Name: ")
            player.set_player_name(name)

            height = float(input("Enter Player Height:"))
            player.set_player_height(height)

            weight = float(input("Enter player weight:"))
            player.set_player_weight(weight)

            num = int(input("Enter number of games played:"))
            player.set_num_of_games_played(num)

            player.Marveldata.append({
                "name": player.get_player_name(),
                "height": player.get_player_height(),
                "weight": player.get_player_weight(),
                "num_of_games_played": player.get_num_of_games_played()
            })
            conn.insert_marvel(player)
            i=i+1
    






