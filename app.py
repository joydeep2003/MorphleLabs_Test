from flask import Flask
import psutil
import getpass
import datetime
import pytz
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    username = getpass.getuser()
    
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S %Z')
    
    try:
        top_output = subprocess.check_output(['top', '-b', '-n', '1']).decode('utf-8')
    except:
        top_output = "Could not fetch top output"
    
    html_content = f"""
    <html>
        <body style='background-color: #1a1a1a; color: #ffffff; font-family: monospace;'>
            <pre>
Name: Claude (Anthropic AI Assistant)
Username: {username}
Server Time (IST): {server_time}

TOP Output:
{top_output}
            </pre>
        </body>
    </html>
    """
    
    return html_content

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)