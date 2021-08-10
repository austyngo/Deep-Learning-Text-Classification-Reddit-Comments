import keras.models

class Prediction(object):
    loaded_model = keras.models.load_model(r'saved_model')
    targets = ['AuthCenter', 'AuthLeft', 'AuthRight', 'Centrist', 'Left', 'LibCenter', 'LibLeft', 'LibRight', 'Right']

    def __init__(self, tokenized): 
        self.tokenized = tokenized

    def predict(self):
        prediction = self.loaded_model.predict(self.tokenized)[0]

        #set highest number in prediction to 1 to match dummy encoding
        bool_predict = []
        for p in prediction:
            if p == max(prediction):
                bool_predict.append(1)
            else:
                bool_predict.append(0)
        
        flair = self.targets[bool_predict.index(1)]
        return flair
