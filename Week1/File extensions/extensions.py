def lower(x):
     return x.lower()

def main():
    user = input("File name:")
    extension = {"gif": "image/gif", "jpg": "image/jpeg", "jpeg": "image/jpeg", "png": "image/png", "pdf": "application/pdf", "txt": "text/plain", "zip": "application/zip"}
    users = lower(user)

    if "." in users:
         y = users.strip().split(".")[-1]
         u = extension[y] if y in extension.keys() else "application/octet-stream"
         print(u)
         
    else:
         print("application/octet-stream")



main()



