from PIL import Image

imagePath = 'Di.png'
newImagePath = 'Di_UPLOAD.png'
img = Image.open(imagePath)
pixels = img.load() # create the pixel map

black_2 = []
for i in range(img.size[0]):
    if i % 2 == 0:
        black_2.append(i)

black_1 = [i-1 for i in black_2 if i > 0]
if img.size[0] % 2 == 0: # 'that' if statement
    black_1.append(img.size[0]-1)


for i in black_1:
    for j in range(0, 720, 2):
        r, g, b = pixels[i,j]
        pixels[i,j] = (20, 20, 20)

for k in black_2:
    for l in range(1, 720+1, 2):
        r, g, b = pixels[i,j]
        pixels[i,j] = (20, 20, 20)

img.save('DI_UPLOAD.png')