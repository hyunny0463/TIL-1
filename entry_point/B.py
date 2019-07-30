import A

print('top-levl B.py')
A.func()

if __name__ == '__main__':
    print('B.py가 직접 실행')
else:
    print('B.py가 import 되어 실행')