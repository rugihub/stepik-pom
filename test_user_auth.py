import pytest
import requests

class TestUserAuth:
    
    def setup(self):
        url = "https://playground.learnqa.ru/api/user/login"
        data = {'email': 'vinkotov@example.com',
                'password': '1234'}

        res1 = requests.post(url, data=data)

        assert 'auth_sid' in res1.cookies, "No auth cookie in response"
        assert 'x-csrf-token' in res1.headers, "No CSRF token header in response"
        assert 'user_id' in res1.json(), "No user_id in response"

        self.auth_sid = res1.cookies.get('auth_sid')
        self.token = res1.headers.get('x-csrf-token')
        self.user_id_from_auth_method = res1.json()['user_id']


    def test_auth_user(self):

        res2 = requests.get(
            "https://playground.learnqa.ru/api/user/auth",
            headers = {"'x-csrf-token":self.token},
            cookies = {"auth_sid":self.auth_sid}
        )

        assert 'user_id' in res2.json(), "No user_id in 2nd response"
        user_id_from_check_method = res2.json()['user_id']
        #print(user_id_from_check_method)

        assert self.user_id_from_auth_method == user_id_from_check_method, \
                "User_id not equal"


    excl_params = [("no cookie"), ("no token")]

    @pytest.mark.parametrize('cond', excl_params)
    def test_neg_auth_check(self, cond):

        if cond == "no cookie":
            res2 = requests.get(
                "https://playground.learnqa.ru/api/user/auth",
                headers = {"'x-csrf-token": self.token}
            )
        else:
            res2 = requests.get(
                "https://playground.learnqa.ru/api/user/auth",
                cookies = {"auth_sid":self.auth_sid}
            )

        assert 'user_id' in res2.json(), "No user_id in 1st response"
        
        user_id_from_check_method = res2.json()['user_id']

        assert user_id_from_check_method == 0, f"User not authorized via {cond}"