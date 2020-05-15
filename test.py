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

    def test_parseVideo(self):
        print("Select a correct video")
        v = sqVideo.myVideo(sqVideo.selectVideo())
        self.assertIsNotNone(sqVideo.parseVideo(v))

    # sqHeatmap.py tests
    def test_generateHeatmapUnit(self):
        x = "testdata.csv"
        h = sqHeatmap.generateHeatmapUnit(x)
        self.assertIsNotNone(h)

    # sqTimeline.py tests
    def test_generateTimelineUnit(self):
        x = "testdata.csv"
        t = sqTimeline.generateTimelineUnit(x)
        self.assertIsNotNone(t)


if __name__ == '__main__':
    unittest.main()
