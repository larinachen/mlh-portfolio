import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)



# variables
class Hobby:
    def __init__(self, img_url, title, description):
        self.img_url = img_url
        self.title = title
        self.description = description


my_hobbies = [Hobby('https://picsum.photos/id/217/200/300', 'title1', 'description1'),
                Hobby('https://picsum.photos/id/27/200/300', 'title2', 'description2'),
                Hobby('https://picsum.photos/id/237/200/300', 'title3', 'description3') ]


@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"))

@app.route('/hobbies')
def hobbies():
    return render_template('hobbies.html', hobbies=my_hobbies)

# start the development server using the run() method
if __name__ == "__main__":
    app.run(debug=True)