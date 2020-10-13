# write your code here
class Calculator:
    def __init__(self):
        self.menu()

    def menu(self):
        while True:
            nums = input().split()

            if not nums:
                continue
            if len(nums) >= 2:
                self.addition(nums)  # pass list of numbers
            elif len(nums) == 1:
                if nums[0] == '/exit':
                    print('Bye!')
                    quit()
                elif nums[0] == '/help':
                    print('The program calculates the sum of numbers')
                print(nums[0])

    @staticmethod
    def addition(*args):
        num_sum = sum([int(num) for num in args[0]])
        print(num_sum)
        # return sum


if __name__ == '__main__':
    calculator = Calculator()
