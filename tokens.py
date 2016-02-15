# coding: utf-8
import requests
import os
import json
import time
import sys

# TODO: take appid, secret, filename to a template or config file
# func argument from template func

api_base = "https://api.weixin.qq.com/cgi-bin/"


class AccessToken:
    def __init__(self):
        pass

    @staticmethod
    def get_url(**kwargs):
        url = api_base + 'token'  # TODO, auto chop, and include other type of url
        i = 0
        for k, v in kwargs.iteritems():
            if i == 0:
                url += '?'
            else:
                url += '&'

            url += "%s=%s" % (k, v)
            i += 1  # buggy
        return url

    @staticmethod
    def token_expired(obj):
        if not (obj.has_key("update_time") and obj.has_key("expires_in")):
            return True #expired
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
        # self.assertTrue(obj != None)
        if obj and not self.token_expired(obj):
            return obj
        else:
            return self.request_token(appid, secret, filename)

    @staticmethod
    def token_save(obj, filename):
        fp = open(filename, "wb")
        json.dump(obj, fp)
        fp.close()

    @staticmethod
    def token_load(filename):
        fp = None
        try:
            fp = open(filename, "rb")
            obj = json.load(fp)
            fp.close()
            return obj
        except IOError as e:  # TODO: fix error judge output
            # return e.error
            # print("I/O error({0}): {1}".format(e.errno, e.strerror)
            print("fail:", e.message)
        finally:
            print("ok")
            # return obj
