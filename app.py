from flask import Flask, render_template
import configcatclient

app = Flask(__name__)

configcat_client = configcatclient.create_client('YOUR_CONFIGCAT_SDK_KEY')

@app.route("/")
def index():
    canShowCopiesSold = configcat_client.get_value('canshowcopiessold', False)
    return render_template('index.html', canShowCopiesSold=canShowCopiesSold)