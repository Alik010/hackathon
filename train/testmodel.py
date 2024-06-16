import os
from ultralytics import RTDETR

model = RTDETR("runs/detect/train2/weights/best.pt")
metrics = model.val(data="config.yaml", split='test', conf = 0.25,imgsz = 640,iou=0.6)