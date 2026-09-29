from flask import Flask, render_template

app = Flask(__name__)

PROFILE = {
    "name": "Varun Joshi",
    "tagline": "Find me around the internet",
    "image": "profile.jpg",
}

# Edit this list to add, remove or reorder links.
# "icon" must match a key in the ICONS dict in templates/index.html.
LINKS = [
    {
        "title": "TikTok",
        "url": "https://www.tiktok.com/@varunjoshitiktok",
        "icon": "tiktok",
    },
    {
        "title": "Instagram",
        "url": "https://www.instagram.com/varunjoshi_insta/",
        "icon": "instagram",
    },
    {
        "title": "YouTube",
        "url": "https://www.youtube.com/@varunjoshi3991",
        "icon": "youtube",
    },
    {
        "title": "TrackThings App",
        "url": "https://trackthingsapp.com",
        "icon": "globe",
    },
]


@app.route("/")
def index():
    return render_template("index.html", profile=PROFILE, links=LINKS)


@app.route("/healthz")
def health():
    return "ok"


if __name__ == "__main__":
    app.run(debug=True, port=5000)
