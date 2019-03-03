#This converts PASCAL VOC formatted XML files to one single JSON file suitable for TensorBox

import xml.etree.ElementTree as ET
import json
import os

#Insert path to data folder here
path = '' #ex:/home/username/tensorbox/data/tagged
image_files = []

for filename in os.listdir(path):
	if not filename.endswith('.xml'): continue
	xml_file = os.path.join(path, filename)
	e = ET.parse(xml_file).getroot()
	jsonObject = {}
	boxes = []
	for object in e.findall("object"):
		box={}
		box["x1"]= int(object.find('bndbox/xmin').text)
		box["x2"]= int(object.find('bndbox/xmax').text)
		box["y1"]= int(object.find('bndbox/ymin').text)
		box["y2"]= int(object.find('bndbox/ymax').text)
		boxes.append(box)

	jsonObject["image_path"] = e.find('folder').text +'/'+ e.find('filename').text
	jsonObject["rects"] = boxes
	image_files.append(jsonObject)

with open("output.json", "w") as text_file:
    json.dump(image_files, text_file, indent=2, sort_keys=True)

print("Done. Please check output.json")
