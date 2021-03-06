import parameter
from population import Population
from genetic_visualisation import plot_demo
from keras_model import KerasDNN
from typing import Tuple
import numpy as np

def fun_to_maximize(genotype):
    
    #here we create a model and calc its score
    dnn_model = KerasDNN( (1,), (1,), genotype['layers'], genotype['neurons'],
             genotype['activation'], genotype['loss_metric'], genotype['optimizer'],
             genotype['batch_norm'], genotype['dropout'], ['accuracy'],
             genotype['last_layer_act'], genotype['kernel_initializer'],
            )
    
    print("I am working!")
    
    print("Parameters: ",  genotype['layers'], genotype['neurons'],
             genotype['activation'], genotype['loss_metric'], genotype['optimizer'],
             genotype['batch_norm'], genotype['dropout'], ['accuracy'],
             genotype['last_layer_act'], genotype['kernel_initializer']
         )
    
    x = np.array([1,2,3])
    y = np.array([0,1,0])
    
    #dnn_model = KerasDNN()
    dnn_model()
    dnn_model.predict( x )#here we need to put training data
    
    score = dnn_model.score(x , y)
    print ("Score: ", score)
    
    return score ##and here- testing data


g_parameter_options = {
    #'input_shape': parameter.IntParameter( (0,10) ), Does not work for now but I don't know if it will be necessery
    #'output_shape': Tuple[ parameter.IntParameter( (0,10) )], Does not work for now but I don't know if it will be necessery
    'layers' : parameter.IntParameter( (10,100) ),
    'neurons': parameter.IntParameter( (10,100) ),
    'activation': parameter.SingleChoiceParameter( ['relu'] ),
    'loss_metric': parameter.SingleChoiceParameter( ['binary_crossentropy'] ), 
    'optimizer': parameter.SingleChoiceParameter( ['adam'] ),
    'batch_norm': parameter.SingleChoiceParameter( [True, False] ), #I wonder if it's better to use IntParameter with (0,1) range repr. boolean?
    'dropout': parameter.FloatParameter( (0.0, 1.0) ),
    #'metrics': parameter.SingleChoiceParameter( ['accuracy'] ), I couldn't make a List of class instances, so for now screw that option
    'last_layer_act': parameter.SingleChoiceParameter( ['softmax'] ), 
    'kernel_initializer': parameter.SingleChoiceParameter( ['he_normal'] )
}
    
pop = 20
iteration = 100
q = Population(g_parameter_options, fun_to_maximize, [0.001, 0.1], 0.8, pop) 

for j in range(0, iteration):
        q.generate_generation()

plot_demo(q)