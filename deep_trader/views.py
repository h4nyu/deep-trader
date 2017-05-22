from deep_trader import app


@app.route('/')
def index():
    app.logger.debug('aaaa')
    return "this is deep trader."
