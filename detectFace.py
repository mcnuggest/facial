from urllib import parse, request
import json
import base64
def returnFaceToken(name):
    __apiKey = "vbpAxnUsy0c1uGn-ABDdipKp0hX3tKVe"
    __apiSecret = "murHataUzWn_GHEAv6C16L7MJTgbwQKv"
    __detectApi = "https://api-cn.faceplusplus.com/facepp/v3/detect"

    __face1 = open(name, 'rb')
    __ls_f = base64.b64encode(__face1.read())
    __face1.close()

    __textmod = {"api_key": __apiKey, "api_secret": __apiSecret, "image_base64": __ls_f,
                 "return_attributes": "gender,smiling,beauty"}
    __textmod = parse.urlencode(__textmod).encode(encoding='utf-8')

    try:
        __req = request.Request(url=__detectApi, data=__textmod)
        __res = request.urlopen(__req)
        __res = __res.read()
        __res = __res.decode(encoding='utf-8')
        __resJson = json.loads(__res)
        if (__resJson['faces']):
            __face_token = __resJson['faces'][0]['face_token']
        else:
            __face_token = "don't have face"

    except:
        print("检测人脸失败，重新尝试")
        __face_token = "failed"
# res='{"image_id": "t+JQq9FEcwTH0fc4cCEbYA==", "request_id": "1512542943,31634c89-1da2-4b8a-b70c-343249b42e44", "time_used": 197, "faces": []}'




    return __face_token
