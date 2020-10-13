# write your code here
class Calculator:

    def addition(self):
        a, b = input().split(" ")
        print(int(a) + int(b))


if __name__ == '__main__':
    calculator = Calculator()
    calculator.addition()
