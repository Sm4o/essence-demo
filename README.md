# Essence Demo
Create an interface with a form and table viz with an API integration


**Functional/Technical requirements**:
- Testable Component Design/architecture
- Presentation and service logic layers (HTTP calls, app flow, shared data)
- SSO integration (preferably Google but others are fine)
> GitHub
- Providing the Authentication State Persistence
> Cookies
- Graph and tabular data viz with sorting, filtering, pagination
> Dash
- Page level authorisation
> flask_login
- Form handling with validation
- API integration (completely free to choose this to be any public API)
> https://api.alpaca.markets
- Unit and integration tests a minimum, with BDD tests using tools like Cypress would be good to see but not essential


Could do something like trends discovery


``` python
$ poetry run flask run
```

# TODO: Add static typing, and pre-commit hooks etc

# allowed users

styling with bulma: https://www.digitalocean.com/community/tutorials/how-to-add-authentication-to-your-app-with-flask-login

https://getbootstrap.com/docs/4.0/examples/cover/


## Alpaca Market Data API
Access real-time and up to 6+ years of historical equities & crypto data.

Check the [Market Data API reference](https://alpaca.markets/docs/api-references/market-data-api/)

Exchanges: CBSE, FTXU, ERSX

https://data.alpaca.markets/v1beta1/crypto


### Paging
https://alpaca.markets/docs/api-references/market-data-api/crypto-pricing-data/#paging


https://alpaca.markets/learn/code-cryptocurrency-live-trading-bot-python-alpaca/
``` python
from alpaca_trade_api.rest import REST, TimeFrame 
from dotenv import load_dotenv
load_dotenv()
api = REST()
api.get_crypto_bars("BTCUSD", TimeFrame.Minute).df
import plotly.graph_objects as go
fig = go.Figure(data=[
    go.Candlestick(
        x=df.index, 
        open=df['open'], 
        high=df['high'], 
        low=df['low'], 
        close=df['close'],
    )
])
fig.show()
```

Heroku deployment
Add GitHub Actions
Add Docker

Add filter by the exchange CBSE, FTXU and ERSX