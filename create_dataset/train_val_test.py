import os
import random
import shutil

# Пути к папкам с данными
images_dir = r'C:\Users\aliko\Downloads\had\hackathon_additional_dataset\images'
labels_dir = r'C:\Users\aliko\Downloads\had\hackathon_additional_dataset\labels'

# Пути к папкам для train, test и val наборов
train_images_dir = r'C:\Users\aliko\PycharmProjects\hackathon\dataset\images\train'
train_labels_dir = r'C:\Users\aliko\PycharmProjects\hackathon\dataset\labels\train'

test_images_dir = r'C:\Users\aliko\PycharmProjects\hackathon\dataset\images\test'
test_labels_dir = r'C:\Users\aliko\PycharmProjects\hackathon\dataset\labels\test'

val_images_dir = r'C:\Users\aliko\PycharmProjects\hackathon\dataset\images\val'
val_labels_dir = r'C:\Users\aliko\PycharmProjects\hackathon\dataset\labels\val'

# Создаем директории для train, test и val наборов, если их нет
os.makedirs(train_images_dir, exist_ok=True)
os.makedirs(train_labels_dir, exist_ok=True)
os.makedirs(test_images_dir, exist_ok=True)
os.makedirs(test_labels_dir, exist_ok=True)
os.makedirs(val_images_dir, exist_ok=True)
os.makedirs(val_labels_dir, exist_ok=True)

# Получаем список всех изображений
all_images = [f for f in os.listdir(images_dir) if os.path.isfile(os.path.join(images_dir, f))]

# Перемешиваем список файлов
random.shuffle(all_images)

# Распределяем файлы по наборам
train_images = all_images[:21500]
test_images = all_images[21500:22000]
val_images = all_images[22000:22500]


# Функция для перемещения файлов изображений и аннотаций
def move_files(image_list, dest_images_dir, dest_labels_dir):
    for image in image_list:
        image_path = os.path.join(images_dir, image)
        label_path = os.path.join(labels_dir, os.path.splitext(image)[0] + '.txt')

        if os.path.exists(label_path):  # Проверяем наличие файла аннотации
            shutil.move(image_path, os.path.join(dest_images_dir, image))
            shutil.move(label_path, os.path.join(dest_labels_dir, os.path.splitext(image)[0] + '.txt'))
        else:
            print(f"Аннотация для изображения {image} не найдена. Пропуск.")


# Перемещаем файлы в соответствующие директории
move_files(train_images, train_images_dir, train_labels_dir)
move_files(test_images, test_images_dir, test_labels_dir)
move_files(val_images, val_images_dir, val_labels_dir)

print("Распределение файлов завершено.")
