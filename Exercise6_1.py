def croud_test(lst):
    if len(lst) > 3:
        print('The room is too crowded!')

names = ['John', 'Janice', 'Jace', 'Jill']
croud_test(names)
names.pop()
names.pop()
croud_test(names)