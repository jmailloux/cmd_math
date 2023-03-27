import random
from time import time

def get_ans(num1:int, num2:int) -> int:
  '''Prompts user to enter the answer for num1 * num 2.  Returns user inputted answer as int
  '''
  ans = None
  while(ans is None):
    try:
      ans = int(input(f'What is {num1} * {num2}? ' ))
    except ValueError:
       print("Please enter a number!")
  return ans

def main():

  total = 0
  correct = 0
  duration = 0
  random.seed()
  while(duration < 10):
    num1 = random.randint(0, 10)
    num2 = random.randint(0, 10)
    user_ans = get_ans(num1, num2)
    total += 1
    if total == 1:
      start = time()
    if(user_ans == num1 * num2):
        correct += 1
    else:
       print('Wrong!!!!!\n')
    percent = correct * 100 / total
    now = time()
    duration = (now-start)/60
    print(f'{duration:.2f} min: {correct}/{total}, {percent:.1f}%')


if __name__ == "__main__":
    try:
      main()
    except KeyboardInterrupt:
       pass