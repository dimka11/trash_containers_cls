fix incorrect train labeling

add wandb

#### Models:

* Transformer based backbone for feature extraction (SWIN)

* Two models (Bad quality class vs other) and Photo has trash vs Photo hasn't trash

* EffNetV2

#### Augmentations:

* Horizontal flip

* Resize / center crop

Albumentations:

Decrease quality:

* Noise
* blur
* other (weather, sun etc)

#### Pre/Post

* lbp-based segmentation of defocus blur
https://www.youtube.com/watch?v=li7ZiUQ6ACM&t=780s


#### Other's solutions:

https://github.com/sweetlhare/neuro-wood

https://github.com/dimka11/santa_image_prediction

https://github.com/dimka11/WoodHack

from HealthDataHack:

https://www.kaggle.com/code/dimka11/healthdatahack-base

https://www.kaggle.com/code/dimka11/healthdatahack-tf

https://www.kaggle.com/code/dimka11/healthdatahack-pt



