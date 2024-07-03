from PIL import Image, ImageDraw, ImageFont
import math

_PERFECT_RATIO = True

def readText():

    text = input("Enter the text to be encoded: ")

    binaArr = []
    for element in text:  
        binaArr.append(format(ord(element), '08b'))
    splitBinaArray = []
    for x in binaArr:
        splitBinaArray.append(x[0:2])
        splitBinaArray.append(x[2:4])
        splitBinaArray.append(x[4:6])
        splitBinaArray.append(x[6:8])

    for x in range(4):
        if (len(splitBinaArray)%3!=0):
            splitBinaArray.append('00')
        else:
            break

    return splitBinaArray

def convertToString(s):
    new = ""
    for x in s:
        new += x 
    return new

print("Click the number of the command:")
print("1:Encode the text in image")
print("2:Decode the text in image")
print("3:Encode the image in image")
print("4:Decode the image in image")


      
      
command = int(input())
if(command == 1):
    print("Enter the filename to encode")
    _IMAGE_PATH = input()
    _SAVE_PATH = "a.png"
    bina = readText()
    
    originalImage = Image.open(_IMAGE_PATH)
    processedImage = originalImage.copy()
    
    imgMode = processedImage.mode
    if(imgMode == "RGB"):
        
        pixelNeeded = int(len(bina)/3)
        pixelAvailable = processedImage.size[0]*originalImage.size[1]
        print("Pixles Needed = ",pixelNeeded)
        print("Pixles Avilable",pixelAvailable)
        
        if(pixelNeeded>pixelAvailable):
        
            new_x =0
            new_y =0
            x=(pixelNeeded/pixelAvailable)
        
            if(_PERFECT_RATIO):
                r=math.ceil(math.sqrt(x))
                new_x =processedImage.size[0]*r
                new_y =originalImage.size[1]*r
            else:
                r=math.sqrt(x)
                new_x =math.ceil(processedImage.size[0]*r)
                new_y =math.ceil(originalImage.size[1]*r)
        
        
        
            print("!!! IMAGE HAS BEEN SCALED UP TO MAINTAIN EXTRA DATA !!!")
            print("!!! OLD SIZE",processedImage.size[0],"x",originalImage.size[1],"=",processedImage.size[0]*processedImage.size[1],"  RATIO : ",processedImage.size[0]/processedImage.size[1]," !!!")
            print("!!! NEW SIZE",new_x,"x",new_y,"=",new_x*new_y,"   RATIO : ",new_x/new_y," !!!")
            processedImage=processedImage.resize((new_x,new_y),Image.ANTIALIAS)
        
        
        i=0
        halt=False
        for x in range(processedImage.size[0]):
            for y in range(processedImage.size[1]):
                if(i<len(bina)):  
                    _rgb = processedImage.getpixel((x,y))
                    _r=int(format(_rgb[0],'08b')[0:6]+bina[i],2)
                    _g=int(format(_rgb[1],'08b')[0:6]+bina[i+1],2)
                    _b=int(format(_rgb[2],'08b')[0:6]+bina[i+2],2)
        
                    processedImage.putpixel((x,y),(_r,_g,_b))
                    #print(processedImage.getpixel((x,y)))
                    i=i+3
                else:
                    halt=True
                    break
            if(halt):
                break
        
        
        processedImage.save(_SAVE_PATH,format="png",quality=100)
        print("ENCODED IN IMAGE => ",_SAVE_PATH)
    
    if(imgMode == "RGBA"):
    
        pixelNeeded = int(len(bina)/4)
        pixelAvailable = processedImage.size[0]*originalImage.size[1]
        print("Pixles Needed = ",pixelNeeded)
        print("Pixles Avilable",pixelAvailable)
    
        if(pixelNeeded>pixelAvailable):
    
            new_x =0
            new_y =0
            x=(pixelNeeded/pixelAvailable)
    
            if(_PERFECT_RATIO):
                r=math.ceil(math.sqrt(x))
                new_x =processedImage.size[0]*r
                new_y =originalImage.size[1]*r
            else:
                r=math.sqrt(x)
                new_x =math.ceil(processedImage.size[0]*r)
                new_y =math.ceil(originalImage.size[1]*r)
    
    
    
            print("!!! IMAGE HAS BEEN SCALED UP TO MAINTAIN EXTRA DATA !!!")
            print("!!! OLD SIZE",processedImage.size[0],"x",originalImage.size[1],"=",processedImage.size[0]*processedImage.size[1],"  RATIO : ",processedImage.size[0]/processedImage.size[1]," !!!")
            print("!!! NEW SIZE",new_x,"x",new_y,"=",new_x*new_y,"   RATIO : ",new_x/new_y," !!!")
            processedImage=processedImage.resize((new_x,new_y),Image.ANTIALIAS)
    
    
        i=0
        halt=False
        for x in range(processedImage.size[0]):
            for y in range(processedImage.size[1]):
                if(i<len(bina)):  
                    _rgb = processedImage.getpixel((x,y))
                    _r=int(format(_rgb[0],'08b')[0:6]+bina[i],2)
                    _g=int(format(_rgb[1],'08b')[0:6]+bina[i+1],2)
                    _b=int(format(_rgb[2],'08b')[0:6]+bina[i+2],2)
                    _a=int(format(_rgb[3],'08b')[0:6]+bina[i+3],2)
    
                    processedImage.putpixel((x,y),(_r,_g,_b,_a))
                    #print(processedImage.getpixel((x,y)))
                    i=i+4
                else:
                    halt=True
                    break
            if(halt):
                break
    
    
        processedImage.save(_SAVE_PATH,format="png",quality=100)
        print("ENCODED IN IMAGE => ",_SAVE_PATH)


if(command == 2):
    print("Enter the filename to decode")   
    _IMAGE_PATH = input()
    
    img = Image.open(_IMAGE_PATH)
    print("Image mode", img.mode)
    print("Image Size",img.size[0],"x",img.size[1],"=",img.size[0]*img.size[1])
    
    bina = []
    if(img.mode == "RGB"):
        for x in range(img.size[0]):
            for y in range(img.size[1]):
                _rgb = img.getpixel((x,y))
                _r_bina = format(_rgb[0],'08b')[6:8]
                _g_bina = format(_rgb[1],'08b')[6:8]
                _b_bina = format(_rgb[2],'08b')[6:8]
                bina.append(_r_bina)
                bina.append(_g_bina)
                bina.append(_b_bina)
        for x in range(4):
            if(len(bina)%4!=0):
                bina.append('00')
            else:
                break
         
        characters = []
        
        x=0
        while(x<len(bina)):
            char = int(bina[x]+bina[x+1]+bina[x+2]+bina[x+3],2)
            if((char<127 and char>30) or char==10):
                characters.append(chr(char))
                x=x+4
            else:
                break
        
        
        text = convertToString(characters)
        draw = ImageDraw.Draw(img)
        font = ImageFont.load_default()
        font = font.font_variant(size = 50)
        draw.text((50,50), text,fill = "black",font = font) 

        img.save("b.png")
        print("Decoded text: ",str(text))
        print("Image with text saved as: b.png")

    if(img.mode == "RGBA"):
        for x in range(img.size[0]):
            for y in range(img.size[1]):
                _rgb = img.getpixel((x,y))
                _r_bina = format(_rgb[0],'08b')[6:8]
                _g_bina = format(_rgb[1],'08b')[6:8]
                _b_bina = format(_rgb[2],'08b')[6:8]
                _a_bina = format(_rgb[3],'08b')[6:8]
                bina.append(_r_bina)
                bina.append(_g_bina)
                bina.append(_b_bina)
                bina.append(_a_bina)
        for x in range(4):
            if(len(bina)%4!=0):
                bina.append('00')
            else:
                break

        characters = []

        x=0
        while(x<len(bina)):
            char = int(bina[x]+bina[x+1]+bina[x+2]+bina[x+3],2)
            if((char<127 and char>30) or char==10):
                characters.append(chr(char))
                x=x+4
            else:
                break


        text = convertToString(characters)
        draw = ImageDraw.Draw(img)
        font = ImageFont.load_default()
        font = font.font_variant(size = 50)
        draw.text((50,50), text,fill = "black",font = font) 

        img.save("b.png")
        print("Decoded text: ",str(text))
        print("Image with text saved as: b.png")

if(command == 3):
    print("Enter the filename to encode")
    _IMAGE_PATH = input()
    print("Enter the filename you want to encrypt")
    _IMAGE_TO_CODE_PATH = input()
    _SAVE_PATH = "encoded_image.png"
    print("encoded image saved as: ",_SAVE_PATH)
    original_image = Image.open(_IMAGE_PATH)
    encoded_image = original_image.copy()
    data_image = Image.open(_IMAGE_TO_CODE_PATH)
    if(encoded_image.mode != data_image.mode):
        print("Image mode is not the same")
    else:
        if(encoded_image.mode == "RGB"):
            pixelNeeded = ((encoded_image.size[0])//4)*((encoded_image.size[1])//4)
            pixelAvailable = data_image.size[0]*data_image.size[1]
            print("Pixles Needed = ",pixelNeeded)
            print("Pixles Avilable",pixelAvailable)
            if(pixelNeeded!=pixelAvailable):
                new_x =0
                new_y =0
                #x=(pixelAvailable/pixelNeeded)
                #r=math.ceil(math.sqrt(x))
                new_x =(encoded_image.size[0])//4
                new_y =(encoded_image.size[1])//4
                print("!!! IMAGE HAS BEEN SCALED UP TO MAINTAIN EXTRA DATA !!!")
                print("!!! OLD SIZE",data_image.size[0],"x",encoded_image.size[1],"=",data_image.size[0]*data_image.size[1],"  RATIO : ",data_image.size[0]/data_image.size[1]," !!!")
                print("!!! NEW SIZE",new_x,"x",new_y,"=",new_x*new_y,"   RATIO : ",new_x/new_y," !!!")
                print("Size needed",encoded_image.size[0]*encoded_image.size[1])
                data_image=data_image.resize((new_x,new_y),Image.LANCZOS)
            bina = []
            for k in range(data_image.size[0]):
                for m in range(data_image.size[1]):
                    _rgb_ = data_image.getpixel((k,m))
                    for h in range(3):
                        bina.append(format(_rgb_[h],'08b')[0:2])
                        bina.append(format(_rgb_[h],'08b')[2:4])
                        bina.append(format(_rgb_[h],'08b')[4:6])
                        bina.append(format(_rgb_[h],'08b')[6:8])
            for x in range(4):
                if(len(bina)%4!=0):
                    bina.append('00')
                else:
                    break
            i=0
            halt=False
            for x in range(encoded_image.size[0]):
                for y in range(encoded_image.size[1]):
                    if(i<len(bina)):  
                        _rgb = encoded_image.getpixel((x,y))
                        _r=int(format(_rgb[0],'08b')[0:6]+bina[i],2)
                        _g=int(format(_rgb[1],'08b')[0:6]+bina[i+1],2)
                        _b=int(format(_rgb[2],'08b')[0:6]+bina[i+2],2)
                        encoded_image.putpixel((x,y),(_r,_g,_b))
                        #print(processedImage.getpixel((x,y)))
                        i=i+3
                    else:
                        halt=True
                        break
                if(halt):
                    break
    
            encoded_image.save(_SAVE_PATH, format="png",quality = 100)
            print("Image encoded and saved as:", _SAVE_PATH)
        else:
            pixelNeeded = ((encoded_image.size[0])//4)*((encoded_image.size[1])//4)
            pixelAvailable = data_image.size[0]*data_image.size[1]
            print("Pixles Needed = ",pixelNeeded)
            print("Pixles Avilable",pixelAvailable)
            if(pixelNeeded!=pixelAvailable):
                new_x =0
                new_y =0
                #x=(pixelAvailable/pixelNeeded)
                #r=math.ceil(math.sqrt(x))
                new_x =(encoded_image.size[0])//4
                new_y =(encoded_image.size[1])//4
                print("!!! IMAGE HAS BEEN SCALED UP TO MAINTAIN EXTRA DATA !!!")
                print("!!! OLD SIZE",data_image.size[0],"x",encoded_image.size[1],"=",data_image.size[0]*data_image.size[1],"  RATIO : ",data_image.size[0]/data_image.size[1]," !!!")
                print("!!! NEW SIZE",new_x,"x",new_y,"=",new_x*new_y,"   RATIO : ",new_x/new_y," !!!")
                print("Size needed",encoded_image.size[0]*encoded_image.size[1])
                data_image=data_image.resize((new_x,new_y),Image.LANCZOS)
            bina = []
            for k in range(data_image.size[0]):
                for m in range(data_image.size[1]):
                    _rgb_ = data_image.getpixel((k,m))
                    for h in range(4):
                        bina.append(format(_rgb_[h],'08b')[0:2])
                        bina.append(format(_rgb_[h],'08b')[2:4])
                        bina.append(format(_rgb_[h],'08b')[4:6])
                        bina.append(format(_rgb_[h],'08b')[6:8])
            for x in range(5):
                if(len(bina)%4!=0):
                    bina.append('00')
                else:
                    break
            i=0
            halt=False
            for x in range(encoded_image.size[0]):
                for y in range(encoded_image.size[1]):
                    if(i<len(bina)):  
                        _rgb = encoded_image.getpixel((x,y))
                        _r=int(format(_rgb[0],'08b')[0:6]+bina[i],2)
                        _g=int(format(_rgb[1],'08b')[0:6]+bina[i+1],2)
                        _b=int(format(_rgb[2],'08b')[0:6]+bina[i+2],2)
                        _a=int(format(_rgb[3],'08b')[0:6]+bina[i+3],2)
                        encoded_image.putpixel((x,y),(_r,_g,_b,_a))
                        #print(processedImage.getpixel((x,y)))
                        i=i+4
                    else:
                        halt=True
                        break
                if(halt):
                    break
            
            encoded_image.save(_SAVE_PATH, format="png",quality = 100)
            print("Image encoded and saved as:", _SAVE_PATH)

if(command == 4):    
    print("Enter the filename to decode")
    _SAVE_PATH = input()
    _OUTPUT_PATH = "decoded_image.png"
    encoded_image = Image.open(_SAVE_PATH)
    bina = []
    if(encoded_image.mode == "RGB"):
        for x in range(encoded_image.size[0]):
            for y in range(encoded_image.size[1]):
                _rgb = list(encoded_image.getpixel((x,y)))
                _r_bina = format(_rgb[0],'08b')[6:8]
                _g_bina = format(_rgb[1],'08b')[6:8]
                _b_bina = format(_rgb[2],'08b')[6:8]
                bina.append(_r_bina)
                bina.append(_g_bina)
                bina.append(_b_bina)
        i=0
        halt=False
        decoded_image = Image.new("RGB",((encoded_image.size[0]//4),(encoded_image.size[1]//4)))
        for x in range((encoded_image.size[0]//4)):
            for y in range((encoded_image.size[1]//4)):
                if(i<len(bina)):  
                    _r=int(bina[i]+bina[i+1]+bina[i+2],2)
                    _g=int(bina[i+3]+bina[i+4]+bina[i+5],2)
                    _b=int(bina[i+6]+bina[i+7]+bina[i+8],2)
                    decoded_image.putpixel((x,y),(_r,_g,_b))
                    #print(processedImage.getpixel((x,y)))
                    i=i+9
                else:
                    halt=True
                    break
            if(halt):
                break
        #array = np.array(pixels,dtype = np.uint8)
        #decoded_image = Image.fromarray(array)
        decoded_image.save(_OUTPUT_PATH)
        print("Color image decoded and saved as:", _OUTPUT_PATH)
    if(encoded_image.mode == "RGBA"):
        for x in range(encoded_image.size[0]):
            for y in range(encoded_image.size[1]):
                _rgb = list(encoded_image.getpixel((x,y)))
                _r_bina = format(_rgb[0],'08b')[6:8]
                _g_bina = format(_rgb[1],'08b')[6:8]
                _b_bina = format(_rgb[2],'08b')[6:8]
                _a_bina = format(_rgb[3],'08b')[6:8]
                bina.append(_r_bina)
                bina.append(_g_bina)
                bina.append(_b_bina)
                bina.append(_a_bina)
        i=0
        halt=False
        decoded_image = Image.new("RGBA",((encoded_image.size[0]//4),(encoded_image.size[1]//4)))
        count = 0
        for x in range((encoded_image.size[0])//4):
            for y in range((encoded_image.size[1])//4):
                if(i<len(bina)):  
                    _r=int(bina[i]+bina[i+1]+bina[i+2]+bina[i+3],2)
                    _g=int(bina[i+4]+bina[i+5]+bina[i+6]+bina[i+7],2)
                    _b=int(bina[i+8]+bina[i+9]+bina[i+10]+bina[i+11],2)
                    _a=int(bina[i+12]+bina[i+13]+bina[i+14]+bina[i+15],2)
                    decoded_image.putpixel((x,y),(_r,_g,_b,_a))
                    #print(processedImage.getpixel((x,y)))
                    i=i+16
                else:
                    halt=True
                    break
            if(halt):
                break
        #array = np.array(pixels,dtype = np.uint8)
        #decoded_image = Image.fromarray(array)

        decoded_image.save(_OUTPUT_PATH)
        print("Color image decoded and saved as:", _OUTPUT_PATH)



