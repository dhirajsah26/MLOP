
# import Marvel.Marvel_Controller as MarvelController
from Marvel.Marvel_Controller import Marvel_Controller
# import Marvel.Marvel_Controller as Marvel_Controller
import DC.DC_Controller as DCController
import Connection.PGConn as PGConn
from Marvel.MarvelView import MarvelView
import pandas as pd
    
db_conn = PGConn.DBConnector()

def main():
    name = input("Enyter your Name: ")
    print(" ")
    print("Hi",name,", Welcome to Python Gladiaotor Game ")
    while True:
        print("\n==== Main Menu ====")
        print("1. Add Marvel Player")
        print("2. ADD DC Player")
        print("3. Probability of selection of 2 from Marvel and 3 from DC teams")
        print("4. List all those stars who are heavier than SpiderMan and taller than Henery")
        print("5. List all those stars who have played more than 100 games and are heavier than Captain America")
        print("6. List of player whose summation of the stats (height, weight, and games played) is greater than 350 units")
        print("7. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            Marvel_Controller().marvel_controller()
        elif choice == '2':
            DCController.DC_Controller().dc_conroller()
        elif  choice == '3':
            get_selection_2_from_Marvel_and_3_from_DC_teams()
        elif  choice == '4':
            heaver_spiderman_and_taller_henery()
        elif  choice == '5':
            played_moreThan_100_games_and_heavier_than_Captain_America()
        elif  choice == '6':
            metaverse_summation_stats()
        elif choice == '7':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")
    # # Step 1: Setup DB (connect or create)
   

    # Step 2: Initialize controllers

def getDataFrame():
    marvel_player_data = db_conn.fetch_all_marvel()
    dc_player_data = db_conn.fetch_all_dc()
    col_names =["Id",'Name','Height(cm)','Weight(kg)','GamesPlayed']
    player_data_ = pd.concat([pd.DataFrame( marvel_player_data ,columns= col_names),pd.DataFrame( dc_player_data ,columns= col_names)] )

    return player_data_

    
def get_selection_2_from_Marvel_and_3_from_DC_teams():
    marvel_player_count=len(db_conn.fetch_all_marvel())
    print(marvel_player_count)
    Dc_player_count = len(db_conn.fetch_all_dc())
    prob_of_Marvel_2 = 2/marvel_player_count
    prob_of_DC_3 =3/Dc_player_count 
    probability_of_2_Marvel_and_3_DC = ( prob_of_Marvel_2 * prob_of_DC_3 )*100
    print("------------------------------------------------")
    print("Probability of selection of 2 from Marvel and 3 from DC teams",probability_of_2_Marvel_and_3_DC)


# 1.2) List all those stars who are heavier than SpiderMan and taller than Henery
def heaver_spiderman_and_taller_henery():
    data = getDataFrame()
    Henery_height = data[data["Name"]=="Henery"]["Height(cm)"].values[0]
    Spider_weight = data[data["Name"]=="SpiderMan"]["Weight(kg)"].iloc[0]
    for index, row in data.iterrows():
        if row["Weight(kg)"]>Spider_weight and row["Height(cm)"] > Henery_height  :
            print(row["Name"],"Is Heavier than SpiderMan and Taller than Henery."  )

# 1.3) List all those stars who have played more than 100 games and are heavier than Captain America.
def played_moreThan_100_games_and_heavier_than_Captain_America():
    data = getDataFrame()
    captain_America_weight = data[data["Name"] == "Captain America"]["Weight(kg)"].iloc[0]
    for index, row in data.iterrows():
        if row['GamesPlayed'] > 100 and row["Weight(kg)"] > captain_America_weight:
            print(f"{data['Name']} is heavier than Captain America and have played more than 100 games.")

# 1.4) For the given dataset representing stars from the Marvel and DC teams, if a metaverse is to be formed where the summation of the stats (height, weight, and games played) of any star is greater than 350 units, then display the names of all the stars meeting this criterion.
def metaverse_summation_stats():
    data = getDataFrame()
    for index, row in data.iterrows():
        summation_stats = row['Height(cm)']+ row['Weight(kg)']+ row['GamesPlayed']
        if summation_stats > 350:
            print(f"{row['Name']} has a summation stats greater than",summation_stats)

if __name__ == "__main__":
    main()