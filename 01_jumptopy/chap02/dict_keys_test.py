# coding: cp949
#-*- coding: utf-8 -*-
#big_data_players={"�迬��":"���ѽ�������","������":"�߱�","������":"�౸"}
korean_str="�ѱ�"
print(korean_str)
big_data_players={"Yeona Kim":"Figuer Skating","Ryu":"Baseball","Park":"Soccer"}
print("Step1] Printing the raw type of dictionary,'big_data_players'")
print(big_data_players)

print("\nStep2] Printing the key lists using big_data_players.keys() function")
print(big_data_players.keys())

print("\nStep3] printing the value lists using big_data_players.values() function")
print(big_data_players.values())

print("\nStep4] Trying to search character of 'Ryu' in the big_data_players dictionary")

for player_key in big_data_players.keys():
    print(player_key)
    if player_key == "Ryu":
        print("\nI Found Ryu")
        print(big_data_players["Ryu"])
        break

print("Program End")
