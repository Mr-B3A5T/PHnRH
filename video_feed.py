import cv2

def loop_video():
    video_path = '/home/osboxes/Downloads/cctv.mp4'
    video_capture = cv2.VideoCapture(video_path)

    while True:
        ret, frame = video_capture.read()
        if ret:
            cv2.imshow('Fake CCTV video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    loop_video()
