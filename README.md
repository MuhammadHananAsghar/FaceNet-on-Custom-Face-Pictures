# FaceNet-on-Custom-Face-Pictures
FaceNet on Custom Face Pictures

## Usage:
1.Create a dataset of faces for each person and arrange them in below order.

```
root folder 
│
└───Person 1
│   │───IMG1
│   │───IMG2
│   │   ....
└───Person 2
|   │───IMG1
|   │───IMG2
|   |   ....
```

2. Use ```generate_faces.py``` to prepare our dataset for training. Run the following command:
```python generate_faces.py ./YOUR_DIRECTIORY_CONTAINING_DATA ./cropped```. It uses tensorflow mtcnn library.
But i recomend use ```generates_faces.py``` to generate faces using dlib on CPU.

3. Run ```trainer.py``` to train the model. Make changes (if you want) in ```params.py``` to adjust training parameters.
