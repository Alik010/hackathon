from ultralytics import RTDETR

def load_model(model_path):
    model = RTDETR(model_path)
    return model