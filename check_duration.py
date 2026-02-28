import imageio_ffmpeg
import subprocess

ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()
# The ffprobe exe is shipped alongside ffmpeg
ffprobe_exe = ffmpeg_exe.replace('ffmpeg', 'ffprobe')

video_path = "C:\\Users\\Zonia\\Desktop\\JB Woodworks\\Jah Images\\Deck\\My Movie 2.mp4"

result = subprocess.run(
    [ffprobe_exe, "-v", "error", "-show_entries", "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", video_path],
    capture_output=True, text=True
)

if result.returncode == 0:
    duration = float(result.stdout.strip())
    print(f"Video duration is: {duration} seconds")
else:
    print(f"Failed to get duration: {result.stderr}")
