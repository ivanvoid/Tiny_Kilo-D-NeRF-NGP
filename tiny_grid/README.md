# Tiny Multiresolution Hash encodings

## Results

### 2D data 
Learning (RGB) form [x,y] coordinates.
|Raw coodinates: [x, y]|[x, y] Encoded with Frequency Encoding (sin,cos)|[x, y] Encoded with Multiresolution Hash |
|-|-|-|
|<div align="center"><img src="./results/xy2rgb_animation.gif" width="200"/>|<div align="center"><img src="./results/xyFreq2rgb_animation.gif" width="200"/>|<div align="center"><img src="./results/xyEncode2rgb_animation.gif" width="200"/>|


### 3D data
Data is a "Video" (sequence of images) stacked into 3D shape.  
Learning (RGB) form [x,y,z] coordinates.
|Raw coodinates [x, y, z]|[x, y,z] Encoded with Frequency Encoding (sin,cos)|[x, y, z] Encoded with Multiresolution Hash|
|-|-|-|
|<div align="center"><img src="./results/xyz2rgb_animation.gif" width="200"/>|<div align="center"><img src="./results/xyzFreq2rgb_animation.gif" width="200"/>|<div align="center"><img src="./results/xyzEncode2rgb_animation.gif" width="200"/>|


## TODO
- [ ] Freq Encoder test