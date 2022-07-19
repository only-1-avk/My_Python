#Write your code below this row 👇


for i in range(1,101):
  if i % 3 == 0 and i % 5 == 0:  #if we put line 7 and line 9 condition before this it will skip other condition so we have first checked this conditio
    print("Fizz")
  elif i % 3 == 0:
    print("Buzz")
  elif i % 5 == 0:
    print("FizzBuzz")
  else:
    print(i)
