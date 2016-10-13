from flask import Flask,request
from WXBizMsgCrypt import WXBizMsgCrypt

app = Flask(__name__)

@app.route('/geturl',methods=['GET'])
def getUrl():
    sCorpID = "wxf29b16f0c55ae5f2"
    sToken = "wzgyXSnxoKNDRb5yoJVtLk4XNkXbKRFm"
    sEncodingAESKey = "7fJlKWPElDjOtXbYkpkLAeac6eVAuUrrYM2dBWeHvlt"
    wxcpt = WXBizMsgCrypt(sToken,sEncodingAESKey,sCorpID)
    params = request.args.items()
    sVerMsgSig = params['msg_signature']
    sVerMsgTimeStap = params['timestamp']
    sVerNonce= params['nonce']
    sVerEchoStr = params['echostr']
    ret,sEchoStr = wxcpt.VerifyURL(sVerMsgSig,sVerMsgTimeStap,sVerNonce,sVerEchoStr)
    if ret!=0:
        print "ERROR:"+ret
        return None
    else:
        return sEchoStr

@app.route('/')
def index():
    return '<h1>Hello,Qian!</h1>'

if __name__=='__main__':
    app.debug = True
    app.run()