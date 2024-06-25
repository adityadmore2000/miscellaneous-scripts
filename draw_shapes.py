import os

import cv2 as cv
import os.path as osp
import numpy as np

def draw_shape(img, *args):
    """
        img: path to image over which shape to draw
        *args: space separated
    """
    try:
        result_dir = osp.join(osp.dirname(__file__),'shape_results')
        os.makedirs(result_dir,exist_ok=True)
        img_opencv = cv.imread(img)
        args = args[0]
        if len(args)>=2:
            if len(args)==2:
                cv.circle(img_opencv,args,5,(255,255,0),-1)
                result_image = os.path.join(result_dir,f"circle_{os.path.basename(img)}")
                cv.imwrite(result_image, img_opencv)
                os.startfile(result_image)
                print(f"output shape drawn to image and stored at: {result_image}")
            elif len(args)==4:
                cv.rectangle(img_opencv,args,(255,0,0),8)
                result_image = os.path.join(result_dir,f"rectangle_{os.path.basename(img)}")
                cv.imwrite(result_image, img_opencv)
                os.startfile(result_image)
                print(f"output shape drawn to image and stored at: {result_image}")
            elif len(args)>4 and len(args)%2==0:
                cv.polylines(img_opencv,np.array(args,dtype=np.int64).reshape((-1, 1, 2)),True,(255,0,0),8)
                result_image = os.path.join(result_dir,f"polylines_{os.path.basename(img)}")
                cv.imwrite(result_image, img_opencv)
                os.startfile(result_image)
                print(f"output shape drawn to image and stored at: {result_image}")
            else:
                print(f"Can't draw shape with coordinates: {args}")
    except Exception as E:
        print(E)

image = r"C:\Users\sez5954\source\repos\projects\Rameshwar_Sir_tasks\scripting\labeling_scripts\shape_results\24_BLK360_3504861_Setup30_right.jpg"
print(cv.imread(image).shape[:])
# draw_shape(image,(1237, 592))
draw_shape(image,(1237-53,592-19))