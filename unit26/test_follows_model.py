""" Follows model tests """

# run these tests like:
#
#    python -m unittest test_follows_model.py


import os
from unittest import TestCase
from sqlalchemy import exc

from models import db, User, Message, Follows

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


class FollowsModelTestCase(TestCase):
    """ Test follows model """

    def setUp(self):
        """ Create test users and add sample data """

        User.query.delete()
        Message.query.delete()
        Follows.query.delete()

        db.session.commit()

        self.client = app.test_client()

        user1 = User(id=1000, username='user1', email='user1@test.com', password='test_pw1')
        user2 = User(id=2000, username='user2', email='user2@test.com', password='test_pw2')
        db.session.add_all([user1, user2])
        db.session.commit()

        user1 = User.query.get(user1.id)
        user2 = User.query.get(user2.id)
        
        self.user1 = user1
        self.user2 = user2


    def tearDown(self):
        res = super().tearDown()
        db.session.rollback()
        return res


    #===== BASIC MODEL ================
    #==================================
    def test_follows_model(self):
        """ Does basic model work? """
        f = Follows(user_being_followed_id=self.user2.id, user_following_id=self.user1.id)
        db.session.add(f)
        db.session.commit()

        self.assertEqual(f.user_being_followed_id, self.user2.id)
        self.assertEqual(f.user_following_id, self.user1.id)

        



