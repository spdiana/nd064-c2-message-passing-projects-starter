import os
import logging

from app import create_app

app = create_app(os.getenv("FLASK_ENV") or "test")
if __name__ == "__main__":
    app.run(debug=True)


# start the application on port 3111
if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', filename='app.log', level=logging.DEBUG)
    app.run(host='0.0.0.0', port='3113', debug = True)