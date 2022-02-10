import tensorflow as tf
from tensorflow.python.platform import gfile

#GRAPH_PB_PATH_TRT = './converted_trt_graph_ss/trt_graph_ss_model.pb'
GRAPH_PB_PATH_FROZEN_SS='./frozen_model_ss/frozen_model_ss_plf.pb'

tf_config = tf.ConfigProto()
#tf_config.gpu_options.allow_growth = False
tf_config.gpu_options.per_process_gpu_memory_fraction = 0.2
tf_sess = tf.Session(config=tf_config)

with tf.Session() as sess:
   print("load graph")
   with gfile.FastGFile(GRAPH_PB_PATH_FROZEN_SS,'rb') as f:
       graph_def = tf.GraphDef()
   graph_def.ParseFromString(f.read())
   sess.graph.as_default()
   tf.import_graph_def(graph_def, name='')
   graph_nodes=[n for n in graph_def.node]
   names = []
   for t in graph_nodes:
      names.append(t.name)

   #print(names)
