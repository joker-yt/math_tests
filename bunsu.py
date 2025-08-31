import random
from fractions import Fraction

def generate_problem():
    # 分子と分母をランダムに生成
    num1, den1 = random.randint(1, 10), random.randint(2, 10)
    num2, den2 = random.randint(1, 10), random.randint(2, 10)

    # 分数を生成
    frac1 = Fraction(num1, den1)
    frac2 = Fraction(num2, den2)

    # 足し算または引き算をランダムに選択
    operation = random.choice(['+', '-'])

    # 問題と答えを計算
    if operation == '+':
        result = frac1 + frac2
        problem = f'{frac1} + {frac2}'
    else:
        result = frac1 - frac2
        problem = f'{frac1} - {frac2}'

    return problem, result

# 問題を10問生成して表示
ansers = []
for _ in range(10):
    problem, result = generate_problem()
    print(f'問題: {problem} = ?')
    ansers.append((problem, result))


input('Are you ready for the answers? Press Enter to see the answers...')
for i in range(10):
    print(f'問題: {ansers[i][0]} = {ansers[i][1]}')
