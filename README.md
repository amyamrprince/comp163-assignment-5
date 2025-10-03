# comp163-assignment-5
# Python Loops — Challenges 1–3 explaniation

## Why I chose each loop type
-Challenge 1 (Collatz): I used a while loop because we don’t know how many steps until n becomes 1.
-Challenge 2 (Prime Check): I used a for loop because the divisors are a known range (2, n-1) and used "break" to stop the loop once the conditon became ture. Else was used to print “prime” if no divisor found.
-Challenge 3 (Multiplication Table): I used nested for loops because the outer loop controls the rows, and the inner loop controls the columns for each row. Both of those let me fill in the multiplication table like a grid.

## How my solutions work 
-challenge 1- I made a container(a list) to store each number because my output kept printing 1 insteaed of 7 as the "Starting number". So in order for me to get the right input i had to store each number in a sequence. I used .append() to add the current number into the list everytime the loop runs. So you start with a number that is not equal to one. If the number is even you divied it by 2 and if it is odd you divied by 3 and add 1. This repeats until the number becomes one because in that case the conditon would become false ending the loop.    

- Challenge 2- If the number is less than or equal to 1 (n<= 1) its not prime. If its greater than one the loop checks for each number between 2 and n-1. If any number divides evenly, the input is not prime(divisble by 3). If the divisor is not found the input is prime.
   
- challenge 3- First for loop prints numbers 1-10 across the top (header). The second loop prints numbers 1-10 down the side. On the inside (row x column) is calculated to fill the table. In order to keep spacing we must add (:4). Resulting in a 10x10 multiplication chart. 

## How to run
Challenge 1- enter a number when prompted to.
Challenge 2- enter a positive number when promted 
challenge 3- click the run button 
