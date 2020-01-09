import unittest
import numpy as np

from algorithms.decision_tree import DecisionTreeClassifier


class TestDecisionTreeClassifier(unittest.TestCase):
    def setUp(self):
        # our test data consists of weather features
        # and a boolean classification of whether or not we decide to play given each feature vector
        # test data taken from:
        # https://www.slideshare.net/marinasantini1/lecture-4-decision-trees-2-entropy-information-gain-gain-ratio-55241087
        self.feature_names = ['outlook', 'temp',  'humidity', 'windy']

        play_or_not = np.array([['sunny',    'hot',  'high',     False,  False],
                                ['sunny',    'hot',  'high',     True,   False],
                                ['overcast', 'hot',  'high',     False,  True],
                                ['rainy',    'mild', 'high',     False,  True],
                                ['rainy',    'cool', 'normal',   False,  True],
                                ['rainy',    'cool', 'normal',   True,   False],
                                ['overcast', 'cool', 'normal',   True,   True],
                                ['sunny',    'mild', 'high',     False,  False],
                                ['sunny',    'cool', 'normal',   False,  True],
                                ['rainy',    'mild', 'normal',   False,  True],
                                ['sunny',    'mild', 'normal',   True,   True],
                                ['overcast', 'mild', 'high',     True,   True],
                                ['overcast', 'hot',  'normal',   False,  True],
                                ['rainy',    'mild', 'high',     True,   False]])
        self.X_train = play_or_not[:, :-1]
        y_train = (play_or_not[:, -1:]).reshape(len(play_or_not),)
        self.y_train = np.array([True if x == 'True' else False for x in y_train])

    def test_fit(self):
        clf = DecisionTreeClassifier()
        clf.fit(self.X_train, self.y_train, self.feature_names)
        # verify the decision tree looks like this
        #
        #                        feature:
        #                        outlook
        #                         / | \
        #                       /   |   \
        #             rainy   /  overcast \   sunny
        #                   /       |       \
        #                 /         |         \
        #            feature:     class:     feature:
        #            windy        True       humidity
        #            /   \                    /   \
        #   False  /       \  True     high /       \  normal
        #        /           \            /           \
        #      class:      class:      class:        class:
        #      True        False       False         True

        assert clf.root.feature == 'outlook'
        rainy_node = clf.root.children_by_attribute['rainy']
        overcast_node = clf.root.children_by_attribute['overcast']
        sunny_node = clf.root.children_by_attribute['sunny']
        assert rainy_node.feature == 'windy'
        assert overcast_node.classification is True
        assert sunny_node.feature == 'humidity'
        assert rainy_node.children_by_attribute['False'].classification is True
        assert rainy_node.children_by_attribute['True'].classification is False
        assert sunny_node.children_by_attribute['high'].classification is False
        assert sunny_node.children_by_attribute['normal'].classification is True

    def test_predict(self):
        clf = DecisionTreeClassifier()
        clf.fit(self.X_train, self.y_train, self.feature_names)
        expected_for_x = [
            (np.array(['sunny', 'hot', 'high', False]), False),  # sunny outlook + high humidity -> don't play
            (np.array(['sunny', 'hot', 'normal', False]), True),  # sunny outlook + normal humidity -> play
            (np.array(['overcast', 'hot', 'high', False]), True),  # overcast outlook -> don't play
        ]
        for x, expected in expected_for_x:
            output = clf.predict(x)
            assert output == expected

    def test_calculate_entropy(self):
        clf = DecisionTreeClassifier()
        all_positive_class = np.array([True, True])
        assert clf._calculate_entropy(all_positive_class) == 0.0
        fifty_fifty_mix = np.array([True, False])
        assert clf._calculate_entropy(fifty_fifty_mix) == 1.0


if __name__ == '__main__':
    unittest.main()
