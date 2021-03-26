import os
import instaloader
import requests
mod = instaloader.Instaloader()
profile = instaloader.Profile.from_username(mod.context, "elihsiehmusic")
# mod.download_igtv(profile, fast_update=False, post_filter=None)

saveDir = "./InstagramDownload/"
if not os.path.isdir(saveDir):
    os.mkdir(saveDir)


for i, item in enumerate(profile.get_posts()):
    if item.video_url is not None:
        username = f"UserPost_number_{i}"
        video = requests.get(item.video_url)
        with open(saveDir + username + ".mp4", 'wb') as f:
            f.write(video.content)
            print(username + "下載完成")
