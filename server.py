from flask import Flask, request, jsonify
from yt_dlp import YoutubeDL

app = Flask(__name__)

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('q')
    ydl_opts = {
        'format': 'bestaudio/best',
        'noplaylist': True,
        'quiet': True
    }

    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(f"ytsearch1:{query}", download=False)['entries'][0]
        return jsonify({
            'title': info['title'],
            'url': info['url'],
            'webpage_url': info['webpage_url'],
            'thumbnail': info.get('thumbnail'),
            'audio_url': info['url']
        })

@app.route('/')
def root():
    return "Servidor yt-dlp está online."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
