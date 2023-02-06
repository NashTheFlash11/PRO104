import cv2

WHITE = 255, 255, 255

img = cv2.imread('Images/solar-system.jpg')
sun = cv2.putText(img,
                "Sun",
                (60,300),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (WHITE))
mercury = cv2.putText(img,
            "Mercury",
            (100,250),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (WHITE))
venus = cv2.putText(img,
            "Venus",
            (180,250),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (WHITE))
earth = cv2.putText(img,
            "Earth",
            (280,250),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (WHITE))
mars = cv2.putText(img,
            "Mars",
            (360,250),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (WHITE))
jupiter = cv2.putText(img,
            "Jupiter",
            (570,370),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (WHITE))
saturn = cv2.putText(img,
            "Saturn",
            (750,300),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (WHITE))
uranus = cv2.putText(img,
            "Uranus",
            (970,300),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (WHITE))
neptune = cv2.putText(img,
            "Neptune",
            (1100,300),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (WHITE))
cv2.imshow("Solar System", img)
cv2.waitKey(0)

