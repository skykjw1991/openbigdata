# coding: cp949
soccer_players={"�����":"��Ʈ��","����":"����Ǯ","�޽�":"�ٸ����γ�","ȣ����":"���˸��帮��","���":"����ư","�׸��":"��Ʋ��Ƽ�ڸ��帮��","ÿ��":"Ĳ��","�Ʊ�����":"�ǽ�Ƽ","���׹�":"��ü����������Ƽ��","����":"�ƽ���"}

print("step1] ������ �� ��� ���") 
print(soccer_players)

print("\nstep2] key (����) ���")
print(soccer_players.keys())

print("\nstep3] value (��) ���")
print(soccer_players.values())

print("\nstep4] ����� �ִ��� �˻�")

if '�����' in soccer_players:
    for player_key in soccer_players.keys():
        print(player_key)
        if player_key == '�����':
            print("\n������� ã�Ҵ�")
            break

print("\n���α׷� ����")




