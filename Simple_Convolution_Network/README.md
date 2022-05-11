# Simple_Convolution_Network
 
## Data set :
Mnist
(x_train, t_train), (x_test, t_test) = load_mnist(flatten=False)


## model :
![ch07_simple_convnet_model_structure](https://user-images.githubusercontent.com/5304511/133893161-03000422-f59d-4a8c-85e7-604ab7eb526d.png)

### Input / output
   Input dimension : 1 channel  
   Resolution : 28 X 28 Resolution  
   Output dimension : 10 category
 
### SimpleConvNet
 conv_param : convolution Hyper Parameter(type : dictionary)  
 number of kernels : 30  
 kernel size : 5 x 5  
 Padding : None  
 Stride = 1  
 Number of hidden layers : 100  
 Data output size : 10  
 
### Gradient
 grads = {} # save each layer of weight and bias  
   
### Train
 Optimizer : Adam  
 mini_batch_size : 100  
 epochs = 20  
 
 ### result :
  test acc:0.9882  
  mode_save : simple_convnet_result_params.pkl  
    
 ![simple_convnet_result_Figure_1](https://user-images.githubusercontent.com/5304511/133918216-7bb1cb01-4920-440b-9ab8-dc8d588de37b.png)
 

 
 
