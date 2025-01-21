from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/hello')
def hello():
    return "hello flask test"

if __name__ == "__main__":
    print("Starting Python Flask Server For Grocery Store Management System")
    app.run(port=5000)

    """ you will see this output given below:
    
    * Serving Flask app 'server'
    * Debug mode: off
    WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
    * Running on http://127.0.0.1:5000
    
    -> copy this url on your browser, and add /hello at the end of the url. 
    UI will be started and you will see "hello flask test" page.
    
    """