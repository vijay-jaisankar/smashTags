"""
    @note This file contains helper functions used to assist in the Video to hashtags task
    List of functionalities
        - Generate (almost) unique filenames
        - Extract audio from video
        - Extract key frames from video track
"""
import time
from moviepy.editor import VideoFileClip, AudioFileClip
from Katna.video import Video

"""
    Generate (almost) unique filename
"""
def generate_unique_filename(base_file_name, extension):
    # Get current unix timestamp
    timestamp = int(time.time())
    
    # Append the timestamp to the base file name and return it
    return f"{base_file_name}_{timestamp}.{extension}"


"""
    Extract and save audio from video
"""
def extract_and_save_audio(video_file_name):
    # Extract base file name and extension
    l = video_file_name.split(".")
    base_file_name = l[0]
    video_extension = l[1]

    # Moviepy objects
    video = VideoFileClip(video_file_name)
    audio = video.audio
    audio.write_audiofile((
        generate_unique_filename(base_file_name, "mp3")
    ))


"""
    Extract keyframe from video file
"""
def extract_keyframe(video_file_name):
    # Load Katna object
    vd = Video()
    # Call keyframe detector module
    imgs = vd.extract_frames_as_images(no_of_frames = 1, file_path= video_file_name)
    # Return keyframe
    return imgs