from pandas import DataFrame
import sklearn
import sklearn.linear_model
from source.models.abstract_classes import MachineLearningModel, Signal

class LogisticRegression(MachineLearningModel):
    def __init__(self, **kwargs) -> None:
        self.kwargs = kwargs
        self.classifier = sklearn.linear_model.LogisticRegression(**kwargs)

    def reset_training(self) -> None:
        self.classifier = sklearn.linear_model.LogisticRegression(**self.kwargs)
        
    def train_model(self, training_data: DataFrame, **kwargs) -> None:
        X = training_data.drop('target', axis=1)
        y = training_data['target']
        self.classifier.fit(X,y,**kwargs)

    def trade_signal(self, features) -> Signal:
        y = self.predict(features)
        if y>0.66:
            return Signal.BUY
        if y<0.33:
            return Signal.SELL
        return Signal.HOLD
    
    def predict(self, row: DataFrame) -> float:
        return self.classifier.predict_proba(row)
    
    def trade_order(self, direction: Signal, price: float) -> float:
        if direction == Signal.HOLD:
            return 0
        if direction == Signal.BUY:
            return self.usd/price # Buy all in
        return -self.btc # Sell all