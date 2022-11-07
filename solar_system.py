import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(img,  
           "Sun",
           (120, 100),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX,
           fontScale=1,  
           color=(0,0,255)
           )

cv2.putText(img,  
"Mercury",
(110, 180),  
fontFace=cv2.FONT_HERSHEY_COMPLEX,
fontScale=0.5,  
color=(200,200,200)
)

cv2.putText(img,  
"Venus",
(190, 170),  
fontFace=cv2.FONT_HERSHEY_COMPLEX,
fontScale=0.5,  
color=(200,200,200)
)

cv2.putText(img,  
"Earth",
(280, 170),  
fontFace=cv2.FONT_HERSHEY_COMPLEX,
fontScale=0.5,  
color=(200,200,200)
)

cv2.putText(img,  
"Mars",
(380, 170),  
fontFace=cv2.FONT_HERSHEY_COMPLEX,
fontScale=0.5,  
color=(200,200,200)
)

cv2.putText(img,  
"Jupiter",
(580, 50),  
fontFace=cv2.FONT_HERSHEY_COMPLEX,
fontScale=0.5,  
color=(200,200,200)
)

cv2.putText(img,  
"Saturn",
(780, 120),  
fontFace=cv2.FONT_HERSHEY_COMPLEX,
fontScale=0.5,  
color=(200,200,200)
)

cv2.putText(img,  
"Uranus",
(960, 130),  
fontFace=cv2.FONT_HERSHEY_COMPLEX,
fontScale=0.5,  
color=(200,200,200)
)

cv2.putText(img,  
"Neptune",
(1100, 130),  
fontFace=cv2.FONT_HERSHEY_COMPLEX,
fontScale=0.5,  
color=(200,200,200)
)

cv2.imshow("output" , img)

cv2.waitKey(0)
