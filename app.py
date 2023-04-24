from flask import Flask
import os
import estimations

env_config = os.environ.get("FLASK_CONFIG","config.DevelopmentConfig")

app = Flask(__name__)

app.config.from_object(env_config)

print(f"Environment: {app.config['ENV']}")
print(f"Debug: {app.config['DEBUG']}")
print(f"Testing: {app.config['TESTING']}")

estimations.init_estimations(app)

if __name__ == '__main__':
    app.run(debug = app.config['DEBUG'])
