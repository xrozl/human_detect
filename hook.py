import torch
import sys

model = torch.hub.load('ultralytics/yolov5', 'yolov5s')  # or yolov5n - yolov5x6, custom
img = ''

if len(sys.argv) == 2:
    img = sys.argv[1]
if img == '':
    exit()

results = model(img)

objects = results.pandas().xyxy[0]
persons = 0
for i in range(len(objects)):
    if objects.name[i] == 'person':
    	persons += 1

if persons == 0:
	print('Not found available persons.')
else:
	print('Found available ' + str(persons) + ' person(s)')
