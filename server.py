import json
import jsonschema

from flask import Flask, request, jsonify
from flask_jsonschema_validator import JSONSchemaValidator

import controller.cool as cool_controller
import controller.hot as hot_controller
import controller.dehumidify as dehumidify_controller
import controller.off as off_controller

app = Flask(__name__)
JSONSchemaValidator(
    app = app,
    root = "schemas"
)
ok = {
    'message': 'ok',
    'code': 200
}   

def error_response(e) -> dict:
    code = 400
    res = {
        'code': code,
        'error': e.error,
        'message': e.message,
    }
    return jsonify(res), 400

@app.errorhandler(jsonschema.ValidationError)
def onValidationError(e):
    res = {
        'code': 400,
        'error': e.__class__.__name__,
        'message': 'Validation error: ' + str(e),
    }
    return jsonify(res), 400

@app.route('/')
def index():
    with open('./public/index.html') as f:
        html = f.read()
    return html

@app.route('/ping')
def ping(): return jsonify(ok), 200

@app.route('/on/cool', methods=['PUT'])
@app.validate('controller', 'cool')
def cool():
    try: cool_controller.cool(request.json)
    except Exception as e: return error_response(e)
    return jsonify(ok), 200

@app.route('/on/hot', methods=['PUT'])
@app.validate('controller', 'hot')
def hot():
    try: hot_controller.hot(request.json)
    except Exception as e: return error_response(e)
    return jsonify(ok), 200

@app.route('/on/dehumidify', methods=['PUT'])
@app.validate('controller', 'dehumidify')
def dehumidify():
    try: dehumidify_controller.dehumidify(request.json)
    except Exception as e: return error_response(e)
    return jsonify(ok), 200

@app.route('/off', methods=['DELETE'])
def off():
    try: off_controller.off()
    except Exception as e: return error_response(e)
    return jsonify(ok), 200

def main():
    PORT = 40001
    app.run(debug=True, host='0.0.0.0', port=PORT)

if __name__ == '__main__':
    main()
