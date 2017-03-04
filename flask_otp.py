import qrcode
import pyotp
from io import BytesIO
from flask import current_app

__author__ = "linw"


class OTP:
    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        if self.app is None:
            self.app = app

    @staticmethod
    def get_key():
        """
        returns a 16 character base32 secret.
        Compatible with Google Authenticator
        """
        return pyotp.random_base32()

    @staticmethod
    def authenticate(key, otp):
        """
        verify the One-Time password with key
        """
        p = 0
        try:
            p = int(otp)
        except:
            return False
        t = pyotp.TOTP(key)
        return t.verify(p)

    @staticmethod
    def qr(key):
        """
        get qrcode image bytes
        >>>from flask_otp import OTP
        >>>otp = OTP.init_app(app)
        >>>img = otp.qr(key) # bytesIO
        >>># to file
        >>>with open("filename.png", "wb") as f:
        >>>    f.write(img.read())
        >>># flask send file
        >>>from flask import send_file
        >>>@app.route("/")
        >>>def qr():
        >>>    return send_file(img, mimetype="image/png")
        """
        t = pyotp.TOTP(key)
        uri = t.provisioning_uri(current_app.config["DOMAIN"] or "")
        q = qrcode.make(uri)
        img = BytesIO()
        q.save(img, 'PNG')
        img.seek(0)
        return img
