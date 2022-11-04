import hackerforms as hf

schema = hf.ListItemSchema().read("aaa").display("bbb")

res = hf.read_list(schema)

print(res)
