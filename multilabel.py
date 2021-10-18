import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

from sklearn.feature_extraction.text import HashingVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.multiclass import OneVsRestClassifier
from sklearn.pipeline import Pipeline


train = pd.read_excel('input/train.xls')
sikayetsayisi=len(train)
yontem=CountVectorizer

print(train.info())
print(train.describe())
print(train.icerik.head())

#creating x and y
x=train.loc[:,'icerik']

z=[0,1,2,3,4,5,6,7]
z[0]=train.loc[:,'Gecikti veya Dağıtıma Çıkmadı']
z[1]=train.loc[:,'Evde yok notu düşüldü veya Kapıya Getirilmedi']
z[2]=train.loc[:,'Telefonlara Cevap Verilmedi']
z[3]=train.loc[:,'İade Süreci']
z[4]=train.loc[:,'Teslim Alınmadı veya Teslim Edilmedi']
z[5]=train.loc[:,'Kötü Diyalog Veya Saygısız Tutum']
z[6]=train.loc[:,'Hasarlı veya Kayıp Paket']
z[7]=train.loc[:,'Hijyen Kurallarına Uyulmadı']

y = train.drop(['id','icerik'],axis=1)

tks = '[A-Za-z0-9]+(?=\\s+)'


pl = Pipeline([
        ('vec', yontem(token_pattern = tks)),
        ('clf', OneVsRestClassifier(LogisticRegression()))
    ])

# Fit to the training data
pl.fit(x,y)

test = pd.read_excel('input/test.xls')
test.info()
#1 missing value

test = test.fillna("")
#predicting
predictions = pl.predict_proba(test.icerik)


toplam=[0,0,0,0,0,0,0,0]
ortalama=[0,0,0,0,0,0,0,0]
for sutun in range (0,len(z)):
    for i in range (0,len(predictions)):
        toplam[sutun]=toplam[sutun]+predictions[i][sutun]
    ortalama[sutun]=toplam[sutun]/len(predictions)



for i in range (0 , len(predictions)):
    for j in range (0,len(z)):
        if predictions[i][j] < ortalama[j]:
            predictions[i][j] = 0
        else:
            predictions[i][j] = 1



# Format predictions in DataFrame: prediction_df
prediction_df = pd.DataFrame(columns=y.columns, index=test.id, data=predictions)

prediction_df.to_excel('predictions.xls')


degisken=0
toplamtahmin=0


for i in range (0 , sikayetsayisi):
    for j in range (0,len(z)):
        toplamtahmin=toplamtahmin+1
        if predictions[i][j] == z[j][i]:
            degisken=degisken+1


yontem=str(yontem)
if "CountVectorizer" in yontem:
    yontem = str(yontem).replace(yontem, "CountVectorizer")
if "TfidfVectorizer" in yontem:
    yontem = str(yontem).replace(yontem, "TfidfVectorizer")
if "HashingVectorizer" in yontem:
    yontem = str(yontem).replace(yontem, "HashingVectorizer")

if len(test)==len(train):
    print("\n"+yontem+" yöntemi ile train edilen "+str(sikayetsayisi)+" test verisinde yapılan toplam " + str(toplamtahmin) + " tahminden " + str(degisken) + " kadarı doğrudur")
    print("doğruluk oranı= %"+ str((100*degisken)/toplamtahmin))
else:
    print("\n"+str(len(test))+" adet veride tahminleme işlemi "+yontem+" yöntemi ile gerçekleştirilmiştir.")

