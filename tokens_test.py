#coding: utf-8
import unittest
import tokens

class AccessTokens(unittest.TestCase):

    def test_get_access_token(self):
        tokenfile = "token9.json"
        obj = tokens.AccessToken()
        obj.get_access_token(
               appid="",    #fill
               secret="",   #fill
               filename=tokenfile
               )
        obj2 = tokens.AccessToken()
        obj2.token_load("token.json")
        print obj2
        self.assertNotEqual(obj, obj2)


if __name__ == '__main__':
    unittest.main()
