## this script is run to convert the pascal files into a yolo format. 
## It resizes the pictures and bound boxes from the xml files, which are then put in a text file,
## to obtain a dataset with images and labels corresponding to the yolo format

import xml.etree.ElementTree as xml
import os
from PIL import Image

def create_dataset():
    #get the paths where we can find the data
    images_path = 'VOCdevkit/VOC2012/JPEGImages'
    xml_path = 'VOCdevkit/VOC2012/Annotations'

    #define the path to where we want to export the new and improved dataset
    images_output_path = 'Pascal/Images'
    label_output_path = 'Pascal/Labels'
    os.makedirs(images_output_path, exist_ok= True)
    os.makedirs(label_output_path, exist_ok= True)

    yolo_size = 448

    for filename in os.listdir(xml_path):
        #get the according image file:  
        image_path = os.path.join(images_path, filename[:-3]+'jpg')
        image = Image.open(image_path)
        #resize and save the image
        image_yolo = image.resize((yolo_size,yolo_size))
        image_yolo.save(images_output_path +'/'+ filename[:-3] + 'jpg')

        #now we need to get the new bounding box coords, 
        #so we can make a txt file with the classes and the coords
        txt_path = os.path.join(label_output_path +'/'+ filename[:-3] + 'txt')   
        tree = xml.parse(xml_path+'/'+filename)
        root = tree.getroot()

        #get the width and height of this image, so we can scale the x and y coords
        image_width = image.width
        image_height = image.height

        with open(txt_path, 'w') as output_txt:

            for object in root.findall('object'):
                #for each identifiable object in the picture, we get the label and write it to the text file
                label = get_class(object.find('name').text)
                output_txt.write(str(label) + ' ')

                #find and rescale the boundboxes, then convert them to the yolo format
                for box in object.findall('bndbox'):
                    xmin = float(box.find('xmin').text) * (yolo_size / image_width)
                    ymin = float(box.find('ymin').text) * (yolo_size / image_height)
                    xmax = float(box.find('xmax').text) * (yolo_size / image_width)
                    ymax = float(box.find('ymax').text) * (yolo_size / image_height)

                    #yolo format
                    x_centered = int((xmin + xmax) / 2)
                    y_centered = int((ymin + ymax) / 2)
                    x_width = int(xmax - xmin)
                    y_height = int(ymax - ymin)

                    yolo_boundbox = [x_centered,y_centered,x_width,y_height]
                    for n in yolo_boundbox:
                        output_txt.write(str(n)+' ')

                #write a new line for each different example of an object in the file
                output_txt.write('\n')

def get_class(c):
    pascal_classes = {
    "aeroplane": 0,
    "bicycle": 1,
    "bird": 2,
    "boat": 3,
    "bottle": 4,
    "bus": 5,
    "car": 6,
    "cat": 7,
    "chair": 8,
    "cow": 9,
    "diningtable": 10,
    "dog": 11,
    "horse": 12,
    "motorbike": 13,
    "person": 14,
    "pottedplant": 15,
    "sheep": 16,
    "sofa": 17,
    "train": 18,
    "tvmonitor": 19
    }
    return pascal_classes[c]

if __name__ == '__main__':
    create_dataset()

