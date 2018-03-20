# coding: cp949

name = "이유덕,이재영,권종표,이재영,박민호,강상희,이재영,김지완,최승혁,이성연,박영서,박민호,전경헌,송정환,김재성,이유덕,전경헌"

print("1. 김 : ",name.count('김'), "이 : ", name.count('이'))
print('2. "이재영"이란 이름이 몇 번 반복되나요? : ', name.count('이재영'))
result =name.split(',')
aSet=set(result)
remove=list(aSet)
print("3. 중복을 제거한 이름을 출력하세요 : ", remove)
remove.sort()
print("4. 오름차순으로 정렬하여 출력하세요 : ", remove)
