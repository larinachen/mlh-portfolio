import os
from flask import Flask, render_template, request
from dotenv import load_dotenv
from peewee import *
import datetime
from playhouse.shortcuts import model_to_dict

# loading environment variables in .env
load_dotenv()

# app configurations
app = Flask(__name__)

mydb = MySQLDatabase(os.getenv("MYSQL_DATABASE"),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        host=os.getenv("MYSQL_HOST"),
        port=3306
    )

print(mydb)

class TimelinePost(Model):
    name = CharField()
    email = CharField()
    content = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = mydb

mydb.connect()
mydb.create_tables([TimelinePost])


# create POST endpoint
@app.route('/api/timeline_post', methods=['POST'])
def post_timeline_post():
    name = request.form['name']
    email = request.form['email']
    content = request.form['content']
    timeline_post = TimelinePost.create(name=name, email=email, content=content)

    print([name,email,content,timeline_post])
    print("hello")

    return model_to_dict(timeline_post)

# create GET endpoint
@app.route('/api/timeline_post', methods=['GET'])
def get_timeline_post():
    return {
        'timeline_posts':[
            model_to_dict(p)
            for p in TimelinePost.select().order_by(TimelinePost.created_at.desc())
        ]
    }

# create a DELETE endpoint
@app.rount('api/timeline_post', methods=['POST'])
def delete_timeline_post():
    pass
    # TODO: research how to delete with mysql

# ======================= FRONT END ============================

# variables
class Hobby:
    def __init__(self, img_url, title, description):
        self.img_url = img_url
        self.title = title
        self.description = description


my_hobbies = [Hobby('../static/img/books.jpg', 'Recipe Development', 'I make the coolest foods :))'),
                Hobby('../static/img/beach.jpg', 'Biking', 'Bike is life! 🚵🚵🚵'),
                Hobby('../static/img/deserttrek.jpg', 'Reading', 'Reading transports me into a world no one else has seen or will ever see'),
                Hobby('../static/img/ukelele.png', 'Biking', 'Bike is life! 🚵🚵🚵'),
                Hobby('../static/img/art gallery 2.jpg', 'Biking', 'Bike is life! 🚵🚵🚵'),
                Hobby('../static/img/stinky.jpg', 'Biking', 'Bike is life! 🚵🚵🚵') ]

class Education:
    def __init__(self, school_name, grad_year, description):
        self.school_name = school_name
        self.grad_year = grad_year
        self.description = description

my_education = [Education('Northwestern University', 'Bachelor of Science: Computer Science | Data Science and Engineering Minor', 
                'Dean\'s List student majoring in Computer Science in McCormick School of Engineering. Mathematics Emerging Scholars program in fall 2021. Courses: Data Structures and Algorithms, Discrete Math, Machine Learning, Programming Fundamentals'),
                ]

class Experience:
    def __init__(self, experience_name, description):
        self.experience_name = experience_name
        self.description = description

my_experiences = [Experience('Major League Hacking | Production Engineering Fellow', 'description of your working experience... Est iure fugit in nulla officia hic delectus quia qui veniam voluptas vel consequuntur placeat qui esse dignissimos aut tempora laudantium! Aut repellat doloremque aut quod dolores ut repellat iusto quo nihil aperiam ut animi maxime et quia dolor.'),
                 Experience('Google | Software Product Sprint Student', 'description of your working experience... Est iure fugit in nulla officia hic delectus quia qui veniam voluptas vel consequuntur placeat qui esse dignissimos aut tempora laudantium! Aut repellat doloremque aut quod dolores ut repellat iusto quo nihil aperiam ut animi maxime et quia dolor.'),
                 Experience('Cravosity | Product Intern', 'description of your working experience... Est iure fugit in nulla officia hic delectus quia qui veniam voluptas vel consequuntur placeat qui esse dignissimos aut tempora laudantium! Aut repellat doloremque aut quod dolores ut repellat iusto quo nihil aperiam ut animi maxime et quia dolor.')]

my_additional_experiences = [Experience('Title1', 'description of volunteer work, hackathons etc... Est iure fugit in nulla officia hic delectus quia qui veniam voluptas vel consequuntur placeat qui esse dignissimos aut tempora laudantium! Aut repellat doloremque aut quod dolores ut repellat iusto quo nihil aperiam ut animi maxime et quia dolor.'),
                            Experience('Title2', 'description of volunteer work, hackathons etc... Est iure fugit in nulla officia hic delectus quia qui veniam voluptas vel consequuntur placeat qui esse dignissimos aut tempora laudantium! Aut repellat doloremque aut quod dolores ut repellat iusto quo nihil aperiam ut animi maxime et quia dolor.')]


class Project:
    def __init__(self, img_url, title, description):
        self.img_url = img_url
        self.title = title
        self.description = description

# mello, activism, boba shop, unveil
my_projects = [Project('static/img/Mello Home Page.png', 'Mello Wellness Web App', 'Super awesome project that I cannot wait to share with everyone!'),
                Project('static/img/demo_pic.png','ACTivism Chrome Extension', 'Glaciers are awesome! 😍 Check out the world\'s coolest glaciers through this interactive game.'),
                Project('static/img/bobaanalysis.png','Shop Rating Predictor', 'Glaciers are awesome! 😍 Check out the world\'s coolest glaciers through this interactive game.'),
                Project('static/img/bobaanalysis.png','Basic AI Algorithms', 'Glaciers are awesome! 😍 Check out the world\'s coolest glaciers through this interactive game.'),
                Project('https://picsum.photos/id/110/200/300', 'AutoAquaponics', 'Everything delivered fast & furious.')]


# leadership: cs mentorshiop, epic, technovation
class Leadership:
    def __init__(self, img_url, title, description):
        self.img_url = img_url
        self.title = title
        self.description = description

my_leaderships = [Leadership('https://picsum.photos/id/17/200/300', 'Northwestern Computer Science Mentorship', 'description'),
                    Leadership('https://picsum.photos/id/27/200/300', 'EPIC Entrepreneurship Club', 'description'),
                    Leadership('https://picsum.photos/id/37/200/300', 'Technovation Girls', 'description')]

class Location:
    def __init__(self, id, loc, img_urls, title, description):
        self.id = id
        self.loc = loc
        self.img_urls = img_urls
        self.title = title
        self.description = description

my_locations = [Location('van',[43.75, 79.87],['https://picsum.photos/id/17/200/300'],'Vancouver, BC', 'my beautiful home <3'),
                Location('ham',[45.75, 70.87],['https://picsum.photos/id/200/200/300'],'Hamilton, ON', 'where I went to Shad, my first ever tech experience'),
                Location('otw',[66.75, 105.87],['https://picsum.photos/id/110/200/300'],'Ottawa, ON', 'just magnificent')]

@app.route('/')
@app.route('/index.html')
def index():
   return render_template('index.html', title="Home", firstname="First", lastname="Last", url=os.getenv("URL"))

@app.route('/hobbies.html')
def hobbies():
    return render_template('hobbies.html', title="About",hobbies=my_hobbies, locations=my_locations)

@app.route('/leaderships.html')
def leadership():
    return render_template('leaderships.html', title="Leadership", leaderships=my_leaderships)

@app.route('/experiences.html')
def experiences():
    return render_template('experiences.html', education=my_education, experiences=my_experiences, add_experiences=my_additional_experiences, title="Experience")

@app.route('/projects.html')
def projects():
    return render_template('projects.html', title="Projects", projects=my_projects)

# start the development server using the run() method
if __name__ == "__main__":
    app.run(debug=True)
