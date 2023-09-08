
import sys

x = [int(a) for a in sys.stdin.read().split()]

if len(sys.argv) < 2:
    print("Incorrect number of arguments.", file=sys.stderr)
    sys.exit(1)

def print_list(x):
    print(" ".join(str(i) for i in x))


x = [1, 2, 3, 4, 5, 6]

a = sum(x)
print(a)
l = len(x)
print(l)
mean = (a/l)
print(mean)

times_three = []
for i in x:
    i *= 3
    print(i)
    times_three.append(i)
print_list(times_three)

even = []
for n in x:
    if n % 2 == 0:
        even.append(n)
print_list(even)


