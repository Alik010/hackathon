import streamlit as st
import os
from utils import convert_avi_to_mp4,search_video
from moviepy.editor import VideoFileClip
from utils import save_list_to_txt,read_list_from_txt,format_timestamps

def process_video(video_path, model, conf, iou, imgsize,device):
    video_res_path = search_video(video_path)
    if video_res_path is None:
        results = model.predict(video_path, conf=conf, iou=iou, imgsz=imgsize,save=True,device=device)
        frame = []
        clip = VideoFileClip(video_path)
        fps = clip.fps
        for i, result in enumerate(results):
            if len(result.boxes.xyxy) > 0:
                frame.append(i)

        processed_indices = []
        for i in range(len(frame)):
            if i == 0 or frame[i] != frame[i - 1] + 1:
                processed_indices.append(frame[i])

        timestamps = [round(frame_index / fps) for frame_index in processed_indices]
        timestamps = list(set(timestamps))
        timestamps = format_timestamps(timestamps)
        path = search_video(video_path)
        directory_path = os.path.dirname(path)
        save_list_to_txt(timestamps,directory_path,"timestamps.txt")

        mp4_path = convert_avi_to_mp4(path)
        return mp4_path, timestamps
    else:
        directory_path = os.path.dirname(video_res_path)
        txt_path = f"{directory_path}/timestamps.txt"
        timestamp = read_list_from_txt(txt_path)
        return video_res_path,timestamp

def video_processing(model, conf, iou, imgsize, device):
    st.sidebar.header("Upload a video file")
    uploaded_video = st.sidebar.file_uploader("Choose a video file", type=["mp4", "avi", "mov", "mkv"])
    save_dir_video = "demo/upload_video"

    if uploaded_video is not None:
        # Create the directory if it doesn't exist
        os.makedirs(save_dir_video, exist_ok=True)

        save_path = os.path.join(save_dir_video, uploaded_video.name)

        # Save the uploaded video
        with open(save_path, mode='wb') as f:
            f.write(uploaded_video.read())

        st.sidebar.video(save_path)

        if st.sidebar.button('Detect'):
            st.sidebar.write("Running detection...")

            path_res,timestamps = process_video(save_path, model, conf, iou, imgsize,device)
            st.video(path_res)
            st.sidebar.success("Detection complete!")

            st.write("Timestamps with objects:")
            for timestamp in timestamps:
                st.write(f"Go to {timestamp} sec")


