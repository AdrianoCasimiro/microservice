from flask import Flask
from flask import request
from flask import jsonify
from rabbitmq.send import send_sensor

app = Flask(__name__)


@app.route('/sensors', methods=['GET', 'POST'])
def sensors():
    sensor = request.args.get('sensor')
    temperature = request.args.get('temperature')
    huminity = request.args.get('huminity')

    send_sensor(sensor, temperature, huminity)

    return jsonify({'Sensor': sensor}), 201


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
