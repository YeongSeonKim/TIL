# 문제 : bit.do/yeoksam_python_33
# 강사님 코드 : bit.do/yeoksam_answer

'''
Python dictionary 연습 문제
'''

# 1. 평균을 구하시오.
score = {
    '수학': 80,
    '국어': 90,
    '음악': 100
}

# 아래에 코드를 작성해 주세요.
print('==== Q1 ====')
# 풀이

# for ench_score in score.values():
#     # print(ench_score) # => 80,90,100
print(sum(score.values()))
print(sum(score.values()) / len(score))



# 2. 반 평균을 구하시오. -> 전체 평균
scores = {
    '민승': {
        '수학': 80,
        '국어': 90,
        '음악': 100
    },
    '건희': {
        '수학': 80,
        '국어': 90,
        '음악': 100
    }
}

# 아래에 코드를 작성해 주세요.
print('==== Q2 ====')
print(scores.keys())
print(scores.values())
a = scores.get('민승')
print(a.values())
print(sum(a.values()))

# 풀이
total_score = 0
length = 0

for person_score in scores.values(): # scores.values() -> value 요소 리스트
		# person_score -> {'수학':80, '국어':90, '음악':100} 과 같이 다시 딕셔너리
    # length += len(person_score)
    for subject_score in person_score.values():
        total_score += subject_score
				# subject_score -> 80 -> 90 -> 100 -> 80 -> 90 -> 100
        length += 1
average_score = total_score / length # 540 / 6
print(average_score)


# 3. 도시별 최근 3일의 온도입니다.
cities = {
    '서울': [-6, -10, 5],
    '대전': [-3, -5, 2],
    '광주': [0, -2, 10],
    '부산': [2, -2, 9],
}

# 3-1. 도시별 최근 3일의 온도 평균은?

# 아래에 코드를 작성해 주세요.
print('==== Q3-1 ====')
'''
출력 예시)
서울 : 평균온도
대전 : 평균온도
광주 : 평균온도
부산 : 평균온도
'''
# 풀이
for name, temp in cities.items():
    # 첫번째 시행
    # name = "서울"
    # temp = [-6, -10, 5]
    average_temp = sum(temp) / len(temp)
    print(f"{name} : {average_temp}")

# 3-2. 도시 중에 최근 3일 중에 가장 추웠던 곳, 가장 더웠던 곳은?

# 아래에 코드를 작성해 주세요.
print('==== Q3-2 ====')
# 풀이
cold = 0
hot = 0
count = 0
hot_city = ""
cold_city = ""

for name, temp in cities.items():
    # 첫 번째 시행
    # name = "서울"
    # temp = [-6, -10, 5]
    if count == 0: # 첫번째 시행을 위한 처리 
        hot = max(temp)
        cold = min(temp)
        hot_city = name
        cold_city = name
    else:
        # 최저 온도가 cold보다 더 추우면, cold에 넣고
        if min(temp) < cold:
            cold = min(temp)
            cold_city = name
        # 최고 온도가 hot보다 더 더우면, hot에 넣고
        if max(temp) > hot:
            hot = max(temp)
            hot_city = name
    count += 1

print(hot_city)
print(cold_city)


# 3-3. 위에서 서울은 영상 2도였던 적이 있나요?

# 아래에 코드를 작성해 주세요.
print('==== Q3-3 ====')
# 풀이
# 1) 약식
2 in cities["서울"]


# 2) 확장
if 2 in cities["서울"]:
    print("네! 있어요")
else:
    print("없어요!")