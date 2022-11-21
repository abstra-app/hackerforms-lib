item = ListItemSchema().read("Name").read_email("Email")
ans = read_list(item, min=1, max=3)
# ans = [{'Name': '', 'Email': ''}]
