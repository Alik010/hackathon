from ultralytics import RTDETR
from clearml import Task
import os

os.environ['WANDB_DISABLED'] = 'true'

task = Task.init(
    project_name="Detection",
    task_name="Train",
    tags=["RT-DETR"]
)

model = RTDETR('rtdetr-l.pt')

results = model.train(data='config.yaml', epochs=300, batch=64, optimizer="AdamW", imgsz=640, augment=True, device=0)
