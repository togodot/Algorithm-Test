### 5635번: 생일

# 문제
# 어떤 반에 있는 학생들의 생일이 주어졌을 때, 가장 나이가 적은 사람과 가장 많은 사람을 구하는 프로그램을 작성하시오.
# 
# 입력
# 첫째 줄에 반에 있는 학생의 수 n이 주어진다. (1 ≤ n ≤ 100)
# 
# 다음 n개 줄에는 각 학생의 이름과 생일이 "이름 dd mm yyyy"와 같은 형식으로 주어진다. 이름은 그 학생의 이름이며, 최대 15글자로 이루어져 있다. dd mm yyyy는 생일 일, 월, 연도이다. (1990 ≤ yyyy ≤ 2010, 1 ≤ mm ≤ 12, 1 ≤ dd ≤ 31) 주어지는 생일은 올바른 날짜이며, 연, 월 일은 0으로 시작하지 않는다.
# 
# 이름이 같거나, 생일이 같은 사람은 없다.
# 
# 출력
# 첫째 줄에 가장 나이가 적은 사람의 이름, 둘째 줄에 가장 나이가 많은 사람 이름을 출력한다.

n = int(input())
max_year = 1989
max_month = 0
max_day = 0
min_year = 1991
min_month = 2
min_day = 2

for i in range(n):
    name, dd, mm, yyyy = map(str, input().split())
    
    if int(yyyy) > max_year:
        max_year = int(yyyy)
        max_month = int(mm)
        max_day = int(dd)
        youngest = name
    elif int(yyyy) == max_year:
        if int(mm) > max_month:
            max_month = int(mm)
            max_day = int(dd)
            youngest = name
        elif int(mm) == max_month:
            if int(dd) > max_day:
                max_day = int(dd)
                youngest = name
                
    if int(yyyy) < min_year:
        min_year = int(yyyy)
        min_month = int(mm)
        min_day = int(dd)
        oldest = name
    elif int(yyyy) == min_year:
        if int(mm) < min_month:
            min_month = int(mm)
            min_day = int(dd)
            oldest = name
        elif int(mm) == min_month:
            if int(dd) < min_day:
                min_day = int(dd)
                oldest = name
                
print(youngest)
print(oldest)
