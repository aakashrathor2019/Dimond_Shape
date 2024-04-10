# TechAlpha_Task2
In task2 create the dimanod  shpae with 2n rows 
1)We define a function print_diamond(n) that takes the parameter n, which represents the number of rows in the diamond.
2)The first for loop is responsible for printing the upper part of the diamond. It iterates from 1 to n (inclusive) and for each iteration, it prints spaces (' ') based on the current row number (n - i) and then prints asterisks ('*') based on the formula 2 * i - 1.
3)The second for loop prints the lower part of the diamond. It iterates from n - 1 down to 1 (exclusive) using a step size of -1. Similar to the upper part, it prints spaces and asterisks.
4)Finally, in the main program, we prompt the user to enter the number of rows for the diamond (n) and call the print_diamond() function with the user input.
