import pandas as pd  
from sklearn import preprocessing
import urllib.request
from sklearn.svm import SVC 

dataset = pd.read_csv('/home/silent/anaconda3/bin/palm_down.csv')
dataset.dropna(inplace=True)
x_data = dataset.loc[:,['gx', 'gy', 'gz']].values
y = dataset.loc[:,['direction']]
normalized_x = preprocessing.normalize(x_data)
svm_model_linear = SVC(kernel = 'linear', C = 1).fit(normalized_x, y) 

from sklearn.metrics import accuracy_score
y_pred = svm_model_linear.predict(normalized_x)
print("Accuracy is ", accuracy_score(y,y_pred)*100)

online=False
while True:
    with urllib.request.urlopen('http://192.168.43.177') as x:
        if online == False:
            print("Device online")
            online=True
        data = x.read().decode('utf-8').split()
        inp_data = [data[3],data[4],data[5]]
        result = int(svm_model_linear.predict([inp_data]))
        if result == 1 :
            pos = "left"
        elif result == 2 :
            pos = "right"
        elif result == 3:
            pos = "up"
        elif result == 4:
            pos = "down"
        elif result == 5:
            pos = "fwd"
        elif result == 6:
            pos = "back"
        elif result == 7:
            pos = 'still'
    print('position -',pos)