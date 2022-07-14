# 姓名：戴亮
# 开发时间：2022/6/30 18:06
# import cv2
#
# cap = cv2.VideoCapture(0)
#
#
# while True:
#     ret, img = cap.read()
#     cv2.imshow("frame", img)
#     key = cv2.waitKey(25)
#     print(key)
#     if key == 27:
#         break
# cap.release()
# cv2.destroyAllWindows()

import cv2

cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'XVID')

out = cv2.VideoWriter("recording.avi", fourcc, 30.0, (640, 480))

while cap.isOpened():
    ret, image = cap.read()
    if ret:
        out.write(image)
        cv2.imshow("recoding", image)
        cv2.waitKey(30)
    else:
        break
cap.release()
out.release()
cv2.destroyAllWindows()

