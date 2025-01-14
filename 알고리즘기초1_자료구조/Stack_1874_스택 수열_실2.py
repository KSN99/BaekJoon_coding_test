# 1~n까지의 수를 스택에 넣었다가 뽑아 늘어놓음으로써, 하나의 수열을 만들 수 있다.
# 이때, 스택에 push 하는 순서는 반드시 오름차순을 지키도록 한다고 하자.
# 임의의 수열이 주어졌을 때 스택을 이용해 그 수열을 만들 수 있는지 없는지,
# 있다면 어떤 순서로 push와 pop 연산을 수행해야 하는지를 알아낼 수 있다. 이를 계산하는 프로그램 작성
# 입력: 첫 줄에 n이 주어지고, 둘째 줄부터 n개의 줄에는 수열을 이루는 1이상 n이하의 정수가 하나씩 순서대로 주어진다.
# 물론 같은 정수가 두 번 나오는 일은 없다.

# 입력된 수열을 만들기 위해 필요한 연산을 한 줄에 한 개씩 출력
# push 연산은 +, pop 연산은 -로 표현, 불가능한 경우 NO를 출력
"""
8줄
1234 ++++
[4,3] --
1256 ++
[4,3,6] -
12578 ++
[4,3,6,8,7,5,2,1] -----
"""

n = int(input())
stack = []
cnt = 1
answer = []
flag = 0
for i in range(n):
    stack_num = int(input())
    while cnt <= stack_num:
        stack.append(cnt)
        answer.append('+')
        cnt += 1
    if stack[-1] == stack_num:
        stack.pop()
        answer.append('-')

    else:
        print("NO")
        flag = 1
        break

if flag == 0:
    for i in answer:
        print(i)

#다시 풀기
n = int(input())
stack = []
answer = []
flag = 0
cur = 1
for i in range(n):
    num = int(input())
    while cur <= num:       # 입력한 수를 만날 때 까지 오름차순으로 push
        stack.append(cur)
        answer.append("+")
        cur += 1
    # 입력한 수를 만나면 while문 탈출. 즉 cur = num일 때 까지 while문을 돌아 스택을 쌓는다.

    if stack[-1] == num:    # stack의 TOP이 입력한 숫자와 같다면
        stack.pop()         # 스택의 TOP을 꺼내 수열을 만들어 준다.
        answer.append("-")
    else:                   # stack의 TOP이 입력한 수가 아니면 주어진 스택을 만들 수 없다.
        print("NO")         # 왜냐하면 12345 처럼 오름차순으로 스택이 입력되는데
        flag = 1            # TOP이 num보다 크면 num은 TOP보다 더 아래에 쌓여있기 때문이다.
        break

if flag == 0:
    for i in answer:
        print(i)