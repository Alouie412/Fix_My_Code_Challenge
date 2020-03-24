# Fix My Code Challenge

Because debugging is hard, and that the majority of bugs in programs are the result of typos or questionable inconsistencies. This repository explores code given and determine why the result does not match the intended logic.

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
|[1-print_square.js](https://github.com/Alouie412/Fix_My_Code_Challenge/blob/master/1-print_square.js) | Using Javascript, take a user input and form a square of # | The error is incorrect conversion. While parseInt is correctly used to convert a string to integer (the user's input is read as a string, which is why parseInt is necessary), the conversion itself is not. The original author converted the string to hexadecimal rather than a decimal, thus why a value like 10 prints out a square of size 16 |
|[2-sort.rb](_link here_) | _Description here_ | _Error here_ |
|[3-user.py](https://github.com/Alouie412/Fix_My_Code_Challenge/blob/master/3-user.py) | Using Python, determine if the password given is a valid password. An empty password or consists only of integers are invalid | This program actually has two errors; the biggest issue is actually finding them because the entire logic is solid. The first error is a simple typo: self.\_password instead of self.\_\password (self.\_password is never used in this program). The second error is comparing hash values. While this is acceptable, the issue is the original author's bizarre choice to compare a hash value in lowercase... to the same hash value in uppercase. |
