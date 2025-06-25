

import mysql.connector
import Connection.db_config as db

class DBConnector:

    database_connector= mysql.connector.connect(
    host = db.host,
    user=db.user,
    password=db.password,
    database= db.database  # Ensure this database exists
    )

    cur= database_connector.cursor()
  
    def insert_marvel(self,player):
        sql = "insert into marvel  (player_name,height,weight,number_of_games_played) VALUES (%s, %s, %s, %s) "
        data = (player.get_player_name(),
                player.get_player_height(),
                player.get_player_weight(),
                player.get_num_of_games_played())
        self.cur.execute(sql,data)
        self.database_connector.commit(); #why do we use self
    
    def insert_dc(self,player):
        print("log from inert_dc db")
        sql = "insert into dc  (player_name,height,weight,number_of_games_played) VALUES (%s, %s, %s, %s) "
        data = (player.get_player_name(),
                player.get_player_height(),
                player.get_player_weight(),
                player.get_num_of_games_played())
        self.cur.execute(sql,data)
        self.database_connector.commit(); #why do we use self

    def fetch_all_marvel(self):
        fetch_query ="select * from marvel"
        self.cur.execute(fetch_query)
        result = self.cur.fetchall()
        return result

    def fetch_all_dc(self):
        fetch_query ="select * from dc"
        self.cur.execute(fetch_query)
        result = self.cur.fetchall()
        return result






