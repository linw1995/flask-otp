"""
flask-otp
-------------

One-Time Password extension to Flask
"""
from setuptools import setup


setup(
    name='flask-otp',
    version='1.0',
    url='https://github.com/linw1995/flask-otp',
    license='MIT',
    author='linw',
    author_email='linw1995@icloud.com',
    description='One-Time Password extension to Flask',
    long_description=__doc__,
    py_modules=['flask_otp'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask',
        "pyotp",
        "qrcode"
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)