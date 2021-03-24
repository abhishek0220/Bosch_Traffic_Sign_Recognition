import os
os.environ['Bosch'] = os.path.join(os.getcwd(), 'Bosch')
os.environ['FLASK_ENV']="development"
from Bosch import app
if __name__ == "__main__" :
    app.run(debug=True)