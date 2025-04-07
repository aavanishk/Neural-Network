import numpy as np

features=np.array([
    [0,0],
    [0,1],
    [1,0],
    [1,1]
])

labels = np.array([0,0,0,1])

w=[0.9,0.9]
threshold=0.5
learning_rate=0.1
epoch = 20 #learning time

for j in range(0,epoch):
    print("epoch",j)
    for i in range(0,features.shape[0]):
        instance=features[i]
        x0=instance[0]
        x1=instance[1]
    
        sum_unit=x0*w[0]+x1*w[1]
    
        if sum_unit>threshold:
            fire=1
        else:
            fire=0
        delta=labels[i]-fire
        print("prediction:", fire,"whereas actual was",labels[i],"(error:",delta,")")
    
        w[0]=w[0]+delta*learning_rate
        w[1]=w[1]+delta*learning_rate
    print("----------------------------------")

   