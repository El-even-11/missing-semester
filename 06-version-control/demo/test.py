import sys

def test():
    print('test!')

def default():
    print('hello world')

def main():
    if sys.argv[1] == 'test':
        test()
    else:
        default()

if __name__ == '__main__':
    main()

