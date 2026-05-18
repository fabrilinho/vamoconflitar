import math
import sys

def eh_primo(num):
    for i in range(2,num//2):
        if num % i ==0:
            return False
    return True

if __name__ == "__main__":
    num1 = int(sys.argv[1])
    print(eh_primo(num1))
