from flask import Flask, render_template, request
import os

app = Flask(__name__, static_folder="static")


@app.route("/")
def index():
    video_dir = "static/videos"
    video_list = os.listdir(video_dir)

    for i in range(len(video_list)):
        video_list[i] = os.path.join("videos", video_list[i])

    return render_template("index.html", video_list=video_list)


@app.route("/player")
def player():
    video_path = request.args.get("vidpath")
    # may be here urlfor
    return render_template("player.html", video_path=video_path)


if __name__ == "__main__":
    app.run(debug=True)
