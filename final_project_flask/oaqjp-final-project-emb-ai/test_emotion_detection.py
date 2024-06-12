import unittest
from EmotionDetection.emotion_detection import emotion_detector

class EmotionDetectionTest(unittest.TestCase):
    """
    Unit test class for testing the emotion_detector function from the EmotionDetection module.
    """

    def testJoy(self):
        """
        Test case for detecting 'joy' emotion.
        """
        text = 'I am so happy today, it is such a great day!'
        expected_emotion = 'joy'
        emotions = emotion_detector(text)
        detected_emotion = max(emotions, key=emotions.get) if emotions else None
        self.assertEqual(detected_emotion, expected_emotion)

    def testSadness(self):
        """
        Test case for detecting 'sadness' emotion.
        """
        text = 'I lost my job today, and I feel so sad and depressed.'
        expected_emotion = 'sadness'
        emotions = emotion_detector(text)
        detected_emotion = max(emotions, key=emotions.get) if emotions else None
        self.assertEqual(detected_emotion, expected_emotion)

    def testAnger(self):
        """
        Test case for detecting 'anger' emotion.
        """
        text = 'I am so angry at my boss for treating me unfairly!'
        expected_emotion = 'anger'
        emotions = emotion_detector(text)
        detected_emotion = max(emotions, key=emotions.get) if emotions else None
        self.assertEqual(detected_emotion, expected_emotion)

    def testFear(self):
        """
        Test case for detecting 'fear' emotion.
        """
        text = 'I am terrified of heights and can never go near the edge of a tall building.'
        expected_emotion = 'fear'
        emotions = emotion_detector(text)
        detected_emotion = max(emotions, key=emotions.get) if emotions else None
        self.assertEqual(detected_emotion, expected_emotion)

    def testDisgust(self):
        """
        Test case for detecting 'disgust' emotion.
        """
        text = 'The smell of rotten eggs is so disgusting, it makes me want to vomit.'
        expected_emotion = 'disgust'
        emotions = emotion_detector(text)
        detected_emotion = max(emotions, key=emotions.get) if emotions else None
        self.assertEqual(detected_emotion, expected_emotion)

if __name__ == '__main__':
    unittest.main()
