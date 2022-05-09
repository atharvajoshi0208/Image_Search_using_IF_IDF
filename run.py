from distutils.log import debug
from imp import reload
from flask import Flask, render_template
from code_flask import app


if __name__ == '__main__':
    app.run(debug=True)
