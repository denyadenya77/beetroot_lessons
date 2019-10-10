text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam mattis ex tellus, vulputate facilisis odio cursus vitae. Suspendisse sed euismod dolor. Aenean orci ex, posuere at pharetra sit amet, fringilla sed diam. Proin condimentum bibendum facilisis. Nullam fringilla bibendum metus, eu vehicula libero pharetra in. Nullam rhoncus ut eros commodo lacinia. Integer et tincidunt lectus, non suscipit felis. Sed orci risus, condimentum nec accumsan elementum, porta at purus. Integer finibus porta varius. Cras sodales mauris sit amet faucibus placerat. Nulla convallis magna quam, eu tincidunt justo vehicula et. Vivamus at fringilla odio, id elementum turpis. Suspendisse lobortis felis sapien. '
a = text.find('sed')
print(a)

b = text[0:10]
print(b)

c = text[-26:]
print(c)

one_more_string = 'Do you like summer? - Yes'
print(one_more_string.replace('Yes', 'No'))

hw = '    Hello world!    '
front = hw.lstrip()
back = front.rstrip()
print(back)

task_14 = 'gOOD nIghT EVEryoNE!'
print(task_14.swapcase())

yes = 'yes'
no = 'no'
print(no * 2 + yes * 3)

Abracadabra = 'Abracadabra'
print(str(Abracadabra.count('a')))