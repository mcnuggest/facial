from urllib import parse, request
import json
import base64

def compareFace(a,b):
    apiKey = "vbpAxnUsy0c1uGn-ABDdipKp0hX3tKVe"
    apiSecret = "murHataUzWn_GHEAv6C16L7MJTgbwQKv"
    compareApi = "https://api-cn.faceplusplus.com/facepp/v3/compare"

    textmod = {"api_key": apiKey, "api_secret": apiSecret, "face_token1": a,"face_token2":b}
    textmod = parse.urlencode(textmod).encode(encoding='utf-8')

    print(textmod)

    try:
        req = request.Request(url=compareApi, data=textmod)
        res = request.urlopen(req)
        res = res.read()
        res = res.decode(encoding='utf-8')
        print(res)
        resJson = json.loads(res)
        if (resJson['confidence']):
            face_token = resJson['confidence']
        else:
            face_token = "don't have value"

    except:
        print("比对人脸失败，重新尝试")
        face_token = "failed"
    print(face_token)
    return 0