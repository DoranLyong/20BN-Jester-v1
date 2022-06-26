import os 
import os.path as osp 

from PIL import Image


dir_path = osp.dirname(osp.realpath(__file__))
os.chdir(dir_path)
#print(os.getcwd())
cwd = os.getcwd()


scene_list = sorted(os.listdir(cwd))



fileEx = r".jpg"


for scene in scene_list:
    path = osp.join(cwd, scene)
    
    files = sorted([file_ for file_ in os.listdir(path) if file_.endswith(fileEx)])
    

    for idx, item in enumerate(files):

        img_path = osp.join(path, item)
        im1 = Image.open(img_path)
        print(img_path)

        new_name = osp.join(path,f"{idx+1:05}.png")

        im1.save(osp.join(path, new_name))

        os.remove(img_path)


        
