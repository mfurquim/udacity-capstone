# Udacity Capstone

This repository is part of the final project for [Machine Learning Engineer Nanodegree](https://www.udacity.com/course/machine-learning-engineer-nanodegree--nd009t) from Udacity.

Build a stock price predictor for intraday trading.

The dataset used is the _Huge Stock Price Data: Intraday Minute Bar_ by [Möbius](https://www.kaggle.com/arashnic) which can be found at [kaggle](https://www.kaggle.com/datasets/arashnic/stock-data-intraday-minute-bar) and [github](https://github.com/FutureSharks/financial-data/tree/master/pyfinancialdata).

The data used to train the model will be the minute-by-minute data of stocks.
Among many others, the stocks can be:

```
$ tree -L 2 data/stocks
data/stocks/
\-- histdata/
    |-- ETXEUR/
    |-- GRXEUR/
    |-- JPXJPY/
    |-- SPXUSD/
    \-- README.md
```

Here is an example of the `EUR_USD`:

```python
import pyfinancialdata
data = pyfinancialdata.get(provider='oanda', instrument='EUR_USD', year=2017)
data.tail(3)
                       close     high      low     open  volume    price
date
2017-12-29 21:57:00  1.20045  1.20071  1.20004  1.20018      50  1.20045
2017-12-29 21:58:00  1.20041  1.20041  1.20041  1.20041       1  1.20041
2017-12-29 21:59:00  1.20039  1.20039  1.19970  1.20036      14  1.20039
```

There's a few potential solutions, such as **multiple linear regression**, **autoregressive integrated moving average (ARIMA)**, **Bayesian machine learning**, **random forest**, **LightGBM** and **CatBoost**, **convolutional neural network (CNN)**, **recurrent neural network (RNN)**, **generative adversarial networks (GAN)**, and **deep reinforcement learning**.
