import pandas as pd
from selenium import webdriver
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import os
dirname = os.path.dirname(__file__)

def predictXI():
    options = ChromeOptions()
    #options.binary_location = '/Applications/Brave Browser.app/Contents/MacOS/Brave Browser'
    PATH='./chromedriver.exe'
    options.headless=False

    website = 'https://fantasy.iplt20.com/season/home?source=organic'
    ser = Service(PATH)
    wd = webdriver.Chrome(options = options, service=ser)

    wd.get(website)
    wd.maximize_window()
    



    #wd.find_element(By.XPATH, '//*[@id="home-widget"]/div/div/div/div/div[2]/div[5]/div/a').click()
    WebDriverWait(wd, 3).until(EC.presence_of_all_elements_located((By.XPATH, '//div[@class="df-fix__team-name"]/span')))
    tt = wd.find_elements(By.XPATH, '//div[@class="df-fix__team-name"]/span')
    team1 = tt[0].text
    team2 = tt[1].text


    df1 = pd.read_csv(f'{dirname}/2023/linkplayers.csv')
    df2 = pd.read_csv(f'{dirname}/2023/player_points_info.csv')

    dft1 = pd.read_csv(f'{dirname}/2023/{team1}.csv')
    dft2 = pd.read_csv(f'{dirname}/2023/{team2}.csv')
    com_data = pd.merge(df1, df2, on=['player_name'])
    fin_data = pd.merge(com_data, dft1, on=['player_id'])
    fin_data = pd.merge(fin_data, dft2, on = ['player_id'])
    combined_data = pd.concat([dft1, dft2], ignore_index=True)
    fin_data = pd.merge(com_data, combined_data, on=['player_id'])
    fin_data = fin_data.sort_values('player_points', ascending=False)
    batter_final = fin_data.loc[(fin_data['player_role'] == "Batter") | (fin_data['player_role'] == "WK Keeper - Batter")].head(4)
    allrounder_final = fin_data.loc[(fin_data['player_role'] == "All-Rounder")].head(3)
    bowler_final = fin_data.loc[(fin_data['player_role'] == "Bowler")].head(4)
    final_squad = pd.concat([batter_final,allrounder_final,bowler_final], ignore_index=True)

    cvc= final_squad.sort_values('player_points', ascending=False,ignore_index=True)
    ctr=0
    for i in final_squad["player_name_x"]==cvc.at[0,"player_name_x"]:
        if(i):
            break
        ctr+=1
    final_squad.at[ctr,"player_name_x"]+=" (C)"
    ctr=0
    for i in final_squad["player_name_x"]==cvc.at[1,"player_name_x"]:
        if(i):
            break
        ctr+=1
    final_squad.at[ctr,"player_name_x"]+=" (VC)"

    l = list(dict.values(dict(final_squad["player_name_x"])))
    l.append(team1)
    l.append(team2)
    return l
    #print(l)

# predictXI()
