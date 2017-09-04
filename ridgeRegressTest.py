import csv
import numpy as np
import matplotlib.image as mpimg

h=85
w=56
c=1
pic_num = 200
predict_num = []
path_pic = 'D:\\flower\\ridgeRegress\\T72\\3383\\test\\'
path_coefficients = 'D:\\flower\\ridgeRegress\\coefficients.csv'
path_intercept = 'D:\\flower\\ridgeRegress\\intercept.csv'
path_predtion='D:\\flower\\ridgeRegress\\T72\\3383\\predictnum.csv'


#��ȡͼƬ
def read_img(path):
    imgs=[]
    for i in range(pic_num):
        i = i + 1
        im = path+'%d.bmp'%i
#         print('reading the images:%s'%(im))
        img=mpimg.imread(im)
        img=np.resize(img,(h,w,c))  #��Ϊͨ����1����Ҫ����c��ֵ
        img=np.resize(img,w*h)   #��data���list[[]]ÿ��ͼƬһ�У�ÿ�е�������h*w*c
        img=img / 255.0;
        imgs.append(img)
    return np.asarray(imgs,np.float32)
data=read_img(path_pic)
# data = np.resize(data,[pic_num,h*w*c]) #��data���list[[]]ÿ��ͼƬһ�У�ÿ�е�������h*w*c

#��ȡcsv�����������ֺ�����
def read_csv(path):
    data = []
    csvfile = open(path, 'r')
    reader = csv.reader(csvfile)
    for it in reader:
        data.append(it)
    return data[:1],np.asarray(data[1:],np.float32)#�����ֺ����ݷֱ𷵻�

coefficients_name,coefficients_num = read_csv(path_coefficients)
intercept_name,intercept_num = read_csv(path_intercept)

#����ȡ��ͼƬ��ϵ�����+�ؾ࣬���Ԥ��ֵ,ע��coefficients���������н���
print(intercept_name[0])
for num in range(len(data)):
    predict = []
    for i in range(4):
        tmp = 0
        for j in range(len(coefficients_num)):
            tmp += coefficients_num[j][i]*data[num][j]
        tmp += intercept_num[0][i]
        predict.append(tmp)
    predict_num.append(predict)
#     print('��%i��ͼ'%(1+num))
#     print(predict)
    
#��ȡ��ֵд��csv�ļ�
csvfile_predictnum = open(path_predtion,'w',newline='') # ����newline����������֮����һ��
writer_predictnum = csv.writer(csvfile_predictnum)
#��һ��д����
writer_predictnum.writerow(coefficients_name[0]) 
for i in range(len(predict_num)):
    writer_predictnum.writerow(predict_num[i])
csvfile_predictnum.close()