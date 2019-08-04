import pandas as pd  
import numpy as np
from sklearn import preprocessing
from sklearn.metrics import confusion_matrix
import urllib.request

dataset = pd.read_csv('C:\\Users\\Admin\\nodemcu_dataset.csv')
dataset.dropna(inplace=True)
x_data = dataset.loc[:,['ax', 'ay', 'az', 'gx', 'gy', 'gz']].values
y = dataset.loc[:,['position']]

normalized_x = preprocessing.normalize(x_data)

from sklearn.svm import SVC 
svm_model_linear = SVC(kernel = 'linear', C = 1).fit(normalized_x, y) 
while True:
    with urllib.request.urlopen('http://192.168.1.72') as x:
        data = x.read()
        data = data.decode('utf-8')
        inp_data = data.split()
        #print(inp_data)
        result = int(svm_model_linear.predict([inp_data]))
        if result == 1 :
            pos = "palm down"
        elif result == 2 :
            pos = "face up"
        elif result == 3:
            pos = "face down"
        elif result == 4:
            pos = "left side"
        elif result == 5:
            pos = "palm up"
    print("Position = ",pos)


from sklearn.metrics import accuracy_score
y_pred = svm_model_linear.predict(normalized_x)
print("Accuracy is ", accuracy_score(y,y_pred)*100)