from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
# gauth.CommandLineAuth()  # 透過授權碼認證
drive = GoogleDrive(gauth)
# Path = "/Users/dwanyu/universityCode/ProfileImage/123.jpg"
file_drive = drive.CreateFile({'title': "test.mp4", 'mimeType': 'video/mp4'})
file_drive.SetContentFile("test.mp4")
file_drive.Upload()
file_drive.GetContentFile("test.mp4")
