FROM pytorch/pytorch:2.1.1-cuda12.0-cudnn8-runtime
#FROM nvcr.io/nvidia/pytorch:22.08-py3
ENV TZ=Europe/Moscow
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y
RUN apt-get install -y python3
RUN apt-get install -y python3-pip

#WORKDIR /home/demo
WORKDIR /usr/src/app
COPY . ./

RUN apt install -y exiftool
RUN pip install -r requirements.txt
RUN export PYTHONPATH='..'

ENTRYPOINT [ "streamlit" ]
CMD [ "run", "demo/app.py", "--browser.serverAddress", "0.0.0.0", "--server.fileWatcherType", "none", "--server.port", "8510"]