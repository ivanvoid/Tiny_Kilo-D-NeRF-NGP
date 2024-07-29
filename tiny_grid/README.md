# Tiny Multiresolution Hash encodings

## Results

### 2D data 
Learning (RGB) form [x,y] coordinates.
|Raw coodinates: [x, y]|[x, y] Encoded with<br> Frequency Encoding (sin,cos)|[x, y] Encoded with<br> Multiresolution Hash |Encoded with<br> Fourier Features|
|-|-|-|-|
|<div align="center"><img src="./results/xy2rgb_animation.gif" width="200"/>|<div align="center"><img src="./results/xyFreq2rgb_animation.gif" width="200"/>|<div align="center"><img src="./results/xyHash2rgb_animation.gif" width="200"/>|<div align="center"><img src="./results/xyFourier2rgb_animation.gif" width="200"/>|
|Encoding dim: 0<br>Training time: 34 sec|Encoding dim: 254<br>Training time: 1 min|Encoding dim: 16<br>Training time: 1:35 min |Encoding dim: 256<br>Training time: 1 min|

### 3D data
Data is a "Video" (sequence of images) stacked into 3D shape.  
Learning (RGB) form [x,y,z] coordinates.
|Raw coodinates [x, y, z]|[x, y,z] Encoded with<br> Frequency Encoding (sin,cos)|[x, y, z] Encoded with<br> Multiresolution Hash|Encoded with<br> Fourier Features|
|-|-|-|-|
|<div align="center"><img src="./results/xyz2rgb_animation.gif" width="200"/>|<div align="center"><img src="./results/xyzFreq2rgb_animation.gif" width="200"/>|<div align="center"><img src="./results/xyzHash2rgb_animation.gif" width="200"/>|<div align="center"><img src="./results/xyzFourier2rgb_animation.gif" width="200"/>|
|Encoding dim: 0<br>Training time: 20 sec<br>Loss: 0.0093|Encoding dim: 255<br>Training time: 21 sec<br>Loss: 0.0036|Encoding dim: 18<br>Training time: 38 sec<br>Loss: 7.712e-6|Encoding dim: 256<br>Training time: 31 sec<br>Loss: 0.0031|

### (3D NeRF) Camera projections to image reconstruction ONE IMAGE ONE VIEW

By [x,y,z] here we mean sampled points along the ray of camera projections.  
Training for 1000 epochs, around 10 minuts.

|Raw camera projections|[x, y,z] Encoded with <br>Frequency Encoding (sin,cos)|[x, y, z] Encoded with<br> Multiresolution Hash|Original image|
|-|-|-|-|
|-|<div align="center"><img src="./results/Cam_xyzFreq2rgb_animation.gif" width="200"/>|<div align="center"><img src="./results/Cam_xyzHash2rgb_animation.gif" width="200"/>|<div align="center"><img src="./results/Original_image.png" width="200"/>|

### NeRF Original
Reconstructing 3D volume from images and camera directions.  
Each frame is 50 iterations.  
|Raw camera projections|[x, y,z] Encoded with <br>Frequency Encoding (sin,cos)|[x, y, z] Encoded with<br> Multiresolution Hash|
|-|-|-|
|-|<div align="center"><img src="./results/xyzFREQ_2RGBA_animation.gif" width="200"/>|<div align="center"><img src="./results/xyzHASH_2RGBA_animation.gif" width="200"/>|
