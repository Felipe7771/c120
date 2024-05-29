import cv2
import time
import math
#Atividade 1
#declare p1 e p2
p1 = 330
p2 = 550

xs = []
ys = []

video = cv2.VideoCapture("footvolleyball.mp4")
#Carregue o rastreador
tracker = cv2.TrackerCSRT_create()

#Leia o primeiro quadro do vídeo
success,img = video.read()

#Selecione a caixa delimitadora na imagem
bbox = cv2.selectROI("tracking",img,False)

#Inicialize o rastreador em img e na caixa delimitadora
tracker.init(img,bbox)

def goal_track(img,bbox):
    x,y,w,h = int(bbox[0]),int(bbox[1]),int(bbox[2]),int(bbox[3])
    c1 = x + int(w/2)
    c2 = y + int(h/2)

    #Atividade 2
    #Descomente o código correto 
    cv2.circle(img,(c1,c2),2,(0,0,255),5)
    #cv2.circle(img,(c2,c1),2,(0,5,255),0)
    #cv2.circle(img,(c2,c1),2,(0,0,255),5)
    #cv2.circle(img,(c1,c2),2,(0,5,255),0)

    cv2.circle(img,(int(p1),int(p2)),2,(0,255,0),3)
    dist = math.sqrt(((c1-p1)**2) + (c2-p2)**2)
    print(dist)

    if(dist<=20):
        cv2.putText(img,"Ponto",(300,90),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,0),2)

    xs.append(c1)
    ys.append(c2)

    for i in range(len(xs)-1):
        cv2.circle(img,(xs[i],ys[i]),2,(0,0,255),5)

def drawBox(img,bbox):
    x,y,w,h = int(bbox[0]),int(bbox[1]),int(bbox[2]),int(bbox[3])
    cv2.rectangle(img,(x,y),((x+w),(y+h)),(255,0,255),3,1)
    cv2.putText(img,"Rastreando",(75,90),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,0),2)


while True:
    check,img = video.read()   
    success,bbox = tracker.update(img)

    if success:
        drawBox(img,bbox)
    else:
        cv2.putText(img,"Errou",(75,90),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)

    #Atividade 3
    #chame a função para rastrear a bola
    goal_track(img,bbox)

    cv2.imshow("resultado",img)
            
    key = cv2.waitKey(1)
    if key == ord('q'):
        print("Fechando")
        break

video.release()
cv2.destroyALLwindows() 