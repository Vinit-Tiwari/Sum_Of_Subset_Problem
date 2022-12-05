***DAA Assignment***

***Sum of Subset Problem***

**Problem Statement:**
Implement: Sum of the Subset problem using the Backtracking approach and demonstrate any two applications in the form of test cases.


**Approach:**
Following steps are performed in order to find all the subsets which have the sum equal to the number entered by user:
Step 1: Take a number input from user, initialise the set array and 'n' equal to length of set.
Step 2: Create functions named 'SumOfSubset' and 'check'. 'check' function will take set and size of subset as input and return all the possible check. Then 'SumOfSubset' function will compare the sum of subset return from 'check' function with the number entered by user.
Step 3: If the sum of subset is equal the number then subset is printed. This process will continue till all check are compared.


**Solved Example:**
set = [5, 10, 12, 13, 15, 18]
input = 30

Here, the control will pass to the sub_set_sem function, this function will run the for loop to get all possible combinations and if the sum of this subset mastches the input, the list will be printed. Similarly all combinations are checked.


**Code**
```
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
```

**Test Case-1**
When the solution in present:

**Output**

![image](https://user-images.githubusercontent.com/95700013/205544372-e391f065-9b1a-4e7f-bdae-2d4c502cb0bf.png)

**Test Case-2**
When the there is no solution

**Output**
![image](https://user-images.githubusercontent.com/95700013/205544837-f02a5e03-19e7-4332-aa6b-66a223917c17.png)
