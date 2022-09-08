# F = m*a
import math
va = ["F = m*a","A = h*b/2","a^2 + b^2 = c^2 "]
for i in va:
  pick = input(f"would you like to solve the formula {i}, y or n ")
  if pick.lower() == 'y' or pick.lower() == 'yes':
    function = i
    break
    
solveing_for = []
variable_pick = input("what Variable would you like to solve for?")
if   i == va[0]:
  variables = ["F","m","a"]
elif i == va[1]:
  variables = ["A",'h','b']
elif i == va[2]:
  variables = ['a','b','c']
  
  
for i in variables:
  if variable_pick == i:
    variables.remove(i)
    solveing_for.append(i)



input1 = input(f"What should {variables[0]} equal?")
input2 = input(f"What should {variables[1]} equal?")

if va[0] == function:
  if solveing_for[0] == 'F':
    Final = int(input1)*int(input2)
  elif solveing_for[0] == "m":
    Final = int(input1) / int(input2)
  elif solveing_for[0] == "a":
    Final = int(input1) / int(input2)
elif va[1] == function:
  if solveing_for[0] == 'A':
    Final = int(input1)*int(input2)/2
  elif solveing_for[0] == "b":
    Final = int(input1)*2 / int(input2)
  elif solveing_for[0] == "h":
    Final = int(input1)*2 / int(input2)
elif va[2] == function:
  if solveing_for[0] == 'a':
    Final = math.sqrt(int(input2)**2 - int(input1)**2)
  elif solveing_for[0] == "b":
    Final = math.sqrt(int(input2)**2 - int(input1)**2)
  elif solveing_for[0] == "c":
    Final = math.sqrt(int(input1)**2 + int(input2)**2)
print(f"Awnser: {Final}")