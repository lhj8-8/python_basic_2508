#closuer2.py

class Mul:
    def __init__(self, m):
        self.m = m


    def mul(self, n):
        return self.m * n


if __name__ == "__main__":
    mul3 = Mul(3)
    mul5 = Mul(5)


    print(mul3.mul(10))  # 30 출력
    print(mul5.mul(10))  # 50 출력
