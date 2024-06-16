from ultralytics import RTDETR


weight = 'runs/detect/train/weights/best.pt'

model = RTDETR(weight)

model.export(format='onnx',imgsz = 640, dynamic=True,simplify=True)