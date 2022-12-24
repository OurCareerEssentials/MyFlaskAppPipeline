'''
Flask App
'''
from flask import Flask
from flask_restful import Api  
from handlers.routes import configure_routes
from handlers.api import sampleAPI  

app = Flask(__name__)
api = Api(app)

api.add_resource(sampleAPI,'/api/test')
configure_routes(app)

if __name__ == '__main__':    
    app.run(host="0.0.0.0", port="3000")