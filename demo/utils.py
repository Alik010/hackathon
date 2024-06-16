import os
from moviepy.editor import VideoFileClip


def convert_avi_to_mp4(avi_path):
    mp4_path = os.path.splitext(avi_path)[0] + '.mp4'
    # Конвертация видео
    video_clip = VideoFileClip(avi_path)
    video_clip.write_videofile(mp4_path, codec='libx264')
    os.remove(avi_path)
    return mp4_path

def search_video(video_path):
    directory = "runs/detect"
    video_name = os.path.splitext(os.path.basename(video_path))[0]
    for root, _, files in os.walk(directory):
        for file in files:
            # Извлечение имени файла без расширения
            file_name_without_extension = os.path.splitext(file)[0]
            if file_name_without_extension == video_name:
                return os.path.join(root, file)
    return None


def save_list_to_txt(numbers, directory, filename):
    # Создаем директорию, если она не существует
    os.makedirs(directory, exist_ok=True)

    # Полный путь к файлу
    filepath = os.path.join(directory, filename)

    # Записываем список в файл
    with open(filepath, 'w') as file:
        file.write(str(numbers))


def read_list_from_txt(filepath):
    with open(filepath, 'r') as file:
        content = file.read()

    numbers = [str(num.strip()) for num in content.strip('[]').split(',')]

    return numbers

def format_timestamps(timestamps):
    formatted_timestamps = []
    for timestamp in timestamps:
        minutes = int(timestamp // 60)
        seconds = int(timestamp % 60)
        formatted_timestamp = f"{minutes}:{seconds:02}"
        formatted_timestamps.append(formatted_timestamp)
    return formatted_timestamps