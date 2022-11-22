fileResponse = read_video("Upload your video")
file = fileResponse.file  # File object
url = fileResponse.url  # Url to the file
content = fileResponse.content  # Raw file content
