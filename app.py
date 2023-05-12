import requests
from flask import Flask, redirect, request

app = Flask(__name__)

@app.route("/oauth2/kakao/callback/")
def auth():
    code = request.args.get('code')
    state = request.args.get('state')
    error = request.args.get('error')
    error_description = request.args.get('error_description')
    # print(f"{code}, {state}, {error}, {error_description}")

    res = requests.post(
        "https://kauth.kakao.com/oauth/token",
        data={
            "grant_type": "authorization_code",
            "client_id": "576378062e928e8231bd946cc7d65013",
            "redirect_uri": "http://localhost:5000/oauth2/kakao/callback/",
            "code": code,
            "client_secret" : "Lj4ZwM3Sk2kynWrfS7I7xyTwJBDy5HFF"
        },
    )
    access_token = res.json()["access_token"]
    # print(access_token)

    res = requests.post(
        "https://kapi.kakao.com/v2/user/me",
        headers={"Authorization": f"Bearer {access_token}"}
    )
    # print(res.json())
    print(f'{res.json()["properties"]["nickname"]}님이 로그인했습니다.')
    return "반갑습니다 !"

if __name__ == '__main__':
    app.run()