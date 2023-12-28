import cv2

cam = cv2.VideoCapture(0)
cv2.namedWindow("Test")
img_counter = 0

# Set the desired directory path here
save_path = "C:/Users/DELL/Desktop/Python/Capture Images/"

while True:
    ret, frame = cam.read()
    if not ret:
        print("Failed to grab frame")
        break
    cv2.imshow("test", frame)

    k = cv2.waitKey(1)
    if k % 256 == 27:
        print("Closing...")
        break
    if k % 256 == 32:
        img_name = "{}OpenCV{}.png".format(save_path, img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1

cam.release()
cv2.destroyAllWindows()
