fileResponse = read_file("Upload your .xlsx file")
file = fileResponse.file  # File object
url = fileResponse.url  # Url to the file
content = fileResponse.content  # Raw file content
