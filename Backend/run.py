from app import app

HOST = '0.0.0.0'

print(f"Starting Flask app at: http://{HOST}:{5013}")
app.run(host=HOST, port=5013, debug=True)

