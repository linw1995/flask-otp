from flask import Flask, session, send_file
from flask_otp import OTP

app = Flask(__name__)
otp = OTP()
otp.init_app(app)

app.config["SECRET_KEY"] = "something"
app.config["DOMAIN"] = "www.XXX.com"


@app.route('/qr')
def qr():
    """
    Return a QR code for the secret key
    The QR code is returned as file with MIME type image/png.
    """
    if session.get("OTPKEY", True):
        # returns a 16 character base32 secret.
        # Compatible with Google Authenticator
        session["OTPKEY"] = otp.get_key()
    img = otp.qr(session["OTPKEY"])
    return send_file(img, mimetype="image/png")


@app.route('/verify/<string:password>')
def verify(password):
    """
    verify the One-Time Password
    """
    return str(otp.authenticate(session["OTPKEY"], password))

if __name__ == '__main__':
    app.run()