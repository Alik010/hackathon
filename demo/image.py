import streamlit as st
import zipfile
import io
from pathlib import Path
from PIL import Image
import shutil

def load_image(image_file):
    img = Image.open(image_file)
    return img


def process_image_and_generate_txt(image, model, conf, iou, imgsize, output_path,device):
    results = model.predict(image, conf=conf, iou=iou, imgsz=imgsize, device=device)
    txt_res = []
    for i, bbox in enumerate(results[0].boxes.xywhn):
        label = results[0].boxes.cls[i]
        x, y, w, h = bbox
        txt_res.append(f"{int(label)} {x} {y} {w} {h}")

    with open(output_path, 'w') as f:
        for line in txt_res:
            f.write(line + '\n')


def image_processing(model, conf, iou, imgsize,device):
    st.sidebar.header("Upload ZIP file with images")
    uploaded_zip = st.sidebar.file_uploader("Choose a ZIP file", type="zip")

    if uploaded_zip is not None:
        # Create a temporary directory to extract zip file
        with zipfile.ZipFile(uploaded_zip, 'r') as zip_ref:
            zip_ref.extractall("temp_images")

        # Process each image in the extracted directory
        extracted_files = Path("temp_images").glob('*')
        output_zip_buffer = io.BytesIO()

        with zipfile.ZipFile(output_zip_buffer, 'w') as zf:
            for file in extracted_files:
                if file.suffix.lower() in ['.jpg', '.jpeg', '.png']:
                    image = load_image(file)
                    # Process the image and generate a txt file
                    txt_output_path = f"temp_images/{file.stem}.txt"
                    process_image_and_generate_txt(image, model, conf, iou, imgsize, txt_output_path,device)

                    # Add txt file to the zip
                    zf.write(txt_output_path, arcname=f"{file.stem}.txt")

        # Save the zip file
        output_zip_buffer.seek(0)
        st.download_button(
            label="Download ZIP with TXT files",
            data=output_zip_buffer,
            file_name="processed_images.zip",
            mime="application/zip"
        )
        shutil.rmtree("temp_images")
        st.success("Processing complete. The ZIP file with output text files is ready for download.")
