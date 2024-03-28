import time

from baseball import helloworld

def main():
    hw = helloworld.HelloWorld()
    print(f'Hello world @ {now()}')

def now():
    return time.strftime("%Y-%m-%d %H:%M:%S")
    
if __name__ == '__main__':
    main()
