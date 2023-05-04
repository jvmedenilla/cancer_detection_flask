import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or b'\x9c\xfb&\x9b\x1cS\x87\xed\x9e\x12\xaeA\xd9\x15\x106'