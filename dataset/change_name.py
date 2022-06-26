""" 이미지 파일 번호가 연속적이도록 변환 
    (i.e) 00001.jpg, 00003.jpg, 00004.jpg -> 00001.jpg, 00002.jpg, 00003.jpg
"""
import os 
import os.path as osp 

from tqdm import tqdm 




def new_name(target_dir): 
    fileEx = ".jpg"

    files = sorted([file_ for file_ in os.listdir(target_dir) if file_.endswith(fileEx)])
    for idx, item in enumerate(files):
        old_name = osp.join(target_dir, item)
        new_name = osp.join(target_dir, f"{idx+1:05}.jpg")
#        print(old_name)
        os.rename(old_name, new_name)



def main(): 
    dataset_path = osp.join('jester-v1')
    
    # list of all files to rename 
    path_dirs = [ osp.join(dataset_path, dir) for dir in os.listdir(dataset_path)]


    for target_path in tqdm(path_dirs):
        new_name(target_path)




if __name__ == '__main__':
    main()