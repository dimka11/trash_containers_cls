fix incorrect train labeling

#### Models:

* Transformer based backbone for feature extraction (SWIN)

* Two models (Bad quality class vs other) and Photo has trash vs Photo hasn't trash

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
