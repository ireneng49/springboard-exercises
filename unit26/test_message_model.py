""" Message model tests """

# run these tests like:
#
#    python -m unittest test_message_model.py


import os
from unittest import TestCase
from sqlalchemy import exc
from datetime import datetime

from models import db, User, Message

# BEFORE we import our app, let's set an environmental variable
# to use a different database for tests (we need to do this
# before we import our app, since that will have already
# connected to the database

os.environ['DATABASE_URL'] = "postgresql:///warbler-test"


# Now we can import app

from app import app

# Create our tables (we do this here, so we only create the tables
# once for all tests --- in each test, we'll delete the data
# and create fresh new clean test data

db.drop_all()
db.create_all()


class MessageModelTestCase(TestCase):
    """ Test message model """

    def setUp(self):
        """ Create test user and message, add sample data """

        User.query.delete()
        Message.query.delete()

        db.session.commit()

        self.client = app.test_client()

        test_user = User(id=1000, username='testuser', email='testuser@test.com', password='test_pw')
        db.session.add(test_user)
        db.session.commit()

        test_message = Message(id=2000, text='some text', user_id=test_user.id)
        db.session.add(test_message)
        db.session.commit()

        test_user = User.query.get(test_user.id)
        test_message = Message.query.get(test_message.id)
        
        self.test_user = test_user
        self.test_message = test_message


    def tearDown(self):
        res = super().tearDown()
        db.session.rollback()
        return res


    #===== BASIC MODEL ================
    #==================================
    def test_message_model(self):
        """ Does basic model work? """
        d = datetime.utcnow()
        m = Message(id=9000, text='testing 1-2-3', timestamp=d, user_id=self.test_user.id)

        db.session.add(m)
        db.session.commit()

        self.assertEqual(m.text, 'testing 1-2-3')
        self.assertEqual(m.timestamp, d)
        self.assertEqual(m.user_id, self.test_user.id)

    def test_no_text_message(self):
        """ Raise error when creating message with no text """
        bad_message = Message(id=4000, text=None, user_id=self.test_user.id)
        db.session.add(bad_message)

        with self.assertRaises(exc.IntegrityError): db.session.commit()

    def test_no_user_id_message(self):
        """ Raise error when creating message with no user_id """
        bad_message = Message(id=4000, text='blah', user_id=None)
        db.session.add(bad_message)

        with self.assertRaises(exc.IntegrityError): db.session.commit()


    #===== USERS RELATIONSHIP ====================
    #=============================================
    def test_user(self):
        """ Returns accurate user information associated with this message """

        self.assertEqual(self.test_message.user.username, 'testuser')
        self.assertEqual(self.test_message.user.email, 'testuser@test.com')
        self.assertEqual(len(self.test_message.user.likes), 0)
        self.assertEqual(self.test_message.user.messages, [self.test_message])

