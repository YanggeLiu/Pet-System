from flask import Flask, request, session, g, redirect, url_for, abort, \
    render_template, flash, Response
import threading
import os
import sqlite3
import cv2
import cam
import control
from flask_cors import CORS
from instance import config
app = Flask(__name__, instance_relative_config=True)

app.config.from_object(config)

CORS(app)


def connect_db():
    return sqlite3.connect(app.config['DB_URL'])


def get_connection():
    db = getattr(g, '_db', None)
    if db is None:
        db = g._db = connect_db()
    return db


def query_db(query, args=(), one=False):
    db = get_connection()
    cur = db.execute(query, args)
    rv = [dict((cur.description[idx][0], value)
               for idx, value in enumerate(row)) for row in cur.fetchall()]
    return (rv[0] if rv else None) if one else rv


@app.route('/go_cam')
def go_cam():
    return Response(cam.generate(), mimetype='multipart/x-mixed-replace;boundary=frame')


@app.route('/create_angle', methods=['POST'])
def create_angle():
    Response_re = None
    if request.method == 'POST':
        data = request.get_json(silent=True)
        position_name = data['position_name']
        col = data['col']
        row = data['row']
        db = get_connection()
        db.execute("insert into angle (POSITION,COL,ROW)values(?,?,?)",
                   [position_name, col, row])
        db.commit()
        db.close()
        Response_re = "creata success!"
    return Response_re


@app.route('/get_angle', methods=['GET'])
def get_angle():
    i = 0
    all_angle = []
    res_all_angle = {}
    if request.method == 'GET':
        for angle in query_db('select POSITION from angle'):
            all_angle.append(angle['POSITION'])
        print(all_angle)
        res_all_angle['all_angle'] = all_angle
    return res_all_angle


@app.route('/move_angle', methods=['POST'])
def move_angle():
    re = None
    if request.method == 'POST':
        position = request.get_json(silent=True)
        position = position['angle_name']
        check_angle = query_db(
            "select COL,ROW from angle where POSITION = ?", [position], one=True)
        control.control_col(check_angle['COL'])
        control.control_row(check_angle['ROW'])
        re = 'moved'
    return re


@app.route('/remove_angle', methods=['POST'])
def remove_angle():
    re = None
    if request.method == 'POST':
        remove_angle = request.get_json(silent=True)
        remove_angle = remove_angle['remove']
        db = get_connection()
        db.execute('delete from angle where POSITION = ?', [remove_angle])
        db.commit()
        db.close()
        re = 'removed'
    return re


@app.route('/col', methods=['POST'])
def col():
    if request.method == 'POST':
        col = request.get_json(silent=True)
        print(col['col'])
        control.control_col(col['col'])
    return 'this is col'


@app.route('/row', methods=['POST'])
def row():
    if request.method == 'POST':
        row = request.get_json(silent=True)
        print(row['row'])
        control.control_row(row['row'])
    return 'this is row'


@app.route('/login', methods=['POST'])
def login():
    Response_re = None
    if request.method == 'POST':
        from_login = request.get_json(silent=True)
        account = from_login['account']
        pwd = from_login['password']
        check_pwd = query_db('select NAME,PWD from Users where ID = ?', [
            account], one=True)
        if check_pwd is None:
            Response_re = 'No such user'
        elif pwd != check_pwd['PWD']:
            Response_re = 'pwd is wrong'
        else:
            Response_re = {'info': 'success!', 'user': check_pwd['NAME']}
    return Response_re


@app.route('/v_mode', methods=['POST'])
def v_mode():
    Response_re = None
    db = get_connection()
    if request.method == 'POST':
        v_id = request.get_json(silent=True)
        v_id = v_id['status']
        if v_id == '1' or v_id == '0':
            db.execute(
                "update setting_status set status = ? where setting_name = 'vision_mode'", [v_id])
            db.commit()
            db.close()
            cam.vision_mode(v_id)
            Response_re = 'changed'
    return Response_re


@app.route('/check_status', methods=['GET'])
def check_status():
    re = None
    if request.method == 'GET':
        status = query_db(
            "select status from setting_status where setting_name = 'vision_mode'", one=True)
        re = {'info': 'success', "status": status['status']}
    return re


@app.route('/reboot', methods=['GET'])
def reboot():
    if request.method == 'GET':
        os.system('sudo reboot')


@app.route('/relink', methods=['GET'])
def relink():
    re = None
    if request.method == 'GET':
        re = 'relink'
    return re


'''
@app.route('/for_test')
def index():
    return render_template('cam.html')
'''

if __name__ == '__main__':
    t = threading.Thread(target=cam.detect_motion)
    t.daemon = True
    t.start()
    app.run(host=app.config['HOST'], threaded=app.config['THREADED'],
            use_reloader=app.config['USE_RELOADER'])
