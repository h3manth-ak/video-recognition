import cv2
import os
import matplotlib.pyplot as plt
class VideoFrameExtractor:
    def __init__(self, video_path):
        self.video_path = video_path
        self.frames = self._extract_frames()

    def _extract_frames(self):
        frames = []
        # Open the video file
        cap = cv2.VideoCapture(self.video_path)

        # Check if the video file opened successfully
        if not cap.isOpened():
            raise FileNotFoundError(f"Could not open video file: {self.video_path}")

        # Iterate through each frame and extract it
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            # Convert the frame to RGB (OpenCV uses BGR by default)
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frames.append(frame_rgb)

        # Release the video capture object
        cap.release()

        return frames

    def get_frames(self):
        return self.frames

    def display_frame(self, frame_index):
        if 0 <= frame_index < len(self.frames):
            plt.imshow(self.frames[frame_index])
            plt.axis('off')
            plt.show()
        else:
            print(f"Invalid frame index: {frame_index}")

# Example usage:
# Replace 'path_to_your_video.mp4' with the actual path to your video file
# video_path = 'C:/Users/USER/Desktop/main-project/dataset/program/sample.mp4'
# frame_extractor = VideoFrameExtractor(video_path)

# Get all frames
# all_frames = frame_extractor.get_frames()

# Display the first frame
# frame_extractor.display_frame(45)
