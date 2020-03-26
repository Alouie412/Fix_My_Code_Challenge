# Fix My Code Challenge

Because debugging is hard, and that the majority of bugs in programs are the result of typos or questionable inconsistencies. This repository explores code given and determine why the result does not match the intended logic. The original code remains intact; the error lines are commented out and replaced with the correct line.

## Description:

* Take code written by someone
* Debug code and explore logic
* Fix code to get correct logic
* Return functional code
* Repeat steps 1 to 5 until done
* ~~Convince HR to fire the incompetent programmer~~

# Files in This Repository
| File Name | Description | Error |
| --- | --- | --- |
|[0-fizzbuzz.py](https://github.com/Alouie412/Fix_My_Code_Challenge/blob/master/0-fizzbuzz.py) | A classic fizzbuzz code using Python that prints Fizz, Buzz, or FizzBuzz depending on the number and certain rules. | The error is simple: the original author forgot that order matters. The original code checked if i % 3 is equal to 0 BEFORE checking if i % 3 and i % 5 is equal to 0. Because the computer reads lines one by one from the top and the entire code is written in one if/else statement, every multiple of 15 will always satisfy the i % 3 condition, and will never run the i % 3 and i % 5 condition |
|[1-print_square.js](https://github.com/Alouie412/Fix_My_Code_Challenge/blob/master/1-print_square.js) | Using Javascript, take a user input and form a square of # | The error is incorrect conversion. While parseInt is correctly used to convert a string to integer (the user's input is read as a string, which is why parseInt is necessary), the conversion itself is not. The original author converted the string to hexadecimal rather than a decimal, thus why a value like 10 incorrectly prints out a square of size 16 but a value like 4 correctly prints out a square of size 4|
|[2-sort.rb](_link here_) | _Description here_ | _Error here_ |
|[3-user.py](https://github.com/Alouie412/Fix_My_Code_Challenge/blob/master/3-user.py) | Using Python, determine if the password given is a valid password. An empty password or consists only of integers are invalid | This program actually has two errors; the biggest issue is actually finding them because the entire logic is solid. The first error is a simple typo: self.\_password instead of self.\_\password (self.\_password is never used in this program). The second error is comparing hash values. While this is acceptable, the issue is the original author's bizarre choice to compare a hash value in lowercase... to the same hash value in uppercase. |
|[4-delete_dnodeint](https://github.com/Alouie412/Fix_My_Code_Challenge/tree/master/4-delete_dnodeint) | Using C, create a doubly linked list, then delete a node at a specific index | This entire directory contains all the C files needed for the doubly linked list task. Each file will be given its own entry |
|[add_dnodeint_end.c](https://github.com/Alouie412/Fix_My_Code_Challenge/blob/master/4-delete_dnodeint/add_dnodeint_end.c) | Create a node and add it to the end of the linked list | No errors found. This file is correct |
|[delete_dnodeint_at_index.c](https://github.com/Alouie412/Fix_My_Code_Challenge/blob/master/4-delete_dnodeint/delete_dnodeint_at_index.c) | Delete a node at the given index. Return 1 if deletion is successful, otherwise -1 | The error was the original author's... odd choice of repairing links at the target node. For whatever reason, the original author chose to set the target node's prev prev... to itself. This results in the original target node, while freed correctly, was not actually removed from the linked list, because the target node's prev's next still points to the target node and not the target node's next. Had the original author attempt to print this linked list in reverse, they will find that their odd linkage would result in an infinite loop. Also originally thought order matters and the free command must come after setting the link on both sides, but the original order is actually acceptable |
|[free_dlistint.c](https://github.com/Alouie412/Fix_My_Code_Challenge/blob/master/4-delete_dnodeint/free_dlistint.c) | Frees the entire linked list | No errors found. This file is correct |
|[lists.h](https://github.com/Alouie412/Fix_My_Code_Challenge/blob/master/4-delete_dnodeint/lists.h) | Header file for the linked list task | No errors found. This file is correct |
|[main.c](https://github.com/Alouie412/Fix_My_Code_Challenge/blob/master/4-delete_dnodeint/main.c) | The driver function. Creates, prints, deletes, and ultimately purges the linked list | No errors found. This file is correct |
|[print_dlistint.c](https://github.com/Alouie412/Fix_My_Code_Challenge/blob/master/4-delete_dnodeint/print_dlistint.c) | Accesses the node of and prints the integers in the linked list | No errors found. This file is correct |
