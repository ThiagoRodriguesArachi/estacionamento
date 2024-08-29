from flask import Flask, render_template, send_from_directory
import subprocess
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_stream')
def start_stream():
    output_dir = "static/hls"
    os.makedirs(output_dir, exist_ok=True)
    
    # Comando para iniciar o FFmpeg
    ffmpeg_cmd = [
        'ffmpeg',
        '-rtsp_transport', 'tcp',
        '-i', 'rtsp://admin:Pb33227862@alprprime.ddns-intelbras.com.br/cam/realmonitor?channel=1&subtype=0&unicast=true',
        '-c:v', 'libx264',
        '-hls_time', '10',
        '-hls_list_size', '6',
        '-hls_flags', 'delete_segments+append_list',
        '-f', 'hls', os.path.join(output_dir, 'output.m3u8')
    ]
    
    subprocess.Popen(ffmpeg_cmd)
    return "Streaming iniciado!"

@app.route('/stream/<path:filename>')
def stream(filename):
    return send_from_directory('static/hls', filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)