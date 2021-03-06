__author__ = 'hemanshu'
from flask import Flask, render_template, request
import flask
app = Flask(__name__)
#UPLOAD_FOLDER = '/'
#app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/average',methods=['GET','POST'])
def average():
    x=''
    if request.method=='GET':
        return render_template('average.html',source=str(x))
    elif request.method=='POST':
        x=str(request.form['points'])
        try:

            l=str(x).split(',')
            l=list(map(int,l))

            return render_template('average.html',source='Average of '+x+' is '+str(sum(l)/len(l)))
        except :
            return render_template('average.html',source='Invalid Input')
    else :
        return 'Invalid Request'

@app.route('/',methods=['GET', 'POST'])
def new_world():
    return render_template('first.html' )
@app.route('/data_hemanshu',methods=['GET', 'POST'])
def new_world1():
    return render_template('data_hemanshu.html' )
@app.route('/data_prateek',methods=['GET', 'POST'])
def new_world2():
    return render_template('data_prateek.html' )
@app.route('/data_gauravl',methods=['GET', 'POST'])
def new_world3():
    return render_template('data_gauravl.html' )
@app.route('/plot', methods=['GET', 'POST'])
def hello():
    if request.method == 'GET':
        return render_template('welcome_plotter_first.html' )
    elif request.method == 'POST':
        print ('i m in')
        a=request.form['a']
        b=request.form['b']
        c=request.form['c']
        a1=[float(i) for i in str.split(a)]
        b1=[float(i) for i in str.split(b)]
        #c1=[float(i) for i in str.split(c)]
        c1=[[float(q) for q in str.split(i)] for i in str.split(c,',')]
        print(a1)
        print(b1)
        print(c1)
        image=graph_plot(a1, b1, c1)
        return render_template('welcome_plotter.html', source=image)
        #a="he"
        #b="ma"
        #c="n"
    else:
        return 'Invalid Request'
######################################################################################################


def graph_plot(objective,constraints_value,constraints):
    import numpy as np

    import matplotlib.pyplot as plt
    from random import randint
    a=np.array(objective,float)
    b=np.array(constraints_value,float)
    c=np.array(constraints,float)
    m=np.size(b)
    x1=0

    y=None
    X=None
    Y=None

    Common=[(1,1)]
    min1=b[0]/c[0][0]
    max1= b[0]/c[0][0]

    for i in range(m):
        x1=b[i]/(c[i][0])
        if x1<min1:
            min1=x1
        if x1>max1:
            max1=x1
    if min1>0:
        max1=min1
    if max1<0:
        max1=-1*max1
    min1=0
        #print(max1,min1)
    flag=2
    L=[(0,0)]

    fig=plt.figure()

    constraints=fig.add_subplot(121)

    solution=fig.add_subplot(122)


        #print("vgdysubj",x1)
    X=np.arange(min1,max1+0.0001,0.0001)
    print(X[0],X[-1])
    S=['r','g','b']
    Y=np.array([(b[0]-(c[0][0]*k))/c[0][1] for k in X])
    constraints.plot(X,Y,'k')
        #constraints.text(max(list(Y))+10,max(list(X))-20,"Constraints")
    constraints.fill_between(X,Y,facecolor=S[0],alpha=0.4)

    for i in range(1,m):
        y=np.array([(b[i]-(c[i][0]*k))/c[i][1] for k in X])
            #constraints.plot(X,)
        constraints.plot(X,y,'k')
        constraints.fill_between(X,y,facecolor=S[i%3],alpha=0.4)
        flag=2
        for j in range(np.size(X)):
            if y[j]<Y[j]:
                Y[j]=y[j]
                if flag!=0:
                    Common.append((X[j],y[j]))
                flag=0
            else:
                if flag!=1:
                    Common.append((X[j],y[j]))
                flag=1

    for i in range(np.size(X)):
        L.append((X[i],Y[i]))
    print("hello")
    print(Common)
    for k in Common:
        if k not in L:
            Common.remove(k)
    maxa=(0,0)
    print(Common)
    for i in range(len(Common)):
        Common[i]=(round(Common[i][0],3),round(Common[i][1],3))
    print(Common)
    print("hello2")
    max1=round((a[0]*Common[0][0])+((a[1]*Common[0][1])),4)
    print(max1)
    for i in Common:
        if max1<round((a[0]*i[0])+((a[1]*i[1])),4):
            max1=round((a[0]*i[0])+((a[1]*i[1])),4)
            maxa=i
            print(max1)
    print("hello3")
    solution.plot(X,Y,'k')
    for i in range(len(Common)):
        solution.plot(Common[i][0],Common[i][1],'yo')
    print("hell4")
    solution.plot(maxa[0],maxa[1],'ko',markersize=7)
    solution.text(maxa[0],maxa[1],"  Z(max) = {} ".format(max1) )
    print("hello5")
    solution.fill_between(X,Y,facecolor=S[randint(0,2)])

    #solution.text(" Solution ")
    print(max1)
    print("hello")
    S1=str(randint(0,1000))+str(randint(0,1000))+str(randint(0,1000))+str(randint(0,1000))+str(randint(0,1000))+str(randint(0,1000))+str(randint(0,1000))+str(randint(0,1000))
    S1='static/'+S1+'.png'
    plt.savefig(S1)

    #plt.show(fig)
        #plt.show()
    return S1




    #############################################################################################


#@app.route('/google.png')
#def uploaded_file(filename):
#   return flask.send_from_directory('/','google.png')

if __name__ == '__main__':
    app.run()

