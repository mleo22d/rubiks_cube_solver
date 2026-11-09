import cv2
import kociemba
import numpy as np



cap = cv2.VideoCapture(1)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,920)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,920)

final_str = ''
rows = 6
cols = 9
colorTOT = [['' for j in range(cols)] for i in range(rows)]
#colorTOT = []
list2 = [0,1,2,3,4,5]

for j, element in enumerate(list2):
    
    while True:

        dim = 150


        _, frame = cap.read()
        hsv_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        height, width, _ = frame.shape
        list2 = [0,1,2,3,4,5]
        
        
        cx = int (width/2)
        cy = int (height/2)
        

        cx1 = cx-100
        cy1 = cy-100

        cx2 = cx
        cy2 = cy-100

        cx3 = cx+100
        cy3 = cy-100

        cx4 = cx-100
        cy4 = cy

        cx5 = cx
        cy5 = cy

        cx6 = cx+100
        cy6 = cy

        cx7 = cx-100
        cy7 = cy+100

        cx8 = cx
        cy8 = cy+100

        cx9 = cx+100
        cy9 = cy+100

        #Pick pixel value

        #hue value
        pixel_center1 = hsv_frame[cy1,cx1]
        hue_value1 = pixel_center1[0]

        pixel_center2 = hsv_frame[cy2,cx2]
        hue_value2 = pixel_center2[0]

        pixel_center3 = hsv_frame[cy3,cx3]
        hue_value3 = pixel_center3[0]

        pixel_center4 = hsv_frame[cy4,cx4]
        hue_value4 = pixel_center4[0]

        pixel_center5 = hsv_frame[cy5,cx5]
        hue_value5 = pixel_center5[0]

        pixel_center6 = hsv_frame[cy6,cx6]
        hue_value6 = pixel_center6[0]

        pixel_center7 = hsv_frame[cy7,cx7]
        hue_value7 = pixel_center7[0]

        pixel_center8 = hsv_frame[cy8,cx8]
        hue_value8 = pixel_center8[0]

        pixel_center9 = hsv_frame[cy9,cx9]
        hue_value9 = pixel_center9[0]

        hue_value = [hue_value1, hue_value2, hue_value3, hue_value4, hue_value5, hue_value6, hue_value7, hue_value8, hue_value9]


        #Saturation value set
        pixel_center1 = hsv_frame[cy1,cx1]
        sat_value1 = pixel_center1[1]

        pixel_center2 = hsv_frame[cy2,cx2]
        sat_value2 = pixel_center2[1]

        pixel_center3 = hsv_frame[cy3,cx3]
        sat_value3 = pixel_center3[1]

        pixel_center4 = hsv_frame[cy4,cx4]
        sat_value4 = pixel_center4[1]

        pixel_center5 = hsv_frame[cy5,cx5]
        sat_value5 = pixel_center5[1]

        pixel_center6 = hsv_frame[cy6,cx6]
        sat_value6 = pixel_center6[1]

        pixel_center7 = hsv_frame[cy7,cx7]
        sat_value7 = pixel_center7[1]

        pixel_center8 = hsv_frame[cy8,cx8]
        sat_value8 = pixel_center8[1]

        pixel_center9 = hsv_frame[cy9,cx9]
        sat_value9 = pixel_center9[1]
        sat_value = [sat_value1,sat_value2,sat_value3,sat_value4,sat_value5,sat_value6,sat_value7,sat_value8,sat_value9]


        list1 = [0,1,2,3,4,5,6,7,8]
        color = ["N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A"]
        caras = ["Escanear Cara Superior", "Escanear Cara Derecha", "Escanear Cara Frontal", "Escanear cara Inferior", "Escanear cara izquierda", "Escanear cara Trasera"]

        for i, element in enumerate(list1):
            
            if hue_value[i] <= 7:
                color[i]= "RED"
            elif hue_value[i] <=20:
                color[i] = "ORANGE"
            elif hue_value[i] <= 40:
                color[i] = "YELLOW"
            elif hue_value[i] <= 95:
                color[i] = "GREEN"
            elif hue_value[i] <= 145:
                color[i] = "BLUE"
            elif hue_value[i] <= 170:
                color[i] = "Cargando..."
            else:
                color[i] = "RED"

            if sat_value[i] <=65:
                color[i] = "WHITE"


        


        #print(pixel_center1);
        if j == 0:
            cv2.putText(frame,caras[j],(cx-300,cy-200),5,2,(255,0,0))
        elif j == 1:
            cv2.putText(frame,caras[j],(cx-300,cy-200),5,2,(0,0,255))
        elif j == 2:
            cv2.putText(frame,caras[j],(cx-300,cy-200),5,2,(255,255,255))
        elif j == 3:
            cv2.putText(frame,caras[j],(cx-300,cy-200),5,2,(0,255,0))
        elif j == 4:
            cv2.putText(frame,caras[j],(cx-300,cy-200),5,2,(0,165,255))
        else:
            cv2.putText(frame,caras[j],(cx-300,cy-200),5,2,(0,255,255))

        
        cv2.putText(frame,color[0],(cx-300,cy-66),1,3,(255,255,255))
        cv2.putText(frame,color[3],(cx-300,cy),1,3,(255,255,255))
        cv2.putText(frame,color[6],(cx-300,cy+66),1,3,(255,255,255))
        cv2.putText(frame,color[2],(cx+155,cy-66),1,3,(255,255,255))
        cv2.putText(frame,color[5],(cx+155,cy),1,3,(255,255,255))
        cv2.putText(frame,color[8],(cx+155,cy+66),1,3,(255,255,255))
        cv2.putText(frame,color[1],(cx-50,cy-154),1,3,(255,255,255))
        cv2.putText(frame,color[4],(cx+130,cy-154),1,3,(255,255,255))
        cv2.putText(frame,color[7],(cx-50,cy+200),1,3,(255,255,255))


        cv2.circle(frame, (cx1,cy1),5,(255,0,0),3)
        cv2.circle(frame, (cx2,cy2),5,(255,0,0),3)
        cv2.circle(frame, (cx3,cy3),5,(255,0,0),3)
        cv2.circle(frame, (cx4,cy4),5,(255,0,0),3)
        cv2.circle(frame, (cx5,cy5),5,(255,0,0),3)
        cv2.circle(frame, (cx6,cy6),5,(255,0,0),3)
        cv2.circle(frame, (cx7,cy7),5,(255,0,0),3)
        cv2.circle(frame, (cx8,cy8),5,(255,0,0),3)
        cv2.circle(frame, (cx9,cy9),5,(255,0,0),3)
        cv2.rectangle(frame, (cx-150,cy-150),(cx+150,cy+150),(255,0,0),3)
        cv2.imshow("Frame",frame)



        key = cv2.waitKey(1)
        if key == 27:
            print("Siguiente Cara")
            colorTOT[j] = color
            

            break
    
solution = np.concatenate((colorTOT[0],colorTOT[1],colorTOT[2],colorTOT[3],colorTOT[4],colorTOT[5]), axis=None)


 
for val in range(len(solution)):
    if solution[val] == "WHITE": #front
        final_str = final_str + 'F'
    elif solution[val] == "RED": #right
        final_str = final_str + 'R'
    elif solution[val] == "YELLOW": #back
        final_str = final_str + 'B'
    elif solution[val] == "ORANGE": #left
        final_str = final_str + 'L'
    elif solution[val] == "BLUE": #Up
        final_str = final_str + 'U'
    elif solution[val] == "GREEN": # down
        final_str = final_str + 'D'


solved = kociemba.solve(final_str)
print(solved)


cap.release()
cv2.destroyAllWindows()