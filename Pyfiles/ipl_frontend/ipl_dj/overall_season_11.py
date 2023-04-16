import pandas as pd
from . import radar
import os
dirname = os.path.dirname(__file__)

def bat_stats_for_graph(all_data,eleven,name):
    bat_max_avg=all_data.sort_values(by="Avg_x",ascending=False,ignore_index=True).at[0,"Avg_x"]+10
    bat_max_runs=all_data.sort_values(by="Runs_x",ascending=False,ignore_index=True).at[0,"Runs_x"]+10
    bat_max_sr=all_data.sort_values(by="SR_x",ascending=False,ignore_index=True).at[0,"SR_x"]+10
    bat_max_4s=all_data.sort_values(by="4s",ascending=False,ignore_index=True).at[0,"4s"]+10
    bat_max_6s=all_data.sort_values(by="6s",ascending=False,ignore_index=True).at[0,"6s"]+10
    Max_stats=[bat_max_runs,bat_max_avg,bat_max_sr,bat_max_4s,bat_max_6s]
    k=eleven.loc[eleven["player_name"]==name]
    runs=list(dict(k["Runs_x"]).values())[0]
    avg=list(dict(k["Avg_x"]).values())[0]
    sr=list(dict(k["SR_x"]).values())[0]
    fours=list(dict(k["4s"]).values())[0]
    sixes=list(dict(k["6s"]).values())[0]
    L=[runs,avg,sr,fours,sixes]
    return radar.bat_graph(L+Max_stats,name)

def bowl_stats_for_graph(all_data,eleven,name):
    bowl_max_avg=all_data.sort_values(by="Avg_y",ascending=False,ignore_index=True).at[0,"Avg_y"]
    bowl_max_eco=all_data.sort_values(by="Econ",ascending=False,ignore_index=True).at[0,"Econ"]
    bowl_max_sr=all_data.sort_values(by="SR_y",ascending=False,ignore_index=True).at[0,"SR_y"]
    bowl_max_wkts=all_data.sort_values(by="Wkts",ascending=False,ignore_index=True).at[0,"Wkts"]
    Max_list=[bowl_max_wkts,bowl_max_avg,bowl_max_sr,bowl_max_eco]
    k=eleven.loc[eleven["player_name"]==name]
    wkts=list(dict(k["Wkts"]).values())[0]
    econ=list(dict(k["Econ"]).values())[0]
    sr=list(dict(k["SR_y"]).values())[0]
    avg=list(dict(k["Avg_y"]).values())[0]
    L=[wkts,avg,sr,econ]
    return radar.bowl_graph(L+Max_list,name)
    
def find_best_XI(folder):
    teamsacr = ['CSK', 'DC', 'GT', 'KKR', 'LSG', 'MI', 'PBKS', 'RR', 'RCB', 'SRH']
    teamsacr_before2022=['CSK','DC','KKR','MI','PBKS','RR','RCB','SRH'] 
    if (int(folder)<2023):
        teamsacr = teamsacr_before2022
    all_data=pd.DataFrame()
    #folder="2022" #input from user

    for team in teamsacr:
        bat_stats=pd.read_csv(f"{dirname}/{folder}/{team}_Batstats.csv")
        player_details=pd.read_csv(f"{dirname}/{folder}/{team}_players.csv")
        bowl_stats=pd.read_csv(f"{dirname}/{folder}/{team}_Bowlstats.csv")
        bat_stats["player_name"]=bat_stats["player_name"].str.upper()
        bowl_stats["player_name"]=bowl_stats["player_name"].str.upper()
        bat_stats=pd.merge(bat_stats,player_details,on=["player_name"])
        complete_stats=pd.merge(bat_stats,bowl_stats,on=["player_name"],how="outer").fillna(0)
        all_data=pd.concat([all_data,complete_stats],ignore_index=True)
    #print(all_data)


    all_data["total_score_bat"]=all_data["Runs_x"]*1.5+all_data["4s"]*0.5+all_data["6s"]-all_data["BF"]*0.5
    all_data["total_score_bat"]/=10
    all_data["total_score_bat"]+=(all_data["SR_x"]-120)/10+(all_data["Avg_x"]-30)/5
    #all_data=all_data.sort_values(by="total_score_bat",ascending=False)

    all_data["total_score_bowl"]=all_data["Wkts"]*20-all_data["Econ"]*2-all_data["SR_y"]*0.5-all_data["Avg_y"]*2
    all_data["total_score_bowl"]/=10

    all_round=all_data.loc[all_data["player_role"]=="All-Rounder"]
    all_round["total_score"]=all_round["total_score_bat"]+all_round["total_score_bowl"]
    batsmen=all_data.loc[all_data["player_role"]=="Batter"]
    bowlers = all_data.loc[all_data["player_role"]=="Bowler"]
    wks = all_data.loc[all_data["player_role"]=="WK Keeper - Batter"].sort_values("total_score_bat",ascending=False).head(1)
    all_round=all_round.sort_values("total_score",ascending=False).head(3)
    batsmen=batsmen.sort_values("total_score_bat",ascending=False).head(4)
    bowlers=bowlers.sort_values("total_score_bowl",ascending=False).head(3)
    eleven=pd.concat([batsmen,wks,all_round,bowlers],ignore_index=True)
    t=dict(eleven["player_name"])
    t1=list(dict.values(t))
    image1=bat_stats_for_graph(all_data,eleven,t1[0])
    image2=bowl_stats_for_graph(all_data,eleven,t1[8])
    #image2=bowl_stats_for_graph(all_data,eleven,t1[8])
    return t1,image1,image2

find_best_XI('2022')