# AUTHOR:
# Ethan Hunt
import unittest
import sqTimeline
import sqVideo
import sqHeatmap

class MyTestCase(unittest.TestCase):

    # sqVideo.py tests
    def test_selectVideo_cancel(self):
        print("Cancel video select")
        self.assertEqual(sqVideo.selectVideo(), "")

    def test_selectVideo_notMP4(self):
        print("Select a non .mp4")
        self.assertEqual(sqVideo.selectVideo(), "nofile")

    def test_parseVideo(self):
        print("Select a correct video")
        v = sqVideo.myVideo(sqVideo.selectVideo())
        self.assertIsNotNone(sqVideo.parseVideo(v))


if __name__ == '__main__':
    unittest.main()
