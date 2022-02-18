""" Likes model tests """

# run these tests like:
#
#    python -m unittest test_like_model.py


import os
from unittest import TestCase
from sqlalchemy import exc

from models import db, User, Message, Likes

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


class LikesModelTestCase(TestCase):
    """ Test likes model """

    def setUp(self):
        """ Create test user, message, and like, and add sample data """

        User.query.delete()
        Message.query.delete()
        Likes.query.delete()

        db.session.commit()

        self.client = app.test_client()

        test_user = User(id=1000, username='testuser', email='testuser@test.com', password='test_pw')
        db.session.add(test_user)
        db.session.commit()

        test_msg = Message(id=2000, text='some text', user_id=test_user.id)
        db.session.add(test_msg)
        db.session.commit()

        test_like = Likes(id=3000, user_id=test_user.id, message_id=test_msg.id)
        db.session.add(test_like)
        db.session.commit()

        test_user = User.query.get(test_user.id)
        test_msg = Message.query.get(test_msg.id)
        test_like = Likes.query.get(test_like.id)
        
        self.test_user = test_user
        self.test_msg = test_msg
        self.test_like = test_like


    def tearDown(self):
        res = super().tearDown()
        db.session.rollback()
        return res


    #===== BASIC MODEL ================
    #==================================
    def test_likes_model(self):
        """ Does basic model work? """
        m = Message(id=4000, text='interesting stuff', user_id=self.test_user.id)
        db.session.add(m)
        db.session.commit()

        l = Likes(id=5000, user_id=self.test_user.id, message_id=m.id)
        db.session.add(l)
        db.session.commit()

        self.assertEqual(l.message_id, m.id)
        self.assertEqual(l.user_id, self.test_user.id)

    def test_unique_message_id_like(self):
        """ Raise error when attempting to like message that is already liked """
        dup_like = Likes(message_id=self.test_msg.id, user_id=self.test_user.id)
        db.session.add(dup_like)

        with self.assertRaises(exc.IntegrityError): db.session.commit()
        



