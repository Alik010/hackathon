from image import image_processing
import streamlit as st
from model import load_model
from video import video_processing


def demo(model_path, device, imgsz):
    st.set_page_config(
        page_title="Object Detection using RT-DETR",
        page_icon="🤖",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    background_image = """
    <style>
    [data-testid="stAppViewContainer"] > .main {
        background-image: url("https://images.unsplash.com/photo-1542281286-9e0a16bb7366");
        background-size: 100vw 100vh;  # This sets the size to cover 100% of the viewport width and height
        background-position: center;  
        background-repeat: no-repeat;
    }
    </style>
    """

    st.markdown(background_image, unsafe_allow_html=True)

    # Main page heading
    st.markdown(
        "<h1 style='text-align: center; color: white;'>Нейросеть для мониторинга воздушного пространства вокруг аэропортов</h1>",
        unsafe_allow_html=True)
    # Sidebar
    st.sidebar.header("ML Model Config")

    # Model Options
    model_type = st.sidebar.radio(
        "Select Task", ['Detection'])

    try:
        model = load_model(model_path)
    except Exception as ex:
        st.error(f"Unable to load model. Check the specified path: f{model_path}")
        st.error(ex)

    confidence = float(st.sidebar.slider(
        "Select Model Confidence", 0, 100, 50)) / 100

    iou = float(st.sidebar.slider(
        "Select Model IOU", 0, 100, 50)) / 100

    st.sidebar.header("Image/Video Config")
    source_radio = st.sidebar.radio(
        "Select Source", ['Image', 'Video'])

    if source_radio == "Image":
        image_processing(model, confidence, iou, imgsz, device)
    elif source_radio == "Video":
        video_processing(model, confidence, iou, imgsz, device)


if __name__ == "__main__":
    demo(
        model_path=r"train\runs\detect\train\weights\best.onnx",
        device="gpu",
        imgsz=640
    )
