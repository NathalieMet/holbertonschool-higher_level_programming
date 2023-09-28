#!/usr/bin/python3

if __name__ == "__main__":
    import sys

result = 0
argc = len(sys.argv)

for i in range(1, argc):
    result += int(sys.argv[i])
print(result)
