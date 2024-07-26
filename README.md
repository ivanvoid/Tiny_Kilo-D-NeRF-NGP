# Tiny Kilo-D-NeRF-NGP

# Description
Simple, humanly readable, COMMENTED(!) and visualised NeRF.  
Still WIP

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
