from flask import Flask, render_template, request, make_response, g

import os
import socket
import random
import json
import logging

hostname = socket.gethostname()

app = Flask(__name__)

#modification-3 

@app.route("/", methods=['POST','GET'])
def hello():
    

    resp = make_response(render_template(
        'index.html',
        option_a=option_a,
        option_b=option_b,
        hostname=hostname,
       
    ))
   
    return resp


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3900, debug=True, threaded=True)