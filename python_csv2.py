from zipfile import*

file=zipfile("myfile.zip",mode='w',ZIP_DEFLATED)


file.write("django.png")
file.write("django.png")
file.close()
print("zip file created sucessfully")
