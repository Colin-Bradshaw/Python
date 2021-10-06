def croud_test(lst):
    if len(lst) > 3:
        print('The room is too crowded!')
    else:
        print('There is still space in this room')

names = ['John', 'Janice', 'Jace', 'Jill']
croud_test(names)
names.pop()
names.pop()
croud_test(names)