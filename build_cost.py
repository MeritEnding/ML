# H(x) =Wx +b
x_data = [1,2,3,4,5]
y_data = [1,2,3,4,5]

W= tf.Variable(2.9)
b= tf.Variable(0.5)
hypothesis =W *x_data +b

# cost(W,b) 에러 제곱의 평균
cost =tf.reduce_mean(tf.square(hypotehsis - y_data))

# tf.reduce_mean()
v =[1.,2.,3.,4.] 
tf.reduce_mean(v) // 2.5

# tf.square() 제곱
tf.square(3)  //9




