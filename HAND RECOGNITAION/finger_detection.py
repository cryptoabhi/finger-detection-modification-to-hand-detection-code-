# This code is to detect the finger pointed. Modification in hand detection code
# cryptoabhi
# if any suggetion , contact me on +919168039929
import cv2
import mediapipe as mp


#for capturing video and increase size
cap = cv2.VideoCapture(0)
cap.set(3, 1280)# increase size of o/p screen
cap.set(4, 720)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

#hands detection

while True:
    
    success, image = cap.read()
    imageRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(imageRGB)
    
    thickness=2
#   checking whether a hand is detected   
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks: # working with each hand
            for id, lm in enumerate(handLms.landmark): #The second for loop helps us get the hand landmark information which will give us the x and y coordinates of each listed point in the hand landmark diagram. This loop will also give us the id of each point.
                h, w, c = image.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
           
                #getting 'y 'co-ordinates of each finger tip 
                if id == 4:
                    thumb = []
                    thumb.append(cy)
                    T=thumb[-1]
                    

                if id == 8:
                    index = []
                    index.append(cy)
                    I=index[-1]

                if id == 12:
                    middle = []
                    middle.append(cy)
                    M=middle[-1]

                if id == 16:
                    Ring = []
                    Ring.append(cy)
                    R=Ring[-1]

                if id == 20:
                    baby = []
                    baby.append(cy)
                    B=baby[-1]
                    
                # recognizing the pointed up finger and printing the initials of pointed finger    
                    if T<M and T<I and T<R and T<B:
                        
                        cv2.putText(image, 'T', (100,100),5, fontScale= 5 ,color=(1,0,0),thickness=5,lineType=cv2.FONT_HERSHEY_COMPLEX)
                    
                    if I<M and I<T and I<R and I<B:
                        
                        cv2.putText(image, 'I', (100,100),5, fontScale= 5 ,color=(1,0,0),thickness=5,lineType=cv2.FONT_HERSHEY_COMPLEX)
                    
                    if M<T and M<I and M<R and M<B:
                        
                        cv2.putText(image, 'M', (100,100),5, fontScale= 5 ,color=(1,0,0),thickness=5,lineType=cv2.FONT_HERSHEY_COMPLEX)
                    
                    if R<M and R<I and R<T and R<B:
                        
                        cv2.putText(image, 'R', (100,100),5, fontScale= 5 ,color=(1,0,0),thickness=5,lineType=cv2.FONT_HERSHEY_COMPLEX)
                    
                    if B<M and B<I and B<R and B<T:
                        
                        cv2.putText(image, 'B', (100,100),5, fontScale= 5 ,color=(1,0,0),thickness=5,lineType=cv2.FONT_HERSHEY_COMPLEX)
                
                    

            mpDraw.draw_landmarks(image, handLms, mpHands.HAND_CONNECTIONS)
#displaying output
    cv2.imshow("Output", image)
    if cv2.waitKey(1) == ord(' '):
        cv2.imwrite('detected finger.jpg', image)

        cap.release()
        exit()
