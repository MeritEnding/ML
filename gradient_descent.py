# 경사 하강법 => GradientTape을 가지고 구현

# 기울기를 얼마만큼 반영할 것인가
learning_rate= 0.01

# Gradient descent

with tf.GreadientTape () as tape:
  hypothesis =W *x_data+b
  cost =tf.reduce_mean(tf.square(hypothesis-y_data))
# 기울기 값을 구해서 튜플로 반
# 경사도 값 미분 값 cost함수에대해서 변수들에대해서 기울기값을 구해서 튜플로 반환 
# w에 대한 기울기는 w_grad b에대한 기울기는 b_grad에 반환

W_grad, b_grad =tape.gradient(cost, [w,b])

W.assign_sub(learning_rate * W_grad)
b.assign_sub(learning_rate * b_grad)


# Full Code
import tensorflow as tf
tf.enable_eager_execution()

x_data =[1,2,3,4,5]
y_data=[1,2,3,4,5]

W= tf.Variable(2.9)
b= tf.Variable(0.5)

learning_rate= 0.01

for i in range(100 +1)

  with tf.GradientTape() as tape:
      hypothesis =W *x_data +b
      cost =tf.reduce_mean(tf.square(hypothesis -y_data))
  W_grad, b_grad =tape.gradient(cost, [W,b])
  W.assign_sub(learning_rate *W_grad)
  b.assign_sub(learing_rate*b_grad)
  if i %10 ==0:
    print("{:5}|{:10.4f}|{:10.4}|{:10.6f}".format(i,W.numpy(),b.numpy(),cost))








