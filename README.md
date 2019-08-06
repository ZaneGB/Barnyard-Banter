# Barnyard-Banter


Many of us delight in our childhood memories of visiting farms, playing with the animals and learning their sounds. Our vision was to recreate those blissful times for today’s children of all ages.  The “Barnyard Banter” project team, consisting of Alejandro Montesinos, Christian de Vera, Lester Strouse and Zane Brown designed an interactive web application that I think you will enjoy.

Machine Learning

At first we needed to create a program that would recognize and distinguish between the four animals we chose: cats, cows, dogs and sheep. This required machine learning. We sourced our training images from the “animals-10” database, with a test file consisting of 5000 dogs and 2000 of each of our other barnyard pals. We chose 200 validation (test) photos by hand, 50 of each animal.

To build and train the ML model we used Keras, an open-source neural-network library written in Python. Combining Keras with TensorFlow allowed us to to treat multidimensional arrays (tensors).

Conventional neural networks are good with data, but no so much with images. For that reason we built a convoluted neural network. These networks are composed of an input layer, an output layer and several hidden layers, some of which are convolutional, hence its name. 
The convolutional layers are linear, but go through an activation function to become non-linear. We selected LeakyRely as our activation function to avoid dying neurons. This is a common problem with CNN models when all negative inputs are set to zero . The gradient flowing through the unit can get knocked off the data manifold and no longer discriminate between inputs. LeakyRelu allows a small non-zero gradient when the input is not active. In other words, y = y if y >= 0 else y=(alpha)(y) where  0 <alpha< 1. 

“Flatten” unstacks the multidimensional tensors into one dimension, so they can be used as input for an interconnected Dense layer. Including a “dropout” layer removes a specified percentage of input altogether, thereby reducing the chance of overfitting the data. The final layer “softmax”  maps each output such that the sum is 1, hence normalizing the input into a probabilistic distribution.
Through research and trial and error we chose the optimal number of epochs as 7, batch size = 50, dropout rate of 0.5 and alpha (the negative slope coefficient) = 0.3 for the activation function.

Learning rate is an important aspect of optimizing an ML model. Learning rate can be construed as the number and size of the steps you take to reach the bottom of a pit. If you choose a large value as learning rate, there is also a huge probability that you will overshoot the bottom and end up on the other side of the pit. Set a small value as the learning rate and your algorithm will take a longer time to converge. Hence, you would have to train the data for a longer period of time. The RMSprop optimizer we employed is a gradient descent algorithm with momentum. RMSprop allows us to shorten the length of our strides as we converge on the bottom of the pit. 

Through these efforts the Barnyard Banter team achieved an overall accuracy rate of 90%  (99% for cows, 92% for cats, 88% for sheep and 79% for dogs). Only a 79% accuracy rate for dogs despite the fact that nearly half of the images in the training sample were canines? Perhaps this is due to differentiation - the sheer number of varieties and sizes of dogs as compared to our other barnyard friends.

Use your Imagination and Explore with us

Once the users upload their photos through URLs or their own personal image files in the home page, they are directed to the results page. Here we inputted a fieldset. At the top, we see what type of animal our model recognizes in the uploaded image.
 
Right below, the uploaded image itself is displayed. There is then the “Play Sound” button right below that which plays an audio mp3 file of the animal sound our model predicted. If our model correctly recognized the animal in the user’s picture there is the “Yes” button the user can click. That button plays an audio file of an audience cheering. If the model is incorrect, the user can then click the “No” button, which plays audio of a man booing.
 
At the bottom of the page, below the fieldset is the “Play Again” navbar that redirects the user back to the home page so they can do the whole thing again.
