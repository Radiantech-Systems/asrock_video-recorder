
    
  
from flask import Flask, jsonify, send_from_directory, abort
from flask_cors import CORS
from werkzeug.utils import safe_join
import os

app = Flask(__name__)
CORS(app)

VIDEO_ROOT = "/root/video_recorder/events/videos/Signal-Jumping"
VIDEO_EXTENSIONS = {".mp4"}


@app.route("/")
def home():
    return "Jetson Video Server is running"


@app.route("/videos")
def videos():
    """
    Return all event videos under VIDEO_ROOT, including videos stored in
    category subdirectories such as Signal-Jumping/ and No-Helmet/.
    """
    video_list = []

    if not os.path.isdir(VIDEO_ROOT):
        return jsonify([])

    for root, dirs, files in os.walk(VIDEO_ROOT):
        # Stable traversal order
        dirs.sort()
        for filename in files:
            if os.path.splitext(filename)[1].lower() not in VIDEO_EXTENSIONS:
                continue

            full_path = os.path.join(root, filename)
            relative_path = os.path.relpath(full_path, VIDEO_ROOT)
            relative_parts = relative_path.split(os.sep)

            # If the video is inside a category folder, use that folder as
            # the category. Root-level videos are labelled "Uncategorized".
            category = relative_parts[0] if len(relative_parts) > 1 else "Uncategorized"

            try:
                modified_time = os.path.getmtime(full_path)
            except OSError:
                modified_time = 0

            video_list.append({
                "name": filename,
                "path": relative_path.replace(os.sep, "/"),
                "category": category,
                "modified_time": modified_time
            })

    # Newest files first; path is a deterministic tie-breaker.
    video_list.sort(
        key=lambda item: (item["modified_time"], item["path"]),
        reverse=True
    )

    return jsonify(video_list)


@app.route("/video/<path:filename>")
def video(filename):
    """
    Stream a video by its relative path returned from /videos.
    Example: /video/Signal-Jumping/car_20261027_141530.mp4
    """
    safe_path = safe_join(VIDEO_ROOT, filename)
    if safe_path is None or not os.path.isfile(safe_path):
        abort(404)

    directory = os.path.dirname(safe_path)
    file_name = os.path.basename(safe_path)

    return send_from_directory(directory, file_name, conditional=True)


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5002,
        threaded=True
    )

