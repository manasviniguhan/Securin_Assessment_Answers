Part-A (15-20 Minutes): 

1. How many total combinations are possible? Show the math along with the code!

Explanation:
•	First, The value of each face of Die A is stored in a list.
•	Second, The value of each face of Die B is stored in another list. 
•	One die has 6 possible outcomes. So, if two dice are rolled then we need to multiply 6 two times which will result in 36. The total number of outcomes in a simultaneous throw of two dice will be 36.

2. Calculate and display the distribution of all possible combinations that can be obtained when rolling both Die A and Die B together. Show the math along with the code! 
Hint: A 6 x 6 Matrix.

Explanation:
•	First, The value of each face of Die A is stored in a list.
•	Second, The value of each face of Die B is stored in another list. 
•	Value of each face of Die A is iterated with the Value of each face of Die B.
•	At last, Distribution of all possible combinations are printed in 6 x 6 matrix format.

3. Calculate the Probability of all Possible Sums occurring among the number of combinations from (2). Example: P(Sum = 2) = 1/X as there is only one combination possible to obtain 
Sum = 2. Die A = Die B = 1

Explanation:
•	First, The value of each face of Die A is stored in a list.
•	Second, The value of each face of Die B is stored in another list. 
•	Each pair is taken from the total possible outcomes. The pair is stored as key and sum of pair is stored as value of the dictionary "sum_of_combinations"
•	A for loop is iterated with a range of 2 to 12 since the minimum possible sum is 2 and maximum possible sum is 12
•	For each iteration, The values of dictionary "sum_of_combinations" are checked whether it is equal to the iterator value. If equal then the counter variable "c" is incremented and divided by "x" and printed as the probability of all possible sums.

Part-B (25-30 Minutes): 

Question:
Now comes the real challenge. You were happily spending a lazy afternoon playing your board game with your dice when suddenly the mischievous Norse God Loki (You love Thor too much & Loki didn’t like that much) appeared. Loki dooms your dice for his fun removing all the “Spots” off the dice.

No problem! You have the tools to re-attach the “Spots” back on the Dice. 
However, Loki has doomed your dice with the following conditions: 
● Die A cannot have more than 4 Spots on a face. 
● Die A may have multiple faces with the same number of spots.
● Die B can have as many spots on a face as necessary i.e. even more than 6. 
But in order to play your game, the probability of obtaining the Sums must remain the same!
So if you could only roll P(Sum = 2) = 1/X, the new dice must have the spots reattached such that those probabilities are not changed. 

Input: 
● Die_A = [1, 2, 3, 4, 5, 6] & Die B = Die_A = [1, 2, 3, 4, 5, 6]
Output: 
● A Transform Function undoom_dice that takes (Die_A, Die_B) as input & outputs New_Die_A = [?, ?, ?, ?, ?, ?],New_Die_B = [?, ?, ?, ?, ?, ?] where,
● No New_Die A[x] > 4

Explanation:
•	A list 1,2,3,4 is taken as "initial_elements" since No New_Die A[x] > 4. For the rest 2 elements the combinations library is used to find the possible extra elements in range of 1 to 4 and they are combined with the “initial_elements” to form the possible combinations for New_Die A. The combinations are stored in list "all_possible_die_A".
•	For New_Die B, The combinations library is used to find the possible combinations in range of 1 to 8 since the maximum number of spots the New_Die A can have is 4 and the maximum possible sum is 12. The combinations are stored in list "all_possible_die_B".
•	To find the undoomed die A and B from the combinations, Two lists are taken, one from "all_possible_die_A" and another one from "all_possible_die_B". They are passed to the "calculate_sum_probabilities" function to calculate all possible sums and are stored in "sum_probabilities".
•	The "sum_probabilities" is passed to the "prob_distribution_matches" function to check whether the "sum_probabilities" of the pair of combinations is equal to the original "sum_probabilities" of the undoomed dice. If equal then they are the New_Die A and New_Die B. Else, Other combinations are checked till the New_Die A and New_Die B are found.

