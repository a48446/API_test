import os
import facebook
import requests
from FaceBookUserData import *

saveDir = "./ProfileImage/"
if not os.path.isdir(saveDir):
    os.mkdir(saveDir)

graph = facebook.GraphAPI(access_token=user_token)
user_data = graph.get_object(id=user_id, fields="name")
image_data = graph.get_object(
    id=user_id, fields="picture")["picture"]
media_data = graph.get_object(
    id=user_id, fields="posts{source}")["posts"]["data"]

user_id = user_data['id']
user_name = user_data['name']
image_url = image_data["data"]["url"]


media_url = []
for i, item in enumerate(media_data):
    if "source" in item:
        media_url.append(item.get("source"))


img = requests.get(image_url)
with open(saveDir + user_name+".jpg", 'wb') as f:
    f.write(img.content)

video = requests.get("".join(media_url))
with open(saveDir+user_name+".mp4", 'wb') as f:
    f.write(video.content)
