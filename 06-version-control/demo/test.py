import sys

def test():
    print('test!')

def default():
    print('hello world')

def bugfix():
    print('bug fixed!')

def main():
    if sys.argv[1] == 'test':
        test()
    elif sys.argv[1] == 'bugfix':
        bugfix()
    else:
        default()

if __name__ == '__main__':
    main()

