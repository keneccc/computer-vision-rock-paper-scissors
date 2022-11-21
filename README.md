# Computer Vision RPS
Milestone 2 
Created 4 classes using teachable machine: Nothing, Rock, Paper and Scissors. 
Exported and saved the model to be utilsed later.
Copied code to open webcam using opencv library 

Milestone 3
Set up a new enviorment 
installed all necessary libraries including opencv-python, tensorflow and ipykernel in the new enviroment 


Milestone 4 
imported random
Defined function "get_user-choice" which asks the user for an input and returns the value
Defined function "get_computer_choice" which selects 1 item at random from a list containing rock, paper and scissors
Defined "get_winner" function which runs previous 2 functions and then wrote a set of if,elif, else statements to code the logic of the game and determine if the input is valid 


Milestone 5
Defined the function get_prediction which returns the prediction of the model after converting the numpy array based on the results of the prrediction to rock,paper,scissors or nothing 
imported time and used time.sleep to delay code for 5 seconds every iteration 
edited get_winner function to determine the number of lives for the computer and player after each round 

defined play function which calls on other previous functions in order to run the game looping automatically until number of lives for either the player or computer is 0

Potential: 
Adding timer counter to the webcam display but might require some editing based on time.sleep function being used for current version of code 
Add sound to alert play it is time to play or the game is over 
Instead of timer could ask user to continue playing using an appropiately placed input function as well as some if and elif statements 


