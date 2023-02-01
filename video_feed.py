import cv2

def loop_video(video_path):
    video = cv2.VideoCapture(video_path)

    while True:
        ret, frame = video.read()

        if not ret:
            video = cv2.VideoCapture(video_path)
            continue

        cv2.imshow("Fake CCTV Video Stream", frame)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    video_path = '/home/osboxes/Downloads/cctv.mp4'
    loop_video(video_path)
