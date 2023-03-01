
# Problem Description
The problem "Decode String" requires us to decode an encoded string, where the encoding rule is:
k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

```java
public int i = 0;
    public String decodeString(String s) {

        if (s.length() == 0){
            return "";
        } else if (s.length() == 1){
            if (Character.isDigit(s.charAt(i)))
                return "";
            else
                return s;
        }

        String result = "";

        for ( ; i < s.length();){
            if (Character.isDigit(s.charAt(i))){
                String repeatedPart = repeater(s);
                result += repeatedPart;
            } else {
                result += s.charAt(i);
                i++;
            }
        }
        return result;
    }

    public String repeater (String s){

        String result = "";

        String iteration = "";
        while (Character.isDigit(s.charAt(i))){
            iteration += s.charAt(i);
            i++; // pass the number
        }

        int nIteration = 0;
        if (s.charAt(i) == '['){
            nIteration = Integer.parseInt(iteration);
        }

        i++; // passing '['
        String repeating = "";

        while (s.charAt(i) != ']'){
            if (Character.isDigit(s.charAt(i))){
                String insideIteration = repeater(s);
                repeating += insideIteration;
            } else {
                repeating += s.charAt(i);
                i++; // pass the character
            }
        }

        i++; //passing ']';

        for (int j = 0; j < nIteration; j++){
            result += repeating;
        }

        return result;
    }
```


# Solution
To solve the problem, we can use a recursive approach where we parse the input string character by character. We start at the beginning of the string, and if we encounter a digit, we know that the next substring is to be repeated. We use recursion to solve this problem.

We keep two pointers: i and j, where i is used to iterate through the input string, and j is used to iterate through the repeated string.

We have two functions:

decodeString - the main function that starts the recursion and returns the decoded string.
repeater - the function that repeats the substring.

## decodeString
The decodeString function checks the length of the input string. If the length of the string is zero or one, we return the input string.

If the length of the input string is greater than one, we initialize an empty string result.

We loop through the input string character by character, and if we encounter a digit, we call the repeater function. If we encounter a character, we add it to the result string and increment the i pointer.

Once the loop is complete, we return the result string.

## repeater
The repeater function is responsible for repeating the substring. We first parse the integer k from the input string by iterating through the string until we reach the [ character.

We then use recursion to repeat the substring k times. We keep track of the repeated string in the repeating variable. Once the recursion is complete, we repeat the substring k times and return the resulting string.

# Complexity Analysis

## Time complexity
The time complexity of this solution is O(n*m), where n is the length of the input string, and m is the maximum integer value in the input string.

## Space complexity
The space complexity of this solution is O(n*m), where n is the length of the input string, and m is the maximum integer value in the input string.

# Summary
The "Decode String" problem can be solved using a recursive approach. We first check the length of the input string and initialize an empty string. We then loop through the input string character by character and call the repeater function when we encounter a digit. The repeater function is responsible for repeating the substring. Once the recursion is complete, we repeat the substring k times and return the resulting string. The time complexity of this solution is O(n*m), and the space complexity is O(n*m).
