import pandas as pd
import matplotlib.pyplot as plt
from source.models.central_model import TradingModel
from typing import Literal
from source.models.central_model import PRICE_COLUMN


class BacktestTradeModels():
    def __init__(self,csv: str | pd.DataFrame, start_date = None, end_date = None):
        if isinstance(csv,str):
            self.data = pd.read_csv(csv)
        else:
            self.data = csv
        if start_date:
            self.data = self.data[self.data['Date'] >= start_date]
        if end_date:
            self.data = self.data[self.data['Date'] <= end_date]
    
    def __call__(self, model: TradingModel, plot: Literal['complete','signal','usd','btc','none']='complete') -> float:
        """Evaluates the model, and optionally plots model decision and currency evolution
        """
        signals = []
        usds = []
        btcs = []
        for _,row in self.data.iterrows():
            print(row)
            signals.append(model(row))
            usds.append(model.usd)
            btcs.append(model.btc)
        if plot == 'complete' or plot == 'signal':
            self.plot_signals(signals)
        if plot == 'complete' or plot == 'usd':
            self.plot_funds(usds,currency='USD')
        if plot == 'complete' or plot == 'btc':
            self.plot_funds(usds,currency='BTC')
        return self.compute_profit(model)

    def compute_profit(self, model: TradingModel) -> float:
        return model.usd + model.btc*self.data[PRICE_COLUMN][-1] # Cash + btc at last price
    
    def plot_signals(self, signals: list) -> None:
        for i,signal in enumerate(signals):
            mark = ['.','^','v'][signal]
            color = ['gray','green','red'][signal]
            plt.title("Buy or Sell Signals")
            plt.plot(i,self.data['Open'][i],color=color,marker=mark)
        plt.figure()
    
    def plot_funds(self,funds: list, currency: str) -> None:
        plt.title(f"Evolution of {currency}")
        plt.plot(funds)
        plt.figure()
