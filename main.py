from flask import Flask

app = Flask(__name__)


@app.route('/cheque/qr', methods = ['POST'])
def hello(request):
    # t=20190513T211700&s=225900.00&fn=9284000100164824&i=2123&fp=3664895564&n=1
    if request.method == 'POST':
        data = request.POST
        print(data.get("t"), data.get("s"), data.get("fn"), data.get("i"), data.get("fp"), data.get("n"))

    return 'Hello, World!'
