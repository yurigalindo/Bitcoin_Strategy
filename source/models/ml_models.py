from pandas import DataFrame,Series
import sklearn
import sklearn.linear_model
from source.models.abstract_classes import MachineLearningModel,MachineLearningSignal, Signal
import warnings

class LogisticRegression(MachineLearningModel):
    def __init__(self, **kwargs) -> None:
        self.kwargs = kwargs
        self.classifier = sklearn.linear_model.LogisticRegression(**kwargs)

    def train_model(self, training_data: DataFrame, **kwargs) -> None:
        X = training_data.drop('target', axis=1)
        X = X.drop('Date',axis=1)
        y = training_data['target']
        self.classifier.fit(X,y,**kwargs)
    
    def predict(self, row: Series, probabilities = False) -> float:
        """Predicts on a single row
        """
        warnings.filterwarnings("ignore", message="X does not have valid feature names, but LogisticRegression was fitted with feature names")
        row = row.drop('target')
        row = row.drop('Date')
        if probabilities:
            return self.classifier.predict_proba(row.to_numpy().reshape(1, -1))
        return self.classifier.predict(row.to_numpy().reshape(1, -1))
    
class ProbabilityThresholding(MachineLearningSignal):
    def __init__(self, model: MachineLearningModel, threshold: float = 0.5) -> None:
        self.model = model
        self.threshold = threshold
    
    def trade_signal(self, features: DataFrame, usd: float, btc: float) -> Signal:
        p = self.model.predict(features, probabilities=True)[0][1] # expects to deal with a model that can output probabilities
        if p > self.threshold:
            return Signal.BUY
        if p < (1 - self.threshold):
            return Signal.SELL
        return Signal.HOLD
        