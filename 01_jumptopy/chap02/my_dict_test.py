# coding: cp949
soccer_players={"손흥민":"토트넘","마네":"리버풀","메시":"바르셀로나","호날두":"레알마드리드","루니":"에버튼","그리즈만":"아틀레티코마드리드","첼시":"캉테","아구에로":"맨시티","포그바":"맨체스터유나이티드","외질":"아스날"}

print("step1] 선수와 팀 모두 출력") 
print(soccer_players)

print("\nstep2] key (선수) 출력")
print(soccer_players.keys())

print("\nstep3] value (팀) 출력")
print(soccer_players.values())

print("\nstep4] 손흥민 있는지 검색")

if '손흥민' in soccer_players:
    for player_key in soccer_players.keys():
        print(player_key)
        if player_key == '손흥민':
            print("\n손흥민을 찾았다")
            break

print("\n프로그램 종료")




