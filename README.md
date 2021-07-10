# Paper-Trading-
This is an algorithmic paper trading bot that uses the following APIs: Alpaca, financialmodelingprep, yahoofinance. With these tools and use of deep learning, we can create an intelligent trading bot that can automate trades in the market. For testing purposes we will trade paper money. 


## Development
Steps to run locally:  

0. create an alpaca account and generate api keys (secret and reg)
1. clone the repo into a local directory using ```git clone https://github.com/ZacharyJWyman/Algorithmic-Trading-.git```
2. Create a config.py file using the terminal by ```touch config.py``` and create variables ```API_KEY = 'key' & API_SECRET_KEY = 'secret_key'``` within config.py file. You can use notepad for this step.
3. cd in master directory and create a virtual env using ```virtualenv venv```
4. cd into virtual environment ```cd venv``` and then instantiate using ```.\Scripts\activate``` (Windows activation)
5. navigate to directory where requirements.txt is located while virtualenv is activate and install dependencies ```pip install -r requirements.txt```
6. to run GUI ```python gui.py``` in the terminal.

### Current:
Currently the bot is linked to a paper trading account and can make paper trades when the market is open. There is also a fully functional GUI that incorporates a deep learning model to predict stock prices. The GUI can make trades for you and store past orders as well as fetch current stock price and predicted price for stocks publicly traded in the U.S. 
  
### What comes next?
* Integrate future forecasting (10-Day & 30-Day) periods. 
* Flag buy and sell periods with model for smart trading. 
* Create a more robust model (ideas: stock sentiment (news), seasonality trends). 

## Using the GUI
[![Video](http://img.youtube.com/vi/KdWSMBeIFdk/0.jpg)](https://youtu.be/KdWSMBeIFdk)
  
## Author
Created by *Zachary Wyman*
