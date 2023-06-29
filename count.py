import os
labels = len(os.listdir('Pascal/Labels'))
images = len(os.listdir('Pascal/Images'))

vocdevlabels = len(os.listdir('VOCdevkit/VOC2012/Annotations'))
vocdevimages = len(os.listdir('VOCdevkit/VOC2012/JPEGImages'))
print(labels, images)
print(vocdevimages, vocdevlabels)