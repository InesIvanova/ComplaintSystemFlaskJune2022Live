from config import create_app
from db import db

app = create_app()


@app.after_request
def return_resp(resp):
    db.session.commit()
    return resp


if __name__ == "__main__":
    app.run()
