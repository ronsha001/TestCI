from flask import Flask, request, Response


app = Flask(__name__)

@app.route('/webhook', methods=['GET', 'POST'])
def health():
  if request.method == 'POST':
    print (request.data)
    return Response("This was a POST request", status=200)
  elif request.method == 'GET':
    return Response("This was a GET request", status=200)

  return Response("Error", status=500)


if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port='8082')