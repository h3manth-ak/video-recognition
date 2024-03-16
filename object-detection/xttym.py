import cv2

class VideoTimestamp:
    def __init__(self, video_path):
        self.video_path = video_path
        self.cap = cv2.VideoCapture(video_path)
        self.fps = self.cap.get(cv2.CAP_PROP_FPS)

    def get_timestamp(self, frame_number):
        print(self.fps)
        timestamp = frame_number / self.fps
        return timestamp

    def release(self):
        self.cap.release()


# video = VideoTimestamp('path_to_your_video.mp4')
# frame_number = 10
# timestamp = video.get_timestamp(frame_number)
# video.release()
# print(f'The timestamp of frame {frame_number} is {timestamp} seconds.')