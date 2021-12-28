import joblib
model = joblib.load('model.pkl')
pca = joblib.load('pca.pkl')

class Model():
    def __init__(self):
        pass
    
    def predict(self, data):
        prediction = 0
        data_pca = self.pca(data)

        prediction = model.predict(data_pca)

        return prediction
    
    def pca(self, data):
        pca_data = pca.transform(data)
        return pca_data
