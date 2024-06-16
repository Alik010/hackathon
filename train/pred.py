from ultralytics import RTDETR

model = RTDETR("runs/detect/train/weights/best.pt")
# Define path to video file
source = "test1.jpg"

# Run inference on the source
results = model.predict(source, imgsz=640, conf=0.5,save=True)
# txt_res = []
# for i,bbox in enumerate(results[0].boxes.xywhn):
#     print(results[0].boxes.cls[i],bbox)
#     label = results[0].boxes.cls[i]
#     x,y,w,h = bbox
#     txt_res.append(f"{int(label)} {x} {y} {w} {h}")
# print(txt_res)