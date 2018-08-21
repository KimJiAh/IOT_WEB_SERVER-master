from flask import Flask, render_template, Response, request
from flask_cors import CORS
import os
from flask_socketio import SocketIO, emit

#메시징코드
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
#cors = CORS(app, resources={r"/*": {"origins": "http://121.129.2.195:8080"}})
CORS(app)

# https://flask-socketio.readthedocs.io/en/latest/
# https://github.com/socketio/socket.io-client

app = Flask(__name__)

app.config[ 'SECRET_KEY' ] = 'jsbcfsbfjefebw237u3gdbdc'
socketio = SocketIO( app )

@app.route( '/' )
def hello():
  return render_template( './메시징.html' )
#요기까지

def messageRecived():
  print( 'message was received!!!' )

@socketio.on( 'my event' )
def handle_my_custom_event( json ):
  print( 'recived my event: ' + str( json ) )
  socketio.emit( 'my response', json, callback=messageRecived )

#게시판 목록
@app.route( '/Board_List' )
def list():
  return render_template( './게시판 목록.html' )

@app.route( '/Board_Delete' )
def delete():
  return render_template( './Board_Delete.html' )

@app.route( '/Board_View' )
def view():
  return render_template( './게시판 내용.html' )

@app.route( '/Board_Reply' )
def reply():
  return render_template( './Board_Reply.html' )

@app.route( '/Board_Reply_action' )
def reply_action():
  return render_template( './Board_Reply_action.html' )

@app.route( '/Board_Update' )
def update():
  return render_template( './Board_Update.html' )

@app.route( '/Board_Write' )
def write():
  return render_template( './글쓰기.html' )

@app.route( '/Board_Write_action' )
def write_action():
  return render_template( './Board_Write_action.jsp' )








# No caching at all for API endpoints.
@app.after_request
def add_header(response):
    # response.cache_control.no_store = True
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '-1'
    return response

@app.route('/streaming')
def index():
    return render_template('스트리밍.html')

@app.route('/map')
def location():
    return render_template('지도.html')

@app.route('/jiah')
def jiah():
    return render_template('시작화면.html')



@app.route('/message')
def jiah3():
    return render_template('message.html')

@app.route('/path')
def path():
    return render_template('path.html')

@app.route('/test', methods=["POST"])
def test():
    print(request.data)
    json = request.form
    file = request.files['abc']
    filename = file.filename
    file.save('/Users/sunghyeok/video_streaming/static/pic.jpg')
    print(json)
    print(file)
    #print(json)
    data = {
        'status': 200
    }
    #js = json.dumps(data)
    return Response(status=200, mimetype='application/json')

if __name__ == '__main__':
    socketio.run(app, debug=True)
    app.run(host='0.0.0.0', debug=True)
