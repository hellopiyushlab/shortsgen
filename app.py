from modules.summarizer import summarize_article
from modules.text_to_speech import text_to_speech_files
from modules.movie_maker import create_video

from flask import Flask, render_template, request, Response, redirect, url_for, send_file

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route("/")
def index():
    return render_template("mijikai.html")

@app.route("/download_video")
def download_video():
    video_path = "./static/output-videos/output_video.mp4"
    return send_file(video_path, as_attachment=True)

@app.route("/download")
def download():
    video_path = request.args.get("video_path", "./output-videos/output_video.mp4")  
    return render_template("download.html", video_path=video_path)


@app.route("/generate", methods=["POST"])
def generate():

    def gen(article):
        update = "Processing..."
        yield f"{update} \n\n"

        summarized_article, summarized_article_list_of_sentences = summarize_article(article)
        print()
        print(summarized_article_list_of_sentences)
        print()

        update = "Summary generated!\n\nGenerating TTS clips..."
        yield f"{update} \n\n"

        saved_audio_files = text_to_speech_files(summarized_article_list_of_sentences)
        print("Audio files saved at the following locations:")
        for file_path in saved_audio_files:
            print(file_path)

        update = "TTS clips generated!\n\nProcessing final video..."
        yield f"{update} \n\n"

        create_video(summarized_article_list_of_sentences, saved_audio_files)

        update = "Video Generated!\n\nClick the download button!"
        yield f"{update} \n\n"

        # Redirection code
        
    data = request.json
    article = data['text']
    
    print("CALLING RESPONSE")
    
    return Response(gen(article), mimetype='text/event-stream')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
