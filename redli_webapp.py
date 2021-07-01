from flask import Flask, render_template, request
import requests
#Coded by JAYAKUMAR - JTECHCODE 2.O
#Subscribe https://www.youtube.com/channel/UC_2ln7CZ7XjSpGDMgzsBjQA
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/helpline')
def help():
    return render_template('help.html')

@app.route('/track', methods=['POST'])
def track():
    if request.method == 'POST':
        url = request.form['user_url']
        resp = requests.get(url)
        redirect_ulr = resp.history
        return render_template('track.html', endurl = resp, redirect = redirect_ulr)

if __name__=='__main__':
    app.run(debug=True)
