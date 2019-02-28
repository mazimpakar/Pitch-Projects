import unittest
from app.models import Pitch

class PitchModelTest(unittest.TestCase):

    def setUp(self):
        self.new_pitch = Pitch(id = 1, title = 'What Makes a Song Sad', pitch_content = 'Where does sad music get its sadness from? And whom should you ask—a composer or a cognitive psychologist?', category = 'Pickup Lines', upvote = 10, downvote = 12, author = 'DANIEL WATTENBERG'
)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_pitch, Pitch))

    def test_save_comment(self):
        self.new_comment.save_comment()
        self.assertTrue(len(Comment.query.all())>0)