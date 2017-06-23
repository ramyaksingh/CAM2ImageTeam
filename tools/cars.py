import cv2

cars_cascade = cv2.CascadeClassifier("cars.xml")

img = cv2.imread("traffic11.png")
#gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cars = cars_cascade.detectMultiScale(img, scaleFactor = 1.02, minNeighbors = 2)
'''
for x, y, w, h in cars:
    img = cv2.rectangle(img, (x,y), (x + w, y + h), (0, 255, 0), 3)
'''
count = 0
i = 0
j = 0
red_boundaries = [10, 10, 90], [150, 150, 255]
print(red_boundaries[0][1])

for x, y, w, h in cars:
#    print("svhbsacjcdnjkdaknvkdavnkavnkn")

#    print(count)
    ver_count = x
    count = 0
    while(ver_count < x + h):


        hor_count = y

        while(hor_count < y + w):

            if (img[hor_count][ver_count][0] <= red_boundaries[1][0] and img[hor_count][ver_count][0] >= red_boundaries[0][0]
                 and img[hor_count][ver_count][1] >= red_boundaries[0][1] and img[hor_count][ver_count][1] <= red_boundaries[1][1]
                and img[hor_count][ver_count][2] <= red_boundaries[1][2] and img[hor_count][ver_count][2] >= red_boundaries[0][2]):
                    count = count + 1

            hor_count = hor_count + 1

        ver_count = ver_count + 1

    img = cv2.rectangle(img, (x,y), (x + w, y + h), (0, 255, 0), 3)
    print(float(count) / float(w * h))
    if(float(count) / float(w * h) > 0.5):
        img = cv2.rectangle(img, (x,y), (x + w, y + h), (0, 0, 255), 3)



cv2.imshow("Cars", img)
cv2.waitKey(0)
