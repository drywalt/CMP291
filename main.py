#enter 5 scores in the range of 0 to 10
#validate each score
#find the highest and lowest
#repeat code for multiple sets of scores and add a counter
#use Y or y in condition
counter = 0
answer = 'y'
overallaverage = 0 
finalaverage = 0
while answer == 'y' or answer == 'Y':
  total = 0
  highest = 0  #start with the lowest and go up
  lowest = 10  #start with the highest and go down
  for s in range(5):
    score = float(input("Enter the score"))
    while score < 0 or score > 10:
      print "Invalid Score. Try again!"
      score = float(input("Enter the score"))
    if score > highest:
      highest = score
    if score < lowest:
      lowest = score
    #accumulate total
    total += score
  #calculate average
  average = (total - highest - lowest)/3
  overallaverage += average #accumulates
  print average
  counter = counter + 1
  answer = input("Do you have another entry?")
finalaverage = overallaverage/counter
print 'There were ', counter, 'entries'
print finalaverage
  