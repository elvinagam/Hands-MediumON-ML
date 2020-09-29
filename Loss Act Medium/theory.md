---

The right way to train a Deep Learning model (Loss and Activation)
Optimizing the training process of a Neural  Network model is one of the essential points since it can lead to 5+ times better performance. A few hyperparameters can be tuned, however, we will be diving deep into only activation and loss functions which are the main breaking points of the full picture. Initially, talking briefly about both and then, combining them together in a optimized way will be the way we follow in this post.


---

The value of a loss function is repeatedly calculated whenever a neuron is activated. Thus, it enables the layer to "know" how far are the gradients away from the true values they should have in the initial iteration. Eventually, in the next run, weights and biases will be updated accordingly. This iteration is evaluated until the algorithm cannot find any way to reduce the value of the loss function anymore.
When choosing the right cost function for the model, the type of the task assigned (regression or classification), and the output layer configuration is essential. Let's check out the difference in the implementation of the Regression, Binary Classification, and Multi-class Classification tasks.
