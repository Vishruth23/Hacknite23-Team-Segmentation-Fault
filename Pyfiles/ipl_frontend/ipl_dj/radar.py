import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
import base64

def bat_graph(bat_st, player):
    labels_bat=["runs","avg","sr","fours","sixes"]
    runs_scored_norm = (bat_st[0]) / (bat_st[5])
    strike_rate_norm = (bat_st[1]) / (bat_st[6])
    fours_hit_norm = (bat_st[2]) / (bat_st[7])
    sixes_hit_norm = (bat_st[3]) / (bat_st[8])
    average_norm = (bat_st[4]) / (bat_st[9])
    data = [runs_scored_norm, strike_rate_norm, fours_hit_norm, sixes_hit_norm, average_norm]
    angles = np.linspace(0, 2*np.pi, len(labels_bat), endpoint=False)
    fig = plt.figure(figsize=(4, 4))
    ax = fig.add_subplot(111, polar=True)
    ax.plot(angles, data, 'o-', linewidth=2)
    ax.fill(angles, data, alpha=0.25)
    ax.set_thetagrids(angles * 180/np.pi, labels_bat)
    ax.set_ylim(0, max(data) * 1.1)
    plt.title(player)
    plt.legend(['player'], loc='upper right')
    #zplt.show()
    buffer=BytesIO()
    plt.savefig(buffer,format="png")
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
    return image_base64

def bowl_graph(bowl_st, player):
    labels_bowl=["wickets","avg","sr","econ"]
    wickets_norm = (bowl_st[0]) / (bowl_st[4])
    sr_norm = (bowl_st[5] - bowl_st[1]) / (bowl_st[5])
    econ_norm = (bowl_st[6] - bowl_st[2]) / (bowl_st[6])
    avg_norm = (bowl_st[7] - bowl_st[3]) / (bowl_st[7])
    data = [wickets_norm, avg_norm, sr_norm, econ_norm]
    angles = np.linspace(0, 2*np.pi, len(labels_bowl), endpoint=False)
    fig = plt.figure(figsize=(4, 4))
    ax = fig.add_subplot(111, polar=True)
    ax.plot(angles, data, 'o-', linewidth=2)
    ax.fill(angles, data, alpha=0.25)
    ax.set_thetagrids(angles * 180/np.pi, labels_bowl)
    ax.set_ylim(0, max(data) * 1.1)
    plt.title(player)
    plt.legend(['player'], loc='upper right')
    #plt.show()
    buffer=BytesIO()
    plt.savefig(buffer,format="png")
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
    return image_base64