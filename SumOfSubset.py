def check(set, r):
    p = tuple(set)
    n = len(p)
    if r > n:
        return
    subset = list(range(r))
    yield tuple(p[i] for i in subset)
    while True:
        for i in reversed(range(r)):
            if subset[i] != i + n - r:
                break
        else:
            return
        subset[i] += 1
        for j in range(i+1, r):
            subset[j] = subset[j-1] + 1
        yield tuple(p[i] for i in subset)


def SumOfSubset(size, set, t):

   for i in range(size+1):
      for subset in check(set, i):

         if sum(subset) == t:
            print(list(subset))


set = [5, 10, 12, 13, 15, 18]
s = len(set)
print("The list is :")
print(set)
t = int(input('Enter the sum: '))
print("The all possible subsets are :")
SumOfSubset(s, set, t)
