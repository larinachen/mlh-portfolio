import unittest
import os
os.environ['TESTING'] = 'true'

from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
    
    def test_home(self):
        """
        Test the root directory.
        """
        response = self.client.get("/")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert '<title>Home</title>' in html
        assert 'Yundi Chen' in html
        assert '<img src="../static/img/Chen_Larina_Photo.jpg">' in html

    def test_timeline_get(self):
        """
        Test the timeline_post endpoint GET method.
        """
        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert "timeline_posts" in json
        assert len(json["timeline_posts"]) == 0, f"Actual length: {len(json['timeline_posts'])}"
    
    def test_timeline_post(self):
        """
        Test the timeline_post endpoint POST method.
        """
        response = self.client.post('/api/timeline_post', data={
            "name": "John Doe",
            "email": "johndoe@email.com",
            "content": "Testing from test_app.py!"
        })
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert json['name'] == 'John Doe'
        assert json['email'] == 'johndoe@email.com'
        assert json['content'] == 'Testing from test_app.py!'

        response_get = self.client.get("/api/timeline_post")
        assert response_get.status_code == 200
        assert response_get.is_json
        json_get = response_get.get_json()
        assert "timeline_posts" in json_get
        assert len(json_get["timeline_posts"]) == 1
        
    def test_timeline(self):
        """
        Test the timeline.html page.
        """
        response = self.client.get("/timeline.html")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert '<title>Timeline</title>' in html
        assert '<form id="form">' in html
        assert 'Timeline Logs' in html

    def test_malformed_timeline_post(self):
        """
        Test malformed POST requests to timeline_post endpoint.
        """
        # POST request missing name
        response = self.client.post('/api/timeline_post', data={
            "email": "johndoe@email.com",
            "content": "Testing from test_app.py!"
        })
        html = response.get_data(as_text=True)
        assert response.status_code == 400, f"Response code: {response.status_code} html response is: {html}"
        assert "Invalid name" in html, f"html response is: {html}"

        # POST request empty name
        response = self.client.post('/api/timeline_post', data={
            "name": "",
            "email": "johndoe@email.com",
            "content": "Testing from test_app.py!"
        })
        html = response.get_data(as_text=True)
        assert response.status_code == 400, f"Response code: {response.status_code} html response is: {html}"
        assert "Empty name" in html, f"html response is: {html}"
        
        # POST request missing content
        response = self.client.post('/api/timeline_post', data={
            "name": "John Doe",
            "email": "johndoe@email.com"
        })
        html = response.get_data(as_text=True)
        assert response.status_code == 400, f"Response code: {response.status_code} html response is: {html}"
        assert "Invalid content" in html, f"html response is: {html}"

        # POST request empty content
        response = self.client.post('/api/timeline_post', data={
            "name": "John Doe",
            "email": "johndoe@email.com",
            "content": ""
        })
        html = response.get_data(as_text=True)
        assert response.status_code == 400, f"Response code: {response.status_code} html response is: {html}"
        assert "Empty content" in html, f"html response is: {html}"

        # POST request with missing email
        response = self.client.post('/api/timeline_post', data={
            "name": "John Doe",
            "content": "Hello world, I'm John!"
        })
        html = response.get_data(as_text=True)
        assert response.status_code == 400, f"Response code: {response.status_code} html response is: {html}"
        assert "Invalid email" in html, f"html response is: {html}"

        # POST request with malformed email
        response = self.client.post('/api/timeline_post', data={
            "name": "John Doe",
            "email": "not-an-email",
            "content": "Hello world, I'm John!"
        })
        html = response.get_data(as_text=True)
        assert response.status_code == 400, f"Response code: {response.status_code} html response is: {html}"
        assert "Invalid email" in html, f"html response is: {html}"
