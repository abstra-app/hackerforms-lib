fileResponse = read_image("Upload your .png image")
file = fileResponse.file  # File object
url = fileResponse.url  # Url to the file
content = fileResponse.content  # Raw file content
