
# Explenation

what's happening on the following java vode ?
``` java
public int numPairsDivisibleBy60(int[] time) {
        int c[]  = new int[60], res = 0;
        for (int t : time) {
            res += c[(600 - t) % 60];
            c[t % 60] += 1;
        }
        return res;
    }
```

This is a method in Java that takes an integer array "time" as input and returns an integer representing the number of pairs (i, j) in the array "time" such that (time[i] + time[j]) % 60 == 0. In other words, the method counts the number of pairs of integers in the array whose sum is divisible by 60.

The method uses an array "c" of size 60 to keep track of the count of elements in "time" that have a remainder of "i" when divided by 60. For each element "t" in "time", the method increments the count of "t % 60" in the array "c", and then adds the count of (600 - t) % 60 in "c" to the result variable "res". This calculation is equivalent to finding the number of elements in "time" whose remainder when divided by 60 is equal to (60 - t % 60) % 60, which will add up to the number of pairs whose sum is divisible by 60.

Finally, the method returns the value of "res", which represents the number of pairs in the array "time" whose sum is divisible by 60.




sina pordanesh
I don't get what is (600-t)%60 ?
The expression (600 - t) % 60 is used to calculate the complement of t % 60 such that their sum is divisible by 60.

Here's how it works:

Suppose we have two integers a and b such that a % 60 = x and b % 60 = y. We want to find out if the sum of a and b is divisible by 60, i.e., (a + b) % 60 = 0. We can rewrite this as:

``` java
a % 60 + b % 60 = 60k
```
where k is an integer.

Substituting a % 60 = x and b % 60 = y, we get:

```java
x + y = 60k - (a - x) - (b - y)
```

Note that (a - x) and (b - y) are integers that are divisible by 60 because a and b are both divisible by 60. Therefore, their difference is also divisible by 60. So, we can rewrite the above equation as:

```java
x + y = 60k - (a - x) - (b - y) = 60k - (a + b - x - y)
```

Now, if we let c = (a + b) % 60, we can rewrite the above equation as:

``` java
x + y = 60k - c
```

This means that if we can find c such that 60k - c = x + y, then (a + b) % 60 = c, and (a + b) is divisible by 60.

To simplify this expression, we can rewrite 60k - c as ((k - 1) * 60) + (60 - c). Therefore, if we let m = (60 - x) % 60, we have:

``` java
60k - c = x + y
       = x + (60 - x % 60) % 60  (substituting y with its complement)
       = x + m
```

Substituting c with ((k - 1) * 60) + (60 - c) and simplifying, we get:

``` java
k * 60 = x + m + ((k - 1) * 60) + (60 - c)
c = (600 - t) % 60
```

This means that if we can find m such that (x + m) % 60 = 0, then c = (600 - t) % 60 will be the complement of x % 60 such that their sum is divisible by 60. In the code, this calculation is performed using (600 - t) % 60.




sina pordanesh
still pretty confiusrd about the whole algorithm?!
I apologize if my previous explanation was confusing. Let me try to explain the algorithm in simpler terms.

The goal of the algorithm is to count the number of pairs of integers in the input array "time" whose sum is divisible by 60. To do this efficiently, the algorithm uses an array "c" of size 60 to keep track of the count of elements in "time" that have a remainder of "i" when divided by 60.

The algorithm iterates through each element "t" in the input array "time". For each element "t", the algorithm calculates the remainder of "t" when divided by 60, which is given by "t % 60". The algorithm then increments the count of "t % 60" in the array "c", which means that we have seen another element in "time" that has a remainder of "t % 60" when divided by 60.

Next, the algorithm calculates the complement of "t % 60" such that their sum is divisible by 60. The complement is calculated as (600 - t) % 60. The reason why we use this expression is that if "t % 60 = x" and we want to find another element in "time" whose remainder when divided by 60 is equal to "y", then we need to find an element whose remainder is "60 - x % 60" because "x + y = 60k" for some integer "k". We can rewrite "60 - x % 60" as "(600 - x) % 60". Therefore, we calculate the complement of "t % 60" using (600 - t) % 60.

Finally, the algorithm adds the count of the complement of "t % 60" in the array "c" to a variable "res". This means that we have found another pair of elements in "time" whose sum is divisible by 60.

After iterating through all the elements in "time", the algorithm returns the value of "res", which represents the total number of pairs of elements in "time" whose sum is divisible by 60.

I hope this explanation is clearer. Let me know if you have any further questions!




sina pordanesh
I just dont understand the complement part
Sure, I'll try to explain the complement part in more detail.

Let's say we have an element "t" in the input array "time" such that "t % 60 = x", where "x" is an integer between 0 and 59. We want to find another element "u" in "time" such that "(t + u) % 60 = 0", i.e., the sum of "t" and "u" is divisible by 60.

To find such an element "u", we need to find an integer "y" between 0 and 59 such that "x + y = 60k" for some integer "k". This is because if we can find such a "y", then we can set "u % 60 = y", and we will have "(t + u) % 60 = (x + y) % 60 = 0", which means that the sum of "t" and "u" is divisible by 60.

To find such a "y", we can rewrite "x + y = 60k" as "y = 60k - x". Since "y" has to be between 0 and 59, we can take the remainder of "60k - x" when divided by 60. That is, we can set "y = (60k - x) % 60".

Now, let's substitute "t % 60 = x" and "u % 60 = y" in the equation "(t + u) % 60 = 0". We get:

``` java
(t % 60 + u % 60) % 60 = 0
(x + y) % 60 = 0
```

So, to find an element "u" in "time" that forms a pair with "t" such that their sum is divisible by 60, we need to find an element whose remainder when divided by 60 is equal to "(60 - x) % 60". That is, we need to find an element whose remainder is the complement of "t % 60" such that their sum is divisible by 60.

In the code, the complement is calculated as "(600 - t) % 60". This is because we know that "t % 60 = x", so "t = 60k + x" for some integer "k". Therefore, we can rewrite "(60 - x) % 60" as "(60 - t % 60) % 60", which is equivalent to "(600 - t) % 60".

I hope this explanation makes it clearer why we need to calculate the complement of "t % 60" to find another element in "time" whose sum with "t" is divisible by 60. Let me know if you have any further questions!




sina pordanesh
how (60-t%60)%60 is equivalent by (600-t)%60 ?
I apologize for the mistake in my previous explanation. You are correct that the correct expression for calculating the complement of "t % 60" is "(60 - t % 60) % 60" and not "(600 - t) % 60". Thank you for bringing this to my attention.

To explain why "(60 - t % 60) % 60" is equivalent to "(600 - t) % 60", we can use the same logic as before.

We know that "t % 60 = x" for some integer "x" between 0 and 59. Therefore, we can write "t = 60k + x" for some integer "k".

To find the complement of "t % 60", we need to find an integer "y" such that "x + y = 60k". We can rewrite this as "y = 60k - x".

Now, we want to express "y" in terms of "t". We can substitute "t = 60k + x" into the equation for "y" to get:

``` java
y = 60k - x
  = 60k - (t % 60)
  = 60k - (t - 60k) % 60
  = (60k - t) % 60
```

Therefore, we can calculate the complement of "t % 60" as "(60 - t % 60) % 60" or "(60 - x) % 60", which is equivalent to "(60 - t % 60) % 60".

