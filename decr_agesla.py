import png
import struct
 
filename = "xyz.png"
#Image_load
png_data = png.Reader(filename=filename).read()
png_img_data = list(png_data[2])
array1=[]
array2=[]
 
#pixel_read
counter = 0
while (counter < len(png_img_data[0])):
    for i in range(0,len(png_img_data)-1):
        
        R = png_img_data[i][counter]   
        G = png_img_data[i][counter+1]  
        B = png_img_data[i][counter+2]
        array1.append(R) 
        array1.append(G)
        array1.append(B)

    counter += 4
decoded_data = array1[3:]
#decryption_start

pos=16 
decoded_data2=decoded_data[pos:pos+len(decoded_data)]
for i in range(0,len(decoded_data2)):
    array2.append(decoded_data2[i] ^ decoded_data[i%16])
 
out1 = open ("out.bin", 'wb') #saving_the_bytes
out1.write(bytearray(array2))
out1.close()
