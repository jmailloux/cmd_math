import random
from time import time

def get_ans(num1:int, num2:int, op:int) -> int:
  '''Prompts user to enter the answer to a question.
     Returns user inputted answer as int
  '''
  ans = None
  while(ans is None):
    try:
      if(op == 0):
        ans = int(input(f'What is {num1} * {num2}? ' ))
      else:
        dividend = num1 * num2
        ans = int(input(f'What is {dividend} / {num1}? ' ))
    except ValueError:
      print("Please enter a number!")
  return ans

def main():
  total = 0
  num_correct = 0
  duration = 0

  random.seed()
  while(duration < 10):
    correct = False
    num1 = random.randint(1, 10)
    num2 = random.randint(0, 10)
    op = random.randint(0,1)
    user_ans = get_ans(num1, num2, op)
    total += 1
    if total == 1:
      start = time()
    if(op == 0):
      if(user_ans == num1 * num2):
        num_correct += 1
        correct = True
    else:
      if(user_ans == num2):
        num_correct += 1
        correct = True
    if not correct:
      print('Wrong!!!!!\n')
    percent = num_correct * 100 / total
    now = time()
    duration = (now-start)/60
    print(f'{duration:.2f} min: {num_correct}/{total}, {percent:.1f}%')


if __name__ == "__main__":
    try:
      main()
    except KeyboardInterrupt:
       pass