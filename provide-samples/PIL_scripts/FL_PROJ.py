from PIL import Image

imagePath = 'Di.png'
newImagePath = 'Di_UPLOAD.png'
im = Image.open(imagePath)

def magically(im):

    def _pxl(pxl):

        if pxl >= center: pxl += 5
        else: pxl -= 20

        return pxl

    center = 127
    newimdata = []
    start = 0
    slide = 1280

    print(im.getdata()[0])
    for color in range(0, len(im.getdata())):
        
        r, g, b = im.getdata()[color]
            
        if color % 2 == 1:
            newimdata.append((r, g, b))
        else:
            newimdata.append((r - 75, g - 80, b - 100))
            
        
        # newimdata.append((r - 100, g - 130, b))
        # newimdata.append((r - 75, g - 80, b - 0))
    '''for color in im.getdata():
        r, g, b = color
        
        
        # newimdata.append((r - 100, g - 130, b))
        newimdata.append((r - 75, g - 80, b - 0))'''

    print(newimdata[1280])
    newim = Image.new(im.mode,im.size)
    newim.putdata(newimdata)
    newim.show()
    return newim


magically(im).save(newImagePath)
