def combinations(set, r):
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
        
def sub_set_sum(size, my_array, sub_set_sum):

   for i in range(size+1):
      for my_sub_set in combinations(my_array, i):

         if sum(my_sub_set) == sub_set_sum:
            print(list(my_sub_set))

set = [5, 10, 12, 13, 15, 18]
s = len(set)
print("The list is :")
print(set)
t = int(input('Enter the sum: '))
print("The all possible subsets are :")
sub_set_sum(s, set, t)