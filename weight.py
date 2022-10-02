from flask import Flask, request, Response


app = Flask(__name__)

@app.route('/health')
def health():
  return Response("OK", status=200)


if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')
