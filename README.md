 # BKAI_Hackathon_2024
The repository for BKAI Hackathon 2024 - Traffic Vehicle Detection Track. The competition focuses solely on one task: detecting and classifying vehicle types from traffic cameras under normal or challenging conditions (nighttime, rain, glare, etc.).

The team's score is **0.79/1.0** on scoreboard. We fine-tune RCNN and DETR model for object detection task, then compare their results and choose the best result based on top mAP score and accuracy. The pipeline follows this
![The Traffic Vehicle Detection Pipeline](https://github.com/MinhHung7/BKAI_Hackathon_2024/blob/main/images/BKAI_Hackathon_Pipeline.png)
## The data preprocessing
The origin dataset consists 11022 images (6392 daytime images and 4630 nighttime images). All of images is divided into 10 scenes, each scene is captured by a road camera

Examples of origin dataset
| ![](https://github.com/MinhHung7/BKAI_Hackathon_2024/blob/main/images/cam_07_00169.jpg) | ![](https://github.com/MinhHung7/BKAI_Hackathon_2024/blob/main/images/cam_03_00504_jpg.rf.f1f369d1795b7550be31edabde9c97d3.jpg) |
|-----------------|-----------------|

Unfortunately, the dataset is heavily imbalanced, the number of vehicles like trucks and coach is very less, but the number of motorbike and car is high, so we use data augmentation techniques to increase accuracy and learnable of models, consists **flipped** and **copy-paste** techniques. 
- The flipped techinique is used by [Albumentation]([https://example.com](https://albumentations.ai/docs/api_reference/augmentations/geometric/transforms/)) library.
- The copy-paste techniques is achieved by with each scene, we find the image has the less vehicles, it mean that iamges has more space, and we will copy the image of coaches and trucks to paste into that space
After augment data, we split the new dataset into 2 parts: daytime and nighttime datasets

The dataset before augment
| ![](https://github.com/MinhHung7/BKAI_Hackathon_2024/blob/main/images/Figure_1.png) | ![](https://github.com/MinhHung7/BKAI_Hackathon_2024/blob/main/images/nighttime_origin.png) |
|-----------------|-----------------|

The dataset after augment
| ![](https://github.com/MinhHung7/BKAI_Hackathon_2024/blob/main/images/class1_CAM_07_460.jpg) | ![](https://github.com/MinhHung7/BKAI_Hackathon_2024/blob/main/images/class3_CAM_03_77.jpg) |
|-----------------|-----------------|
## The training
In the training phase, we use 2 pre-trained models are **RCNN** and **DETR** for object detection task, with previous data preprocessing phase, the both models achive high mAP score > 0.85. With each model, we train it on daytime and nighttime datasets, this will help the models have good recognization on difference conditions (light and no-light conditions).
- The total time we take for daytime training is 4 hours with 20000 epochs
- The total time we take for nighttime training is 2 hours with 10000 epochs
## The inference
In the inference, we use both 2 models to detect on the test dataset, then compare the score each sample on 2 models to choose the best results with higher score

![Test_predict1](https://github.com/MinhHung7/BKAI_Hackathon_2024/blob/main/images/test_predict1.jpg)
![Test_](https://github.com/MinhHung7/BKAI_Hackathon_2024/blob/main/images/cam_08_00531_jpg.rf.a0f90e6ba8ce0b083ee1b6b78f899761.jpg)
