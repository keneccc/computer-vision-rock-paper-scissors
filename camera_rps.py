# %% 
import cv2
import time 
from keras.models import load_model
import numpy as np
model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
import random 
rps_list=["rock", "paper","scissors"]
computer_input= random.choice(rps_list)
countdown= 20
computer_lives=3
player_lives=3

def get_prediction(): #Function to open camera and determine user game input of rock,paper or scissors 
    global countdown
    while countdown > 0: 
        countdown = countdown-1
        ret , frame = cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32)/127.0) - 1 # Normalize the image
        data[0] = normalized_image
        global prediction
        prediction = model.predict(data)
        cv2.imshow('frame', frame)
        # Press q to close the window
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        if prediction[0][0]> 0.7:
            prediction="rock"
        elif prediction[0][1]> 0.7:
            prediction="scissors"
        elif prediction[0][2]>0.7:
            prediction="paper"
        elif prediction[0][3]>0.7:
            prediction="nothing"
        print("You chose", prediction)
                        
    # After the loop release the cap object
    cap.release()
    # Destroy all the windows
    cv2.destroyAllWindows()
    return prediction
        
def play():  # fucntion to play game 
    
    def get_computer_choice(): # function to determine computer selection
        computer_input
        print(computer_input)

    def get_winner():   # function to determine winner 
        global player_lives
        global computer_lives
        get_computer_choice()
        get_prediction()
        if prediction== computer_input:
            print("Tie")
        elif prediction== "rock" and computer_input=="scissors": # determine if prediction is "ROCK"
            print("Winner!")
            computer_lives= computer_lives-1
        elif prediction == "scissors" and computer_input=="paper": # determine if prediction is "Scissors"
            print("Winner!")
            computer_lives= computer_lives-1
        elif prediction == "paper" and computer_input=="rock": # determine if prediction is "Paper "
            print("Winner!")
            computer_lives=computer_lives-1
        else:
            print("LOSER")
            player_lives=player_lives-1
    

    get_winner()

    if player_lives>0 and computer_lives>0:
        play()
        print(player_lives)
    elif player_lives == 0:
        exit()
    
        

    
                           
play()

# %%
