for i in range(1, 101):
  if i%3==0 and i%5==0:
    printCommon()
  elif i%3==0:
    printThird()
  elif i%5==0:
    printFifth()
  else:
    print(i)