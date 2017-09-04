import numpy as np
import matplotlib.image as mpimg
import csv
from sklearn import linear_model


# path='D:\\flower\\wnum\\'
path='D:\\flower\\ridgeRegress\\T72\\3340\\simulation\\'
entries_path="D:\\flower\\ridgeRegress\\entries.csv"
out_path='D:\\flower\\ridgeRegress\\T72\\3340\\'
#�����е�ͼƬresize��100*100
h=85
w=56
c=1
pic_num = 2504
#��ȡͼƬ
def read_img(path):
    imgs=[]
    for i in range(pic_num):
        i = i + 1
        im = path+'%d.bmp'%i
        print('reading the images:%s'%(im))
        img=mpimg.imread(im)
        img=np.resize(img,w*h*c) #��data���list[[]]ÿ��ͼƬһ�У�ÿ�е�������h*w*c
        img=img/255    #��һ��
        imgs.append(img)
    return np.asarray(imgs,np.float32)
data=read_img(path)

#��ȡcsv�����������ֺ�����
def read_csv(path):
    data = []
    csvfile = open(path, 'r')
    reader = csv.reader(csvfile)
    for it in reader:
        data.append(it)
    return data[:1],np.asarray(data[1:],np.float32)#�����ֺ����ݷֱ𷵻�

label_name,label = read_csv(entries_path)

#����2504��ֵ��˳��
num_example=data.shape[0]
arr=np.arange(num_example)
np.random.shuffle(arr)
data=data[arr]
label=label[arr]

#ѡ��ع鷽ʽ
regr = linear_model.LinearRegression()
# regr=linear_model.LassoCV(alphas=[0.1, 0.5, 1]) #losscv��֧�ֶ�����
# alphas=np.arange(0.01,100,10) 
# regr=linear_model.RidgeCV(alphas=[0.01, 0.1, 0.5, 1, 3, 5, 7, 10, 20, 100])
regr.fit(data_train, label_train)
#д��ϵ��
csvfile_coe = open(out_path+'coefficients.csv','w',newline='') # ����newline����������֮����һ��
writer_coe = csv.writer(csvfile_coe)
writer_coe.writerow(label_name[0])
len_coef = len(regr.coef_)
len_coef_0 = len(regr.coef_[0])
for i in range(len_coef_0):
    tmp = []
    for j in range(len_coef):
        tmp.append(regr.coef_[j][i])
    writer_coe.writerow(tmp)
csvfile_coe.close()
#д���ؾ�
csvfile_intercept = open(out_path+'intercept.csv', 'w', newline='')
writer_intercept = csv.writer(csvfile_intercept)
writer_intercept.writerow(label_name[0])
writer_intercept.writerow(regr.intercept_)
csvfile_intercept.close()


xPred = data_test
yPred = regr.predict(xPred)
print('score')
print(regr.score(xPred,label_test,sample_weight=None))
print ("predicted y: ")

csvfile_testnum = open(out_path+'testnum.csv','w',newline='') # ����newline����������֮����һ��
writer_testnum = csv.writer(csvfile_testnum)
csvfile_realnum = open(out_path+'realnum.csv','w',newline='') # ����newline����������֮����һ��
writer_realnum = csv.writer(csvfile_realnum)
len_yPred = len(yPred)
for i in range(len_yPred):
    print ('Ԥ��ֵ��',yPred[i])
    print('��ʵֵ��',label_test[i])
    print('****************')
    writer_testnum.writerow(yPred[i])
    writer_realnum.writerow(label_test[i])
csvfile_testnum.close()
csvfile_realnum.close()