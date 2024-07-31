ffmpeg -i 0.gif -vf "select='not(mod(n\,2))'" -vsync vfr ../0_frame_%d.png
ffmpeg -i 1.gif -vf "select='not(mod(n\,4))'" -vsync vfr ../1_frame_%d.png
ffmpeg -i 2.gif -vf "select='not(mod(n\,2))'" -vsync vfr ../2_frame_%d.png
ffmpeg -i 3.gif -vf "select='not(mod(n\,3))'" -vsync vfr ../3_frame_%d.png
rm ../*9* ../*8*

