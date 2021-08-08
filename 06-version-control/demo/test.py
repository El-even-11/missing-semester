import sys

def default():
    print('hello world')

def bugfix():
    print('bug fixed!')

def main():
    if sys.argv[1] == 'bugfix':
        bugfix()
    else:
        default()

if __name__ == '__main__':
    main()

