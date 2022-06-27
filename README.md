## Vehicle-Counting-OpenCv-Web-Application
A Flask Based Web Application to detect vehicles & count them using YOLOV4 & OpenCV

#### This is a deep learning vision-based project, where I have used yolov4 for famous coco-dataset for detection. Through masking I am tracking each vehicle and giving unique id to each vehicle to track every vehicle for counting.

### Architecture Used:-
  #### yolov4, OpenCV, computer vision, html, Flask api.

![track-yolo-gif](https://user-images.githubusercontent.com/52413661/122457543-6170ea00-cfcc-11eb-90fe-641da28949f2.gif)

### How to run on Local Server :-
#### a) In PyCharm, go to settings choose Python interpreter & create a new environment with Python 3.6 or 3.7(as these two works better).

#### b) Open Anaconda prompt & there create a new environment by using the command--
	conda create –n ‘env_name’ python==3.6.5

#### Activate your Environment by using the command--
      conda activate ‘env_name’

#### 2. Install requirements.txt by using the command--
        pip install requirements.txt

#### 3. a) In PyCharm just simply right click & run “main.py” file.

#### b) In Prompt use the command –
        python app.py
