""" Message View tests """

# run these tests like:
#
#    FLASK_ENV=production python -m unittest test_message_views.py


import os
from unittest import TestCase

from models import db, connect_db, Message, User

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


class MessageViewTestCase(TestCase):
    """ Test views for messages """

    def setUp(self):
        """ Create test client, add sample data """

        User.query.delete()
        Message.query.delete()

        self.client = app.test_client()

        self.testuser = User.signup(username="testuser",
                                    email="test@test.com",
                                    password="testuser",
                                    image_url=None)

        db.session.commit()

        testmessage = Message(id=1000, text='testing 123', user_id=self.testuser.id)
        db.session.add(testmessage)
        db.session.commit()
        testmessage = Message.query.filter(Message.id==testmessage.id).first()
        self.testmessage = testmessage

    def tearDown(self):
        res = super().tearDown()
        db.session.rollback()
        return res

    def test_messages_add(self):
        """ Message is added to db """
        # Since we need to change the session to mimic logging in,
        # we need to use the changing-session trick:
        with self.client as c:
            with c.session_transaction() as sess:
                sess[CURR_USER_KEY] = self.testuser.id
            # Now, that session setting is saved, so we can have
            # the rest of ours test

            response = c.post("/messages/new", data={"text": "Hello"}, follow_redirects=True)
            
            messages = Message.query.all()

            self.assertEqual(response.status_code, 200)
            self.assertEqual(2, len(messages))
            self.assertIn('testing 123', str(response.data))
            self.assertIn('Hello', str(response.data))

    def test_no_session_user_add(self):
        """ Should not be able to add message if not logged in """
        with self.client as c:
            response = c.post("/messages/new", data={"text": "Hello"}, follow_redirects=True)

            self.assertEqual(response.status_code, 200)
            self.assertIn('Access unauthorized.', str(response.data))

    def test_messages_show(self):
        """ Show messages created by logged in user """
        with self.client as c:
            with c.session_transaction() as sess:
                sess[CURR_USER_KEY] = self.testuser.id

            msg = Message(id=2000, text='some text', user_id=self.testuser.id)
            db.session.add(msg)
            db.session.commit()

            response = c.get(f'/messages/{msg.id}')
            
            self.assertEqual(response.status_code, 200)
            self.assertIn('some text', str(response.data))
        

    def test_messages_destroy(self):
        """ Message is deleted from db """
        with self.client as c:
            with c.session_transaction() as sess:
                sess[CURR_USER_KEY] = self.testuser.id

            response = c.post(f'/messages/{self.testmessage.id}/delete', follow_redirects=True)

            messages = Message.query.all()

            self.assertEqual(response.status_code, 200)
            self.assertEqual(0, len(messages))
            self.assertNotIn('testing 123', str(response.data))

    def test_no_session_user_messages_destroy(self):
        """ Should not be able to delete message if not logged in """
        with self.client as c:
            response = c.post(f'/messages/{self.testmessage.id}/delete', follow_redirects=True)

            self.assertEqual(response.status_code, 200)
            self.assertIn('Access unauthorized.', str(response.data))

