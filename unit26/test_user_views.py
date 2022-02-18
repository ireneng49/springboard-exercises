"""User View tests."""

# run these tests like:
#
#    FLASK_ENV=production python -m unittest test_user_views.py


import os
from unittest import TestCase

from models import db, connect_db, Message, User, Follows, Likes

# BEFORE we import our app, let's set an environmental variable
# to use a different database for tests (we need to do this
# before we import our app, since that will have already
# connected to the database

os.environ['DATABASE_URL'] = "postgresql:///warbler-test"


# Now we can import app

from app import app, CURR_USER_KEY

# Create our tables (we do this here, so we only create the tables
# once for all tests --- in each test, we'll delete the data
# and create fresh new clean test data
db.drop_all()
db.create_all()

# Don't have WTForms use CSRF at all, since it's a pain to test

app.config['WTF_CSRF_ENABLED'] = False

class UserViewTestCase(TestCase):
    """Test views for users """

    def setUp(self):
        """ Create test client, add sample data """
        User.query.delete()
        Message.query.delete()

        self.client = app.test_client()

        testuser = User.signup(username="testuser",
                                    email="test@test.com",
                                    password="testuser",
                                    image_url=None)
        testuser.id = 1000
        db.session.commit()

        testuser2 = User.signup(username="testuser2",
                                    email="test2@test.com",
                                    password="testuser2",
                                    image_url=None)
        testuser2.id = 3000
        db.session.commit()

        testuser3 = User.signup(username="testuser3",
                                email="test3@test.com",
                                password="testuser3",
                                image_url=None)
        testuser3.id = 5000
        db.session.commit()

        testmessage = Message(id=2000, text='some text', user_id=testuser2.id)
        db.session.add(testmessage)
        db.session.commit()

        testmessage2 = Message(id=4000, text='some other text', user_id=testuser.id)
        db.session.add(testmessage2)
        db.session.commit()

        testfollow = Follows(user_being_followed_id=testuser2.id, user_following_id=testuser.id)
        db.session.add(testfollow)
        db.session.commit()

        testlike = Likes(id=6000, user_id=testuser.id, message_id=testmessage.id)
        db.session.add(testlike)
        db.session.commit()

        testuser = User.query.filter(User.id == testuser.id).first()
        self.testuser = testuser

        testuser2 = User.query.filter(User.id == testuser2.id).first()
        self.testuser2 = testuser2

        testuser3 = User.query.filter(User.id == testuser3.id).first()
        self.testuser3 = testuser3

        testmessage = Message.query.filter(Message.id == testmessage.id).first()
        self.testmessage = testmessage

        testmessage2 = Message.query.filter(Message.id == testmessage2.id).first()
        self.testmessage2 = testmessage2

        testfollow = Follows.query.first()
        self.testfollow = testfollow

        testlike = Likes.query.first()
        self.testlike = testlike
               
    def tearDown(self):
        res = super().tearDown()
        db.session.rollback()
        return res

    def no_session_tests(self, res):
        """ Test the path with no user logged in to session """
        self.assertEqual(res.status_code, 200)
        self.assertIn('Access unauthorized.', str(res.data))
        self.assertIn('<h4>New to Warbler?</h4>', str(res.data))

    def test_list_users(self):
        """ Shows user cards based on search params """
        with self.client as c:
            with c.session_transaction() as sess:
                sess[CURR_USER_KEY] = self.testuser.id

        response = c.get('/users?q=test')
        self.assertEqual(response.status_code, 200)
        self.assertIn('<p class="card-bio">', str(response.data))
        self.assertIn('<p>@testuser</p>', str(response.data))

    def test_users_show(self):
        """ Shows user details and messages originated by this user """
        with self.client as c:
            with c.session_transaction() as sess:
                sess[CURR_USER_KEY] = self.testuser.id

            response = self.client.get(f'/users/{self.testuser.id}')

            self.assertEqual(response.status_code, 200)
            self.assertIn(f'<p>{self.testmessage2.text}</p>', str(response.data))

    def test_show_following(self):
        """ Shows user cards for users being followed by this user """
        with self.client as c:
            with c.session_transaction() as sess:
                sess[CURR_USER_KEY] = self.testuser.id

        response = self.client.get(f'/users/{self.testuser.id}/following')

        self.assertEqual(response.status_code, 200)
        self.assertIn(f'<p>@{self.testuser2.username}</p>', str(response.data))

    def test_no_session_show_following(self):
        """ Shows unauthorized message, redirects to home """
        with self.client as c:
            response = self.client.get(f'/users/{self.testuser.id}/following', follow_redirects=True)

        self.no_session_tests(response)
    
    def test_users_followers(self):
        """ Shows user cards for users following this user """
        with self.client as c:
            with c.session_transaction() as sess:
                sess[CURR_USER_KEY] = self.testuser.id

            response = self.client.get(f'/users/{self.testuser2.id}/followers')

            self.assertEqual(response.status_code, 200)
            self.assertIn(f'<p>@{self.testuser.username}</p>', str(response.data))

    def test_no_session_users_followers(self):
        """ Show unauthorized message, redirect to home """
        with self.client as c:
            response = self.client.get(f'/users/{self.testuser2.id}/followers', follow_redirects=True)

        self.no_session_tests(response)

    def test_add_follow(self):
        """ Adds follow to follows table, shows card on following page"""  
        with self.client as c:
            with c.session_transaction() as sess:
                sess[CURR_USER_KEY] = self.testuser.id

            response = self.client.post(f'/users/follow/{self.testuser3.id}', follow_redirects=True)

            self.assertEqual(response.status_code, 200)
            self.assertIn(f'<p>@{self.testuser3.username}</p>', str(response.data))
            self.assertIn(self.testuser3.id, [follow.user_being_followed_id for follow in Follows.query.all()])

    def test_no_session_add_follow(self):
        """ Show unauthorized message, redirect to home """
        with self.client as c:
            response = self.client.post(f'/users/follow/{self.testuser3.id}', follow_redirects=True)

        self.no_session_tests(response)

    def test_stop_following(self):
        """ Removes follow from follows table, user card does not show on following page """
        with self.client as c:
            with c.session_transaction() as sess:
                sess[CURR_USER_KEY] = self.testuser.id

            response = self.client.post(f'/users/stop-following/{self.testuser2.id}', follow_redirects=True)

            self.assertEqual(response.status_code, 200)
            self.assertNotIn(f'<p>@{self.testuser2.username}</p>', str(response.data))
            self.assertNotIn(self.testuser2.id, [follow.user_being_followed_id for follow in Follows.query.all()])

    def test_no_session_stop_following(self):
        """ Show unauthorized message, redirect to home """
        with self.client as c:
            response = self.client.post(f'/users/stop-following/{self.testuser2.id}', follow_redirects=True)

        self.no_session_tests(response)
    
    def test_toggle_like_message(self):
        """ Remove testuser/testmessage (testlike) from likes table """
        with self.client as c:
            with c.session_transaction() as sess:
                sess[CURR_USER_KEY] = self.testuser.id

            response = self.client.post(f'/users/add_like/{self.testmessage.id}', follow_redirects=True)

            self.assertEqual(response.status_code, 200)
            self.assertNotIn("btn-primary", str(response.data))
            self.assertNotIn(self.testlike.id, [like.message_id for like in Likes.query.all()])

    def test_users_likes(self):
        """ Liked messages show up on page """
        with self.client as c:
            with c.session_transaction() as sess:
                sess[CURR_USER_KEY] = self.testuser.id

        response = self.client.get(f'/users/{self.testuser.id}/likes')

        self.assertEqual(response.status_code, 200)
        self.assertIn(self.testmessage.text, str(response.data))

    def test_no_session_users_likes(self):
        """ Show unauthorized message, redirect to home """
        with self.client as c:
            response = self.client.get(f'/users/{self.testuser.id}/likes', follow_redirects=True)

        self.no_session_tests(response)

    def test_get_profile(self):
        """ Show form populated with user profile data on get request """
        with self.client as c:
            with c.session_transaction() as sess:
                sess[CURR_USER_KEY] = self.testuser.id
            response = self.client.get(f'/users/{self.testuser.id}/profile')

        self.assertEqual(response.status_code, 200)
        self.assertIn('<h2 class="join-message">Edit Your Profile.</h2>', str(response.data))
        self.assertIn('value="testuser"', str(response.data))
        self.assertIn('value="test@test.com"', str(response.data))

    def test_no_session_get_profile(self):
        """ Show unauthorized message, redirect to home """
        with self.client as c:
            response = self.client.get(f'/users/{self.testuser.id}/profile', follow_redirects=True)

        self.no_session_tests(response)

    def test_post_profile(self):
        """ Process and display profile change accurately """
        with self.client as c:
            with c.session_transaction() as sess:
                sess[CURR_USER_KEY] = self.testuser.id
            response = self.client.post(f'/users/{self.testuser.id}/profile',
                                        data={'username':'testuser',
                                              'password':'testuser',
                                              'bio':'here is a bio'},
                                        follow_redirects=True)

        self.assertEqual(response.status_code, 200)
        self.assertIn(f'<h4 id="sidebar-username">@{self.testuser.username}</h4>',str(response.data))
        self.assertIn('here is a bio', str(response.data))

    def test_no_session_post_profile(self):
        """ Show unauthorized message, redirect to home """
        with self.client as c:
            response = self.client.get(f'/users/{self.testuser.id}/profile', follow_redirects=True)

        self.no_session_tests(response)
    
    def test_unauthorized_post_profile(self):
        """ Process and display profile change accurately """
        with self.client as c:
            with c.session_transaction() as sess:
                sess[CURR_USER_KEY] = self.testuser.id
        response = self.client.post(f'/users/{self.testuser.id}/profile',
                                    data={'username':'testuser',
                                    'password':'testuserX',
                                    'bio':'here is a bio'},
                                    follow_redirects=True)

        self.assertEqual(response.status_code, 200)
        self.assertNotIn(f'<h4 id="sidebar-username">@{self.testuser.username}</h4>', str(response.data))
        self.assertIn('Username/password incorrect', str(response.data))
        self.assertNotIn('here is a bio', str(response.data))

    def test_delete_user(self):
        """ Removes user from users table """
        with self.client as c:
            with c.session_transaction() as sess:
                sess[CURR_USER_KEY] = self.testuser.id
            response = self.client.post('/users/delete', follow_redirects=True)

        self.assertEqual(response.status_code, 200)
        self.assertIn('<h2 class="join-message">Join Warbler today.</h2>', str(response.data))
        self.assertNotIn(self.testuser.id, [user.id for user in User.query.all()])

    def test_no_session_delete_user(self):
        """ Show unauthorized message, redirect to home """
        with self.client as c:
            response = self.client.post('/users/delete', follow_redirects=True)

        self.no_session_tests(response)
