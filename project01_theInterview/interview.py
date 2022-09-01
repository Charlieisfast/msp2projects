print('this is the interview')
age = input("How old are You?")
school = input("what school did you go to?")
have_other_job = input("did you have any other jobs y or n?")
if have_other_job == 'y':
  
  Other_jobs = input("What other jobs did you have?")
  favorite_color = input("whats your favorite color?")
  college = input("What college did you go to?")
  print(f"Interview Report\n age: {age}\n School: {school}\n Other Jobs: {Other_jobs}\n College: {college}")
elif have_other_job == 'n':
  favorite_color = input("whats your favorite color?")
  college = input("What college did you go to?")
  print(f"Interview Report\n Age: {age}\n School: {school}\n Favorite Color: {favorite_color}\n College: {college}")
else:
  print("not y or n try again")