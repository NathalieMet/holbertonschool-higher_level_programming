#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4

string = dir(hidden_4)
filtered = sorted([name for name in string if not name.startwith("__")])
for name in filtered:
    print(name)
