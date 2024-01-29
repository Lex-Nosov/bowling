import unittest

from utils import get_score, get_score_new_rules


class BowlingTest(unittest.TestCase):

    def test_normal_data_0(self):
        result = get_score('xx1/325-')
        self.assertEqual(result, 65)

    def test_normal_data_1(self):
        result = get_score('X4/341412X513/1-X')
        self.assertEqual(result, 112)

    def test_normal_data_2(self):
        result = get_score('X4/-41-12X5-3/1--9')
        self.assertEqual(result, 93)

    def test_normal_data_4(self):
        result = get_score('-/-/-/-/-/-/-/-/-/-/')
        self.assertEqual(result, 150)

    def test_normal_data_5(self):
        result = get_score('XXXXXXXXXX')
        self.assertEqual(result, 200)

    def test_normal_data_6(self):
        result = get_score('2/4/6/8/1/3/5/7/9/1/')
        self.assertEqual(result, 150)

    def test_normal_data_8(self):
        result = get_score('--------------------')
        self.assertEqual(result, 0)

    def test_invalid_characters_0(self):
        with self.assertRaises(ValueError):
            get_score('xx1|325-')

    def test_invalid_characters_1(self):
        with self.assertRaises(ValueError):
            get_score('qwerasdfzxcvtyghbnui')

    def test_invalid_characters_2(self):
        with self.assertRaises(ValueError):
            get_score('xx34465/0/')

    def test_invalid_characters_3(self):
        with self.assertRaises(ValueError):
            get_score('sdfsdfsdf')

    def test_invalid_characters_4(self):
        with self.assertRaises(ValueError):
            get_score('0000000000')

    def test_invalid_characters_5(self):
        with self.assertRaises(ValueError):
            get_score('1/2/3/4/0/')

    def test_few_frames_0(self):
        with self.assertRaises(ValueError):
            get_score('X')

    def test_few_frames_1(self):
        with self.assertRaises(ValueError):
            get_score('')

    def test_many_frames_0(self):
        with self.assertRaises(ValueError):
            get_score('XXXXX343434343434')

    def test_many_frames_3(self):
        with self.assertRaises(ValueError):
            get_score('2/4/6/8/1/3/5/7/9/1/X')

    def test_many_frames_4(self):
        with self.assertRaises(ValueError):
            get_score('X23--5/346/444-14-823231231')

    def test_not_enough_throws_in_frame_0(self):
        with self.assertRaises(ValueError):
            get_score('xx345')

    def test_not_enough_throws_in_frame_1(self):
        with self.assertRaises(ValueError):
            get_score('XXXXX3')

    def test_not_enough_throws_in_frame_2(self):
        with self.assertRaises(ValueError):
            get_score('3/5/6/-')

    def test_not_enough_throws_in_frame_3(self):
        with self.assertRaises(ValueError):
            get_score('-------')

    def test_frame_size_exceeded_0(self):
        with self.assertRaises(ValueError):
            get_score('X4/-41-79X5-3/1--9')

    def test_frame_size_exceeded_1(self):
        with self.assertRaises(ValueError):
            get_score('99999999999999999999')


class BowlingTestNewRules(unittest.TestCase):

    def test_normal_data_0(self):
        result = get_score_new_rules('X4/34')
        self.assertEqual(result, 40)

    def test_normal_data_1(self):
        result = get_score_new_rules('XXX347/21')
        self.assertEqual(result, 92)

    def test_normal_data_2(self):
        result = get_score_new_rules('X4/-41-12X5-3/1--9')
        self.assertEqual(result, 79)

    def test_normal_data_4(self):
        result = get_score_new_rules('-/-/-/-/-/-/-/-/-/-/')
        self.assertEqual(result, 100)

    def test_normal_data_5(self):
        result = get_score_new_rules('XXXXXXXXXX')
        self.assertEqual(result, 270)

    def test_normal_data_6(self):
        result = get_score_new_rules('2/4/6/8/1/3/5/7/9/1/')
        self.assertEqual(result, 144)

    def test_normal_data_8(self):
        result = get_score_new_rules('--------------------')
        self.assertEqual(result, 0)

    def test_invalid_characters_0(self):
        with self.assertRaises(ValueError):
            get_score_new_rules('xx1|325-')

    def test_invalid_characters_1(self):
        with self.assertRaises(ValueError):
            get_score_new_rules('qwerasdfzxcvtyghbnui')

    def test_invalid_characters_2(self):
        with self.assertRaises(ValueError):
            get_score_new_rules('xx34465/0/')

    def test_invalid_characters_3(self):
        with self.assertRaises(ValueError):
            get_score_new_rules('sdfsdfsdf')

    def test_invalid_characters_4(self):
        with self.assertRaises(ValueError):
            get_score_new_rules('0000000000')

    def test_invalid_characters_5(self):
        with self.assertRaises(ValueError):
            get_score_new_rules('1/2/3/4/0/')


if __name__ == '__main__':
    unittest.main()
