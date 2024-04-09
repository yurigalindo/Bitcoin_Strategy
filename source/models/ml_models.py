from pandas import DataFrame
import sklearn
import sklearn.linear_model
from source.models.abstract_classes import MachineLearningModel,MachineLearningSignal, Signal

class LogisticRegression(MachineLearningModel):
    def __init__(self, **kwargs) -> None:
        self.kwargs = kwargs
        self.classifier = sklearn.linear_model.LogisticRegression(**kwargs)

    def train_model(self, training_data: DataFrame, **kwargs) -> None:
        X = training_data.drop('target', axis=1)
        y = training_data['target']
        self.classifier.fit(X,y,**kwargs)
    
    def predict(self, row: DataFrame, probabilities = False) -> float:
        if probabilities:
            return self.classifier.predict_proba(row)
        return self.classifier.predict(row)
    
class ProbabilityThresholding(MachineLearningSignal):
    def __init__(self, model: MachineLearningModel, threshold: float = 0.5) -> None:
        self.model = model
        self.threshold = threshold
    
    def trade_signal(self, features: DataFrame, usd: float, btc: float) -> Signal:
        p = self.model.predict(features, probablities=True) # expects to deal with a model that can output probabilities
        if p > self.threshold:
            return Signal.BUY
        if p < (1 - self.threshold):
            return Signal.SELL
        return Signal.HOLD
        