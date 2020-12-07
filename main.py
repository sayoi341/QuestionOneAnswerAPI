from flask import Flask, request, json, jsonify
from flask.helpers import safe_join
app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False

dics = {
    '1' : '国語期末'
}

@app.route('/hello', methods=['GET'])
def hello():
    return jsonify({'message': 'hello'})

@app.route('/dics', methods=['GET'])
def allDics():
    return jsonify(dics)

@app.route('/dics', methods=['POST'])
def createDic():
    dicID = str(int(max(dics.keys())) + 1)
    posted = request.get_json()

    if 'dic' in posted:
        dics[dicID] = posted['dic']
        msg = 'new Dictionary created!'
    else:
        msg = 'no Dictionary created'

    json = {
        'message' : msg
    }
    return jsonify(json)

@app.route('/dics/<int:dicID>', methods=['DELETE'])
def deleteDic(dicID):
    dicID = str(dicID)

    if dicID in dics:
        msg = 'Dictionary {} deleted'.format(dics[dicID])
        del dics[dicID]
    else:
        msg = '{0} is not in Dictionary'.format(dicID)

    json = {
        'message' : msg
    }

    return jsonify(json)

@app.route('/dics/<int:dicID>', methods=['PUT'])
def updateDic(dicID):
    dicID = str(dicID)
    posted = request.get_json()

    if 'dic' in posted and dicID in dics:
        dics[dicID] = posted['dic']
        msg = 'Dictionary {} is changed!'.format(dicID)
    else:
        msg = 'No Dictionary updated'

    json = {
        'message' : msg
    }

    return jsonify(json)

