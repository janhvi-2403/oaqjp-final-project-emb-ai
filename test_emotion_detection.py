import unittest
from unittest.mock import patch, Mock

from EmotionDetection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_emotion_scores(self, mock_post):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "emotionPredictions": [
                {
                    "emotion": {
                        "anger": 0.1,
                        "disgust": 0.05,
                        "fear": 0.1,
                        "joy": 0.7,
                        "sadness": 0.05,
                    }
                }
            ]
        }
        mock_post.return_value = mock_response

        result = emotion_detector("I am happy")
        self.assertEqual(result["dominant_emotion"], "joy")
        self.assertEqual(result["joy"], 0.7)

    def test_empty_input(self):
        result = emotion_detector("")
        self.assertIsNone(result["dominant_emotion"])


if __name__ == "__main__":
    unittest.main()
