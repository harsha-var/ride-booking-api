from flask import Flask,jsonify
app = Flask(__name__)
@app.route('/book-ride',methods=['GET'])
def book_ride():
  return jsonify({"ride_id":123,"ride-name":"sparkle","status":"confirmed"})

if __name__ == '__main__':
  app.run(host='0.0.0.0',port=3000)
