# src/extract_data.py
import os
import time
import pandas as pd
from mwclient import Site
import requests
from config import HEADERS

def get_leaguepedia_data():
    print("Consultando datos de Pro Play en leaguepedia...")
    site = Site("lol.fandom.com",
                path="/",
                clients_useragent="KalistaAnalyticsProject/1.0 (Portfolio Project)",)
    
    time.sleep (3)

    response = site.api(
        "cargoquery",
        tables="ScoreboardGames=SG, ScoreboardPlayers=SP",
        join_on="SG.GameId=SP.GameId",
        fields=("SG.OverviewPage, SG.Gamelength, SP.Champion, SP.Win, SP.Gold, SP.CS"),
        where='SP.Champion="Kalista"',
        limit="200",
    )

    data = [item["title"] for item in response.get("cargoquery",[])]
    df= pd.DataFrame(data)
    print(f"Datos de Leaguepedia obtenidos total de registros: {len(df)}")
    return df 


if __name__ == "__main__":
          df_pro = get_leaguepedia_data()
          df_pro.to_csv("data/raw/kalista_pro_raw.csv", index=False)
          print("Archivo guardado en data/raw/kalista_pro_raw.csv")  
    