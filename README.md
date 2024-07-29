# Tiny Kilo-D-NeRF-NGP
**WIP**

# Description
Simple, humanly readable, COMMENTED(!) and visualised NeRF and it's encodings.  

## Encodings Results
You can check [Encodings results here](./tiny_grid/README.md), but here is the summary.  
Multiresolution Hash encoding outperform all other encodings.

|Original Image|Raw coodinates: [x, y]|[x, y] Encoded with<br> Frequency Encoding (sin,cos)|
|-|-|-|
|<div align="center"><img src="./data/judi.png" width="200"/>|<div align="center"><img src="./tiny_grid/results/xy2rgb_animation.gif" width="200"/>|<div align="center"><img src="./tiny_grid/results/xyFreq2rgb_animation.gif" width="200"/>|
|-|Encoding dim: 0<br>Training time: 34 sec<br>Loss: 1.8e-2|Encoding dim: 254<br>Training time: 1 min<br>Loss: 9.2e-3|
|[x, y] Encoded with<br> Multiresolution Hash |Encoded with<br> Fourier Features||
|<div align="center"><img src="./tiny_grid/results/xyHash2rgb_animation.gif" width="200"/>|<div align="center"><img src="./tiny_grid/results/xyFourier2rgb_animation.gif" width="200"/>|
|Encoding dim: 16<br>Training time: 1:35 min<br>Loss: 4.7e-6|Encoding dim: 256<br>Training time: 1 min<br>Loss: 4.1e-3|


## NeRF




# Setup
`python=3.9`  
`CUDA Version: 12.2`

Create enviroment with conda or pip:
```
conda env create -f environment.yml
or 
pip install -r requirements.txt
```

## Models
You can download pretrain models from:  
[Google Drive](https://drive.google.com/drive/folders/1bD93brXrHU2QZ_uuXFiHMARtMg4lVdAK?usp=sharing)


# Run
# Flags
# Notebooks descriptions
`tiny_nerf.ipynb`:  
- Training NeRF  

`tiny_d_nerf.ipynb`:
- Training Dynamic NeRF  

`tiny_grid/tiny_simple_prediction_task.ipynb`:
- Training FCN to predict (xy->RGB) and (xyz->RGB) wirh multiresolution hash encodings



# TODO
- [x] Tiny NeRF (One image / Batch training)
- [x] Tiny D-NeRF
- [ ] Grid for NeRF (one image one view) 
- [ ] Tiny NeRF-NGP
- [ ] Tiny D-NeRF-NGP
- [ ] Tiny Kilo-D-NeRF-NGP
---
- [ ] [Cover LIFF pose estimation](https://github.com/fyusion/llff)

# Attributions
- https://github.com/albertpumarola/D-NeRF
- https://github.com/houchenst/FastNeRF
- https://github.com/Hanlin-Zhou/PyTorch-InstantNGP
