# Tiny Multiresolution Hash encodings

## Results

### 2D data 
Learning (RGB) form [x,y] coordinates.
|Raw coodinates: [x, y]|[x, y] Encoded with<br> Frequency Encoding (sin,cos)|[x, y] Encoded with<br> Multiresolution Hash |
|-|-|-|
|<div align="center"><img src="./results/xy2rgb_animation.gif" width="200"/>|<div align="center"><img src="./results/xyFreq2rgb_animation.gif" width="200"/>|<div align="center"><img src="./results/xyHash2rgb_animation.gif" width="200"/>|


### 3D data
Data is a "Video" (sequence of images) stacked into 3D shape.  
Learning (RGB) form [x,y,z] coordinates.
|Raw coodinates [x, y, z]|[x, y,z] Encoded with<br> Frequency Encoding (sin,cos)|[x, y, z] Encoded with<br> Multiresolution Hash|
|-|-|-|
|<div align="center"><img src="./results/xyz2rgb_animation.gif" width="200"/>|<div align="center"><img src="./results/xyzFreq2rgb_animation.gif" width="200"/>|<div align="center"><img src="./results/xyzHash2rgb_animation.gif" width="200"/>|

### (3D NeRF) Camera projections to image reconstruction

By [x,y,z] here we mean sampled points along the ray of camera projections.  
Training for 1000 epochs, around 10 minuts.

|Raw camera projections|[x, y,z] Encoded with <br>Frequency Encoding (sin,cos)|[x, y, z] Encoded with<br> Multiresolution Hash|Original image|
|-|-|-|-|
|-|<div align="center"><img src="./results/Cam_xyzFreq2rgb_animation.gif" width="200"/>|<div align="center"><img src="./results/Cam_xyzHash2rgb_animation.gif" width="200"/>|<div align="center"><img src="./results/Original_image.png" width="200"/>|

