# coding: utf-8
import unittest
import tokens


class AccessTokensTest(unittest.TestCase):
    def test_get_access_token(self):
        tokenfile = "token6.json"
        obj = tokens.AccessToken()
        token = obj.get_access_token(
            appid="",  # fill
            secret="",  # fill
            filename=tokenfile
        )
        obj2 = tokens.AccessToken()
        token2 = obj2.token_load("token.json")
        print obj2
        self.assertNotEqual(token, token2)

        obj3 = tokens.AccessToken()
        token3 = obj3.token_load("token6.json")
        print obj3
        self.assertEqual(token, token3)

if __name__ == '__main__':
    unittest.main()
