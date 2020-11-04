# link -> https://stackoverflow.com/questions/10607468/how-to-reduce-the-image-file-size-using-pil

flask run --host 199.192.27.157 --port 5000

# string array to array

from ast import literal_eval
s = "['a',['b','c','d'],'e']"
print(literal_eval(s))
['a', ['b', 'c', 'd'], 'e']

# office way

from PIL import Image

company_obj = models.Company.objects.get(id=id)

url = str(company_obj.company_compressed_logo.url).split("media-employers")[::-1][0]
base = str(setter.BASE_DIR) # settings base dir # settings imported as setter

path = base+"/media"+url

picture = Image.open(path)
new_pic = picture.resize((120,120),Image.ANTIALIAS) 
print("last", path)
new_pic.save(path, quality=100,optimize=True)


# other way
from PIL import Image


picture = Image.open("dog.jpg")

new_pic = picture.resize((180,180),Image.ANTIALIAS) # 180 is width and 180 is height

new_pic.save("compressed.jpg", quality=100)
# You can add optimize=True to the arguments of you want to decrease the 
# size even more, but optimize only works for JPEG's and PNG's. For other 
# image extensions, you could decrease the quality of the new saved image. 
# You could change the size of the new image by just deleting a bit of code 
# and defining the image size and you can only figure out how to do this 
# if you look at the code carefully. I defined this size:


print(new_pic.size)


# another way

compressed_picture = picture.save("compressed_picture.jpg", optimize=True, quality=10)

print(picture.size)


# another way

# lets say you have a model called Book and on it a field called 
# 'cover_pic', in that case, you can do the following to compress 
# the image:

from PIL import Image
b = Book.objects.get(title='Into the wild')
image = Image.open(b.cover_pic.path)
image.save(b.image.path,quality=20,optimize=True)
