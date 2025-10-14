import subprocess, shlex
from pathlib import Path

def extract_audio(video_path: str, out_audio: str = None, sr=16000):
    video_path = Path(video_path)
    if out_audio is None:
        out_audio = str(video_path.with_suffix(".wav"))
    cmd = f'ffmpeg -y -i {shlex.quote(str(video_path))} -ac 1 -ar {sr} -vn {shlex.quote(out_audio)}'
    subprocess.run(cmd, shell=True, check=True)
    return out_audio
