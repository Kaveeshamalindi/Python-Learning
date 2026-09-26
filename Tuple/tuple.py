#--------------------------------------------------------------------

fullname = ('Grace', 'M', 'Hopper')
print(type(fullname))                   #<class 'tuple'>

Fullname = ['Grace', 'M', 'Hopper']
print(type(Fullname))                   #<class 'list'>

#---------------------------------------------------------------------------------------------

def convert_seconds(seconds):
  hours = seconds // 3600
  minutes = (seconds - hours * 3600) // 60
  remaining_seconds = seconds - hours * 3600 - minutes * 60
  return hours, minutes, remaining_seconds
result = convert_seconds(5000)

print(type(result))
print(result)

#---------------------- unpack -------------------------------

hours, minute, seconds = result
print(hours, minute, seconds)

hours, minute, seconds = convert_seconds(1000)
print(hours, minute, seconds)


