
from sklearn.linear_model import LogisticRegression     #from sklearn.linear_model:- sklearn/linear_model(sub folder of sklearn)      						                &&&     import LogisticRegression:- a one type of blue print to create LogisticRegression model

X = [[1], [2], [3], [4], [5]]
y = [0, 0, 1, 1, 1]

model = LogisticRegression()  #model:- variable name    &&&    LogisticRegression:- probabiliy Object name
model.fit(X, y)               #fit:- In-build Function    &&&     X=input  y=output

hours = float(input("Enter how many hours you studies = "))

result = model.predict([[hours]])   #predict:- build-in Function    &&&   ([[houre]]) :- 2D lidt OR used to Prediction

if result == 1:
  print(f"Based on you study {hours} hours you you are likely Pass...")
else:
  print(f"Based on you study {hours} hours you you are likely Fail...")