import os

if os.path.exists("./cropped")==False:
    os.makedirs("./cropped")
 
# Alpha value for the triplet loss function
ALPHA = 0.5
# Image size for the network
IMAGE_SIZE= 96
# Freezing inceptionNet layers
LAYERS_TO_FREEZE= 60
# No of epochs in training Model
NUM_EPOCHS= 1
# No of Steps per Epochs
STEPS_PER_EPOCH= 1
# Batch Size for training
BATCH_SIZE= 64
