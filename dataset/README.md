## Prepare the dataset 

Download the 20BN_jester_V1_videos.zip from the link below: 

    - https://www.kaggle.com/datasets/kylecloud/20bn-jester-v1-videos
    - Then, run the `unzip_multithread.py` code for decompression. 



※ You can use the command like: 

```bash
~$ unzip <dataset>.zip -d jester-v1  
```

But, it's too slow that it might take around 2-hour. So, pretty recommend to use `unzip_multithread.py`. 



## Preprocess 

The order of image frames of this dataset is not regular. Some clips include not evenly ordered file names. In order to align the names in sequential, run the code below: 

```bash 
~$ python change_name.py
```





