# with open("../../../Desktop/file.txt","a") as file:
#     content = file.write("somey")
#     print(content)
with open("./some.txt", "r") as s:
    content = s.readline()

print(content[1])
