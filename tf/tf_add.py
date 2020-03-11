
import tensorflow  as tf

def tf_add():
    a_t = tf.constant(2)
    b_t = tf.constant(3)

    c_t = a_t + b_t

    print("Tensorflow adding: ", c_t)

    with tf.Session() as sess:
        c_t_value = sess.run(c_t)
        print("c_t_value: ", c_t_value)

if __name__ == "__main__":
    tf_add()