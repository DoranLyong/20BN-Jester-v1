# Prepare Jester-v1 dataset

### Data Preparation

Firstly, we need to download the [Jester](https://20bn.com/datasets/jester/v1) dataset. 

*  ***(Notice)*** The official link is expired, so I refer to the other link in [kaggle dataset](https://www.kaggle.com/datasets/kylecloud/20bn-jester-v1-videos).

* place the `.zip` file into the `dataset` directory. 

* extract the frames by running 

  ```python
  cd dataset 
  python unzip_multithread.py
  ```

  

### Process the data and generate corresponding labels

Finally, we get category.txt, train_videofolder.txt, val_videofolder.txt and test_videofolder.txt documents.

```
python3 datas/generate_label.py
```



***

### Reference 

1. https://github.com/jiamingNo1/Temporal-Shift-Module/tree/master/datas

   
