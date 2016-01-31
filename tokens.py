#coding: utf-8
import requests
import os
import json
import time
import sys

api_base="https://api.weixin.qq.com/cgi-bin/"
class AccessToken:

    def get_url(self, **kwargs):
        url = api_base + 'token' #TODO, auto chop, and include other type of url
        i = 0
        for k,v in kwargs.iteritems():
            if i == 0:
                url += '?'
            else:
                url += '&'

            url += "%s=%s" % (k, v)
            i += 1 # buggy
        return url

    def token_expired(self, obj):
        expire = float(obj['update_time']) + float(obj['expires_in'])
        return expire < time.time()

    def request_token(self, appid, secret, filename):
        req_url = self.get_url(
            grant_type='client_credential',
            appid=appid,
            secret=secret)
        self.resp = requests.get(req_url)
        obj = json.loads(self.resp.text)
        obj["update_time"] = time.time()
        self.token_save(obj, filename)

    def get_access_token(self, appid, secret, filename):
        obj = self.token_load(filename)
        #self.assertTrue(obj != None)
        if obj and not self.token_expired(obj):
            return obj
        else:
            return self.request_token(appid, secret, filename)

    def token_save(self, obj, filename):
        fp = open(filename, "wb")
        json.dump(obj, fp)
        fp.close()

    def token_load(self, filename):
        fp = None
        try:
            fp = open(filename, "rb")
            obj = json.load(fp)
            fp.close()
            return obj
        except IOError as e: #TODO: fix error judge output
            print "fail:", e
        finally:
            print "ok"
            #return obj
