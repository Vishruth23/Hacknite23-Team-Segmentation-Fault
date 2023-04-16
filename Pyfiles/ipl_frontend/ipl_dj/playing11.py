import csv
import pandas as pd
from . import radar
import os
dirname = os.path.dirname(__file__)

def bat_stats_for_graph(all_data,name):
    bat_max_avg=all_data.sort_values(by="Avg",ascending=False,ignore_index=True).at[0,"Avg"]
    bat_max_runs=all_data.sort_values(by="Runs",ascending=False,ignore_index=True).at[0,"Runs"]
    bat_max_sr=all_data.sort_values(by="SR",ascending=False,ignore_index=True).at[0,"SR"]
    bat_max_4s=all_data.sort_values(by="4s",ascending=False,ignore_index=True).at[0,"4s"]
    bat_max_6s=all_data.sort_values(by="6s",ascending=False,ignore_index=True).at[0,"6s"]
    Max_stats=[bat_max_runs,bat_max_avg,bat_max_sr,bat_max_4s,bat_max_6s]

    runs=list(dict(all_data.loc[all_data["player_name"]==name]["Runs"]).values())[0]
    avg=list(dict(all_data.loc[all_data["player_name"]==name]["Avg"]).values())[0]
    sr=list(dict(all_data.loc[all_data["player_name"]==name]["SR"]).values())[0]
    fours=list(dict(all_data.loc[all_data["player_name"]==name]["4s"]).values())[0]
    sixes=list(dict(all_data.loc[all_data["player_name"]==name]["6s"]).values())[0]
    L=[runs,avg,sr,fours,sixes]
    #print(L)
    return radar.bat_graph(L+Max_stats,name)

def bowl_stats_for_graph(all_data,name):
    bowl_max_avg=all_data.sort_values(by="Avg",ascending=False,ignore_index=True).at[0,"Avg"]
    bowl_max_eco=all_data.sort_values(by="Econ",ascending=False,ignore_index=True).at[0,"Econ"]
    bowl_max_sr=all_data.sort_values(by="SR",ascending=False,ignore_index=True).at[0,"SR"]
    bowl_max_wkts=all_data.sort_values(by="Wkts",ascending=False,ignore_index=True).at[0,"Wkts"]
    Max_list=[bowl_max_wkts,bowl_max_avg,bowl_max_sr,bowl_max_eco]

    k=all_data.loc[all_data["player_name"]==name]
    wkts=list(dict(k["Wkts"]).values())[0]
    econ=list(dict(k["Econ"]).values())[0]
    sr=list(dict(k["SR"]).values())[0]
    avg=list(dict(k["Avg"]).values())[0]
    L=[wkts,avg,sr,econ]
    return radar.bowl_graph(L+Max_list,name)


def find_best_teamXI(team,folder):

    # team='PBKS' #input from the site
    # folder="2019"
    bat_stats=pd.read_csv(f"{dirname}/{folder}/{team}_Batstats.csv")
    player_details=pd.read_csv(f"{dirname}/{folder}/{team}_players.csv")
    bowl_stats=pd.read_csv(f"{dirname}/{folder}/{team}_Bowlstats.csv")
    bat_stats["player_name"]=bat_stats["player_name"].str.upper()
    bowl_stats["player_name"]=bowl_stats["player_name"].str.upper()
    bat_stats=pd.merge(bat_stats,player_details,on=["player_name"])
    bowl_stats=pd.merge(bowl_stats,player_details,on=["player_name"])
    bat_stats["total_score_bat"]=bat_stats["Runs"]*1.5+bat_stats["4s"]*0.5+bat_stats["6s"]-bat_stats["BF"]*0.5
    bat_stats["total_score_bat"]/=10
    bat_stats["total_score_bat"]+=(bat_stats["SR"]-120)/10+(bat_stats["Avg"]-30)/5
    bat_stats=bat_stats.sort_values(by="total_score_bat",ascending=False)
    bowl_stats["total_score_bowl"]=bowl_stats["Wkts"]*20-bowl_stats["Econ"]*2-bowl_stats["SR"]*0.5-bowl_stats["Avg"]*2
    bowl_stats["total_score_bowl"]/=10
    bowl_stats=bowl_stats.sort_values(by="total_score_bowl",ascending=False)
    all_stats=pd.merge(bat_stats,bowl_stats,on="player_name",how="outer").fillna(0)
    all_stats["total_score"]=all_stats["total_score_bat"]+all_stats["total_score_bowl"]
    all_stats=all_stats.loc[all_stats["player_role_x"]=="All-Rounder"].sort_values(by="total_score",ascending=False)
    t=dict(pd.concat([bat_stats.loc[bat_stats["player_role"]=="Batter"].head(4),bat_stats.loc[bat_stats["player_role"]=="WK Keeper - Batter"].head(1),all_stats.loc[all_stats["player_role_x"]=="All-Rounder"].head(3),bowl_stats.loc[bowl_stats["player_role"]=="Bowler"].head(3),],ignore_index=True)["player_name"])
    lt=3

    while(len(t)<=10):
        k=bowl_stats.loc[bowl_stats["player_role"]=="Bowler"]
        p = k.iloc[lt]["player_name"]
        lt=lt+1
        t[len(t)]=p

    image1=bat_stats_for_graph(bat_stats,t[0])
    image2=bowl_stats_for_graph(bowl_stats,t[8])
    return t,image1,image2
''' 
    image1=bat_stats_for_graph(bat_stats,table,t[0])
    return (list(dict.values(t))),image1
    '''
#find_best_teamXI("RR",2022)

