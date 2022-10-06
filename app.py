from flask import Flask, render_template, request
import configcatclient

from ampli import *


ampli.load(LoadOptions(
  environment=Environment.PRODUCTION
))

app = Flask(__name__)

configcat_client = configcatclient.create_client('YOUR_CONFIGCAT_SDK_KEY')

@app.route("/", methods=('GET', 'POST'))
def index():
    canShowCopiesSold = configcat_client.get_value('canshowcopiessold', False)

    if request.method == 'POST':
        ampli.book_purchase(user_id='user@exampled.com')

    return render_template('index.html', canShowCopiesSold=canShowCopiesSold)