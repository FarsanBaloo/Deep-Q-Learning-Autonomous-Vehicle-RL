from pathlib import Path
import gymnasium as gym

def record_videos(env, video_folder="videos", name_prefix="rl-video"):
    video_folder = Path(video_folder)
    video_folder.mkdir(parents=True, exist_ok=True)

    # record every episode
    wrapped = gym.wrappers.RecordVideo(
        env,
        video_folder=str(video_folder),
        episode_trigger=lambda ep: True,
        name_prefix=name_prefix,
        disable_logger=True,
    )
    return wrapped

def show_videos(video_folder="videos"):
    video_folder = Path(video_folder)
    vids = sorted(video_folder.glob("*.mp4"))
    print("Videos:")
    for v in vids:
        print(" -", v)
