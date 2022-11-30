import numpy as np
import tflite_runtime.interpreter as tflite
from PIL import Image
import sys, time
import glob
import os
from datetime import datetime 
from matplotlib import pyplot as plt

model_path='/home/pablo/model.tflite'
imgs_path='/home/pablo/beach/'
labels_file='/home/pablo/labels.txt'
save_path='/home/pablo/beach/plt.jpg'

interpreter = tflite.Interpreter(model_path=model_path)
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()
_, height, width, _ = interpreter.get_input_details()[0]['shape']
size = [width, height]

def load_labels(filename):
  with open(filename, 'r') as f:
    return [line.strip() for line in f.readlines()]

labels=load_labels(labels_file)
start = time.perf_counter()
img_seq=[]
globs=glob.glob(imgs_path + datetime.now().strftime('%Y-%m-%d') + "*.jpg")
inference_ouput=np.zeros(shape=(
    len(globs),
    len(labels)
    ))
pointer=0
print('found globs:', len(globs))
for file in sorted(globs):
    print('inferring', file)
    image = Image.open(file).convert('RGB').resize(size, Image.Resampling.LANCZOS)
    input_data = np.array(np.asarray(image), dtype=np.float32)
    input_data = np.expand_dims(input_data , axis=0)
    interpreter.set_tensor(input_details[0]['index'], input_data)

    interpreter.invoke()
    output_data = interpreter.get_tensor(output_details[0]['index'])[0]

    for i in range(len(labels)):
        print('{:08.6f}: {}'.format(float(output_data[i]), labels[i]))
    img_seq.append(os.path.basename(file)[11:16])
    inference_ouput[pointer]=output_data
    pointer+=1
    print('output data', output_data)
inference_time = time.perf_counter() - start
print('inference time: ','%.1fms' % (inference_time * 1000))    

inference_ouput=inference_ouput.transpose()
pointer=0
plt.style.use('dark_background')
plt.rcParams["figure.figsize"] = [8, 6]
fig, ax = plt.subplots()
ax.stackplot(img_seq, inference_ouput*100)
plt.legend(labels)
plt.xticks(rotation = 45)
plt.savefig(save_path)

