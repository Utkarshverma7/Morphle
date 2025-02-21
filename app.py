from flask import Flask
import subprocess
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Get system username
    username = subprocess.run(['whoami'], capture_output=True, text=True).stdout.strip()

    # Get server time in IST
    ist_time = datetime.now(pytz.timezone('Asia/Kolkata')).strftime('%Y-%m-%d %H:%M:%S')

    # Get top output
    top_output = subprocess.run(['top', '-b', '-n', '1'], capture_output=True, text=True).stdout

    # Prepare the response
    response = f"""
    <pre>
    Name - Utkarsh Verma
    Username - {username}
    Server Time in IST - {ist_time}
    Top Output:
    {top_output}
    </pre>
    """
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
