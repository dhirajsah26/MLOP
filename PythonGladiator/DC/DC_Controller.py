import DC.DCModel as DCModel
import Connection.PGConn as PGConn

conn = PGConn.DBConnector()
player = DCModel.DC_Player()

class DC_Controller:
    def dc_conroller(self):
        n = int(input("Enter the number of details you want to enter: "))
        i =0
        while i < n:
            print("Enter details of ",i+1, " player of DC")

            name = input("Enter Player Name: ")
            player.set_player_name(name)

            height = float(input("Enter Player Height:"))
            player.set_player_height(height)

            weight = float(input("Enter player weight:"))
            player.set_player_weight(weight)

            num = int(input("Enter number of games played:"))
            player.set_num_of_games_played(num)

            # player.DCdata.append({
            #     "name": player.get_player_name(),
            #     "height": player.get_player_height(),
            #     "weight": player.get_player_weight(),
            #     "num_of_games_played": player.get_num_of_games_played()
            # })
            conn.insert_dc(player)
            i=i+1
        