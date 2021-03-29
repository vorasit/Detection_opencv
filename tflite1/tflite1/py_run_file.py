import os 
os.system('python3 classify_image.py \
--model models/efficientnet-edgetpu-M_quant_edgetpu.tflite \
--labels models/imagenet_labels.txt \
--input images/gun2.jpg')