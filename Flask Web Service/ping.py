from flask import Flask

app = Flask(__name__)


@app.route('/ping', methods=['GET'])
def ping():
    return 'pong'

def main():
    app.run(debug=True, port=8080)

if __name__ == '__main__':
    main()
