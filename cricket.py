#Creted by Pooja
#On 13 Oct 2020
# Dictionary implementation using python
def orangecap(d):
    data={}
    for v in d.items():
        for player_name, score in v.items():
            prev_player = player_name
            if prev_player == player_name:
                score = data.get(player_name,0) + score
                data[player_name] = score
    high_score_player = max(data, key=lambda i: data[i])
    return(high_score_player, data[high_score_player])
#orangecap({'match1':{'player1':57, 'player2':38}, 'match2':{'player3':9, 'player1':42}, 'match3':{'player2':41, 'player4':63, 'player3':91}})
b=orangecap({'test1':{'Ashwin':84, 'Kohli':120}, 'test2':{'Ashwin':59, 'Pujara':42}})
print(b)