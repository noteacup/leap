def is_leap(x):
    if x % 4 != 0:
        return False
    elif x % 100 != 0:
        return True
    elif x % 400 != 0:
        return False
    elif x % 3200 != 0:
        return True

x = input('請輸入年份: ')
x = int(x)
result = is_leap(x)
if result == True:
    print('閏年')
else:
    print('平年')
