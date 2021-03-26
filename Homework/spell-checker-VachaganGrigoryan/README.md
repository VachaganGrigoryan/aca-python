# Spell-checker
We will create spell-checker step by step.

Step 1. Writing utils for spell checker

1. In one file utils.py create function that will count two strings Levenshtein distance.

The Levenshtein distance between two strings a, b (of length |a| and |b| respectively) is given by leva,b(|a|,|b|) where:
![alt text](https://23o0161033pm1289qo1hzrwi-wpengine.netdna-ssl.com/wp-content/uploads/2017/01/Maths-768x162.jpg)

where 1(ai≠bi) is the indicator function equal to 0 when ai≠bi and equal to 1 otherwise, and leva, b(i,j) is the distance between the first i characters of a and the first j characters of b.

2. Create function in utils.py which calculate Soundex code for string:

Algorithm steps for Soundex code are:

- Copy the first character of the input string to the first character of the output string

- For subsequent characters in the input string, add digits to the output string according to the table below, up to a maximum of three digits (ie. a total output string length of 4). Note that a number of input letters are ignored, including all vowels. Also, further occurences of an input letter with the same encoding are ignored.

- If we reach the end of the input string before the output string reaches 4 characters, pad it to the right with zeros.

----Encoding Table----

Input letter	 Encoding <br />
A	------------ 0 <br />
B	------------ 1 <br />
C	------------ 2 <br />
D	------------ 3 <br />
E	------------ 0 <br />
F	------------ 1 <br />
G	------------ 2 <br />
H	------------ 0 <br />
I	------------ 0 <br />
J	------------ 2 <br />
K	------------ 2 <br />
L	------------ 4 <br />
M	------------ 5 <br />
N	------------ 5 <br />
O	------------ 0 <br />
P	------------ 1 <br />
Q	------------ 2 <br />
R	------------ 6 <br />
S	------------ 2 <br />
T	------------ 3 <br />
U	------------ 0 <br />
V	------------ 1 <br />
W	------------ 0 <br />
X	------------ 2 <br />
Y	------------ 0 <br />
Z	------------ 2 <br />

3. create main.py and use functions from utils.py

When you run your code this will be printed: <br />


Exp1: Choose from options: <br />
        1. Levenshtein <br />
        2. Soundex <br />
       Type 1 or 2: 1 <br />
       First string: kitten <br />
       Seccond string: sitting <br />
       Levenshtein distance for "kitten" and "sitting" is 3 <br />
       
       
Exp2: Choose from options: <br />
        1. Levenshtein <br />
        2. Soundex <br />
       Type 1 or 2: 2 <br />
       Input string: example <br />
       Soundex code for "example" is E251 <br />
       
       

Step 2. 

1. create file checker.py <br />
2. in the checker.py file write function that will map Soundex code to words of dictionary.txt file (find out best(fastest) way to implement mapping) <br />
3. in the checker.py file write function that get misspelled word, count Soundex code, get list of words that has the same Soundex code as misspelled word, count Levenstein distance between misspelled word and that list of words and return words that have minimal Levenstein distance with misspelled word. <br />
4. update main.py to work as follows: <br />

Exp.: Choose from options: <br />
        1. Levenshtein <br />
        2. Soundex <br />
        3. Spell correction <br />
      Type 1, 2 or 3: 3 <br />
      Write misspelled word: sprinq <br />
      Possible options: spring, sprint
 
