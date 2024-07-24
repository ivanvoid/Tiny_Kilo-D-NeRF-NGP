import bpy
import os
from math import *
from mathutils import *

import numpy

import os
import sys
_dir = os.path.dirname('./')
sys.path.append(_dir) 
from export_script import get_3x4_P_matrix_from_blender

#set your own target here
target = bpy.data.objects['Cube']
cam = bpy.data.objects['Camera']

bpy.data.objects["Camera"].location = Vector((7.0, 7.0, 7.0))

t_loc_x = target.location.x
t_loc_y = target.location.y
cam_loc_x = cam.location.x
cam_loc_y = cam.location.y

# The different radii range
radius_range = [6] #range(6,18,3) #range(0,10)

R = (target.location.xy-cam.location.xy).length # Radius

init_angle  = (1-2*bool((cam_loc_y-t_loc_y)<0))*acos((cam_loc_x-t_loc_x)/R)-2*pi*bool((cam_loc_y-t_loc_y)<0) # 8.13 degrees
    
target_angle = (pi - init_angle) # Go 180-8 deg more
num_steps = 10 #how many rotation steps

for r in radius_range:
    for x in range(num_steps):
        alpha = init_angle + (x)*target_angle/num_steps
        
        cam.rotation_euler[2] = pi/2 + alpha #
        cam.location.x = t_loc_x+cos(alpha)*r
        cam.location.y = t_loc_y+sin(alpha)*r

        filename = '{:}_{:}_{:}_{:}_{:}'.format(
        r, x, round(alpha,2), round(cam.location.x, 2), round(cam.location.y, 2))

        # Define SAVEPATH and output filename
        file = f'renders/{filename}.png'

#        file = os.path.join('renders/', str(x)+'_'+ str(r)+'_'+str(round(alpha,2))+'_'+str(round(cam.location.x, 2))+'_'+str(round(cam.location.y, 2)))
	
        # Save camera parameters
        P, K, RT = get_3x4_P_matrix_from_blender(cam)
        K = numpy.matrix(K)
        numpy.savetxt(f"./camera_parameters/{filename}_K_3x4_intrinsic.txt", K)
        RT = numpy.matrix(RT)
        numpy.savetxt(f"./camera_parameters/{filename}_RT_3x4_extrinsic.txt", RT)	
        # Render
        bpy.context.scene.render.filepath = file
        bpy.ops.render.render(write_still=True)
    init_angle = alpha
