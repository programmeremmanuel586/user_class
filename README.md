# Create a User class

### The backbone of social media

Almost any social media platform will rely on objects - they allow the program to run in the ways we humans think about the program. 

In this lab, you'll build the class that could support the creation of new users on a social media site. By the end of the lab, you'll have built a user that has an email on file, that can update their status based on their mood, and that can even change their password - if they know the current one!

### Structure of the lab

This lab runs in two files.

The `user_class.py` file is where you will *define* your user class. The `users.py` file is where you will *create individual users* (initialize individual instances of the class) and then call methods on those users in order to see whether your class is functioning correctly.

## Two ways to run this lab:

#### Run the pre-written tests

To run the pre-written tests, open both files in your text editor, and uncomment one line of code at a time in the `users.py` file.

After you uncomment each line of test code, run the program in the console by typing `python users.py` and see what errors you get. Build out and modify the class definition in the user_class.py file until the code runs successfully. Then move on to the next line.

#### Write your own tests

If you'd rather write your own tests, feel absolutely free. You'll want to code your tests at the end of the user_class.py file, and then test each one by running that program with the command `python user_class.py`

Here's what you ought to be able to do with your user class:

1. Initialize new instances of the user class, starting each user with at least a name, an email, a password, and an age. Think about what information Facebook asks for when you create an account:

<img src="images/signup.png" width="200" height="300"/>

2. Create a default argument for age, so that a user can still create an account even if they don't wish to share their age. (The minimum age for most social media sites is 13).
3. Write a method called `status_update` that prints out how the user is feeling, based on their mood.
4. Write a method called `change_password` that takes two arguments - the old password and the new password. It should change the user's password ONLY if the attempt at the old password matches the existing password for that user. If the old password doesn't match, it should print out an error. Think about how you might change your password on Facebook:

<img src="images/changepassword.png" width="400" height="200"/>
