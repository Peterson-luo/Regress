import tensorflow as tf
import numpy as np
import matplotlib.image as mpimg
import csv

img_path='D:\\flower\\example\\test\\' 
model_path='D:\\workspace\\py33\\model-tmp\\'
pred_path='D:\\flower\\model\\cnn\\predictnum.csv'

h=85
w=56
c=1
pic_num = 200
name=['gDiffuse', 'gSpecular', 'bDiffuse', 'bSpecular']
 
def read_img(path):
    imgs=[]
    for i in range(1,pic_num):
        im = path+'%d.bmp'%i
        print('reading the images:%s'%(im))
        img=mpimg.imread(im)
        img=img/255
        img=np.resize(img,(h,w,c))  #��Ϊͨ����1����Ҫ����c��ֵ
        imgs.append(img)
    return np.asarray(imgs,np.float32)
data=read_img(img_path)
    
with tf.Session() as sess:
   
    saver = tf.train.import_meta_graph(model_path+'model.ckpt.meta')
    saver.restore(sess,tf.train.latest_checkpoint(model_path))
   
    graph = tf.get_default_graph()
    
    x = graph.get_tensor_by_name("x:0")
    feed_dict = {x:data}
   
     
    
    logits = graph.get_tensor_by_name("logits_eval:0")
   
    classification_result = sess.run(logits,feed_dict)
   
    #��ӡ��Ԥ�����
    
    print(classification_result)
    
    #��ȡ��ֵд��csv�ļ�
    csvfile_predictnum = open(pred_path,'w',newline='') # ����newline����������֮����һ��
    writer_predictnum = csv.writer(csvfile_predictnum)
    #��һ��д����
    writer_predictnum.writerow(name) 
    for i in range(len(classification_result)):
        writer_predictnum.writerow(classification_result[i])
    csvfile_predictnum.close()