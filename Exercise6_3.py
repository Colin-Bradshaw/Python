def croud_test(lst):
    if len(lst) > 5:
        print('There is a mob in here!')
    elif len(lst) > 3:
        print('The room is too crowded!')
    elif len(lst) > 0:
        print('There is still space in this room.')
    else:
        print('This room is empty.')

names = ['John', 'Janice', 'Jace', 'Jill', 'Jack', 'Jane']
croud_test(names)
names.pop()
names.pop()
croud_test(names)
names.pop()
names.pop()
croud_test(names)
names.pop()
names.pop()
croud_test(names)