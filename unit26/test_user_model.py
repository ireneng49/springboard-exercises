"""User model tests."""

# run these tests like:
#
#    python -m unittest test_user_model.py


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


class UserModelTestCase(TestCase):
    """ Test user model """

    def setUp(self):
        """ Create test client, add sample data """

        User.query.delete()
        Message.query.delete()
        Follows.query.delete()

        db.session.commit()

        self.client = app.test_client()

        user_good = User.signup('usergood','usergood@test.com', 'test_pw', '')
        user_id = 1000
        user_good.id = user_id

        user_soso = User.signup('usersoso','usersoso@test.com', 'soso_pwd', None)
        user_soso_id = 2000
        user_soso.id = user_soso_id

        db.session.commit()

        user_good = User.query.get(user_id)
        user_soso = User.query.get(user_soso_id)
        
        self.user_good = user_good
        self.user_soso = user_soso

    def tearDown(self):
        res = super().tearDown()
        db.session.rollback()
        return res


    #===== BASIC MODEL ================
    #==================================
    def test_user_model(self):
        """ Does basic model work? """

        u = User(
            email="test@test.com",
            username="testuser",
            password="HASHED_PASSWORD"
        )

        db.session.add(u)
        db.session.commit()

        self.assertEqual(u.username, 'testuser')
        self.assertEqual(u.email, 'test@test.com')
        self.assertTrue(u.password.startswith('HASHED_PASSWORD'))
        self.assertEqual(u.image_url, '/static/images/default-pic.png')
        self.assertEqual(u.header_image_url, '/static/images/warbler-hero.jpg')
        self.assertIsNone(u.bio)
        self.assertIsNone(u.location)

        # User should have no messages, no followers, not following anyone, no likes
        self.assertEqual(len(u.messages), 0)
        self.assertEqual(len(u.followers), 0)
        self.assertEqual(len(u.following), 0)
        self.assertEqual(len(u.likes), 0)

        # Representation is accurate
        self.assertEqual(str(u), f'<User #{u.id}: {u.username}, {u.email}>')

    #===== SIGN UP ====================
    #==================================
    def test_good_signup(self):
        user_test = User.signup('usertest', 'usertest@test.com', 'test_password', None)
        user_id = 2222
        user_test.id = user_id
        db.session.commit()

        self.assertIsInstance(user_test, User)
        self.assertEqual(user_test.id, 2222)
        self.assertEqual(user_test.username, 'usertest')
        self.assertEqual(user_test.email, 'usertest@test.com')
        self.assertTrue(user_test.password.startswith('$2b$'))

    def test_no_username_signup(self):
        """ Error if no username entered """
        user_test = User.signup(None, 'usertest@test.com', 'test_pwd', None)
        user_id = 2222
        user_test.id = user_id

        with self.assertRaises(exc.IntegrityError): db.session.commit()

    def test_no_email_signup(self):
        """ Error if no email entered """
        user_test = User.signup('usertest', None, 'test_pwd', None)
        user_id = 2222
        user_test.id = user_id

        with self.assertRaises(exc.IntegrityError): db.session.commit()

    def test_no_password_signup(self):
        """ Error if no password entered """
        with self.assertRaises(ValueError): 
            User.signup('usertest', 'usertest@test.com', None, None)
        
    def test_dup_username_signup(self):
        """ Error if username already in use (usergood signed up in setup function) """
        user_test = User.signup('usergood', 'usertest@test.com', 'test_pwd', None)
        user_id = 2222
        user_test.id = user_id
        
        with self.assertRaises(exc.IntegrityError): db.session.commit()

    def test_dup_email_signup(self):
        """ Error if email already in use (usergood signed up in setup function) """
        user_test = User.signup('usergood', 'usergood@test.com', 'test_pwd', None)
        user_id = 2222
        user_test.id = user_id
        
        with self.assertRaises(exc.IntegrityError): db.session.commit()


    #===== AUTHENTICATION ===============
    #====================================
    def test_good_authenticate(self):
        """ usergood signed up in setup function """
        test_user = User.authenticate('usergood','test_pw')

        self.assertIsInstance(test_user, User)

    def test_bad_username_authenticate(self):
        """ usergood signed up in setup function """
        self.assertFalse(User.authenticate('baduser', 'test_pw'))

    def test_bad_password_authenticate(self):
        """ usergood signed up in setup function """
        self.assertFalse(User.authenticate('gooduser', 'bad_pw'))


    #===== FOLLOWS ===============
    #=============================
    def test_follows(self):
        """ Returns accurate followers/following """
        self.user_soso.following.append(self.user_good)
        db.session.commit()

        self.assertEqual(self.user_good.followers, [self.user_soso])
        self.assertEqual(self.user_soso.following, [self.user_good])

    def test_is_followed_by(self):
        self.user_soso.following.append(self.user_good)
        db.session.commit()

        self.assertTrue(self.user_good.is_followed_by(self.user_soso))
        self.assertFalse(self.user_soso.is_followed_by(self.user_good))

    def test_is_following(self):
        self.user_soso.following.append(self.user_good)
        db.session.commit()

        self.assertTrue(self.user_soso.is_following(self.user_good))
        self.assertFalse(self.user_good.is_following(self.user_soso))

    #===== MESSAGES ===============
    #==============================
    def test_messages(self):
        """ Returns accurate messages associated with this user """
        msg = Message(text='some_text', user_id=self.user_good.id)
        db.session.add(msg)
        db.session.commit()

        self.assertEqual(self.user_good.messages, [msg])

    #===== LIKES ===============
    #===========================
    def test_likes(self):
        """ Returns accurate likes associated with this user """
        msg = Message(text='some_text', user_id=self.user_good.id)
        db.session.add(msg)
        db.session.commit()

        self.user_good.likes.append(msg)
        db.session.commit()

        self.assertEqual(self.user_good.likes, [msg])
