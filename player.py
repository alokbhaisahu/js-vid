#!/usr/bin/env python
"""
Author: Alok Bhai Sahu
Purpose: A video player for watching lectures efficiently with keyboard
support.
Date: 2024-03-18T16:26
"""
from flask import Flask, render_template, request, send_from_directory
import os
import argparse


app = Flask(__name__, static_folder="static")


@app.route("/")
def index():
    """
    Sends all contents of the video_dir to the index.html.
    Doesn't check if it is a video or not
    """
    video_list = os.listdir(video_dir)

    return render_template("index.html", video_list=video_list)


@app.route("/player")
def player():
    """
    Sends the just the filename of selected video to player.html
    """
    video_path = request.args.get("vidpath", default=None)
    if video_path is None:
        return "No video selected"
    return render_template("player.html", video_path=video_path)


@app.route('/<path:filename>')
def serve_video(filename):
    """
    Simply sends the requested file from video_dir.
    The app.route decorator is required
    """
    return send_from_directory(video_dir, filename)


def get_args():
    """
    Allows to choose a directory to serve videos from.
    Doesn't check whether it is valid path or not.
    """
    parser = argparse.ArgumentParser(prog="js_vid")
    parser.add_argument("video_dir",
                        help="Absolute path of directory having your "
                        "video files")
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = get_args()
    video_dir = args.video_dir
    app.run(debug=True)
