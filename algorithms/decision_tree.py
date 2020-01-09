import math

import numpy as np


class DecisionTreeClassifier:
    INFO_GAIN_THRESHOLD = .05

    def __init__(self):
        self.root = None
        self.feature_names = None

    def fit(self, X_train, y_train, feature_names):
        self.feature_names = feature_names
        root_node = DecisionNode(X_train, y_train, feature_names)
        self.root = root_node
        self._branch(root_node)

    def predict(self, x):
        node = self.root
        while True:
            # leaf nodes have a classification attribute
            # return the classification when we hit a leaf node\
            if node.classification is not None:
                return node.classification
            feature = node.feature
            children_by_attribute = node.children_by_attribute
            feature_i = self.feature_names.index(feature)
            feature_attr = x[feature_i]
            node = children_by_attribute[feature_attr]

    def _calculate_entropy(self, classifications):
        '''
        for binary classification, we have two possible values:
        the positive and negative classes
        the formula for entropy we use is:
        entropy(p, q) = - p * log2(p) - q * log2(q)
        where p is the ratio of the positive class in a node
        and q is the ratio of the negative class in a node
        since there are only two possible values, q is equal to 1 - p
        :param np.array classifications: numpy array of True/False classifications for a possible branch
        '''
        ratio_positive = float(classifications.sum()) / len(classifications)  # ratio of elements classified as True
        ratio_negative = 1.0 - ratio_positive
        entropy_p = entropy_q = 0.0
        if ratio_positive != 0.0:
            entropy_p = - ratio_positive * math.log(ratio_positive, 2)
        if ratio_negative != 0.0:
            entropy_q = - ratio_negative * math.log(ratio_negative, 2)
        entropy = entropy_p + entropy_q
        return entropy

    def _branch(self, decision_node):
        '''
        calculate all possible feature splits for the data in a decision node
        be dumb and just recalculate features we've already split on
        for the best split, assign the feature to the passed decision_node
        and create new children nodes
        recursively call branch on the children nodes if they're not pure within some threshold
        '''
        feature_sets = decision_node.data.T
        y_values = decision_node.y_values
        feature_names = decision_node.feature_names
        starting_entropy = self._calculate_entropy(y_values)

        entropies = []
        for feature_set in feature_sets:
            classifications_by_feature = {}
            # construct a data structure that looks like this
            # {'rainy': [True, True, False, True, False],
            # 'overcast': [True, True, True, True],
            # 'sunny': [False, False, False, True, True]}
            # where the key is the feature attribute and the
            # value is a list of classifications (True or False) for that feature
            for i, feature_val in enumerate(feature_set):
                if not classifications_by_feature.get(feature_val):
                    classifications_by_feature[feature_val] = []
                classifications_by_feature[feature_val].append(y_values[i])

            entropy_for_feature = 0
            for feature_val in classifications_by_feature:
                feature_val_classifications = np.array(classifications_by_feature[feature_val])
                feature_val_entropy = self._calculate_entropy(feature_val_classifications)
                ratio_feature_val = float(len(feature_val_classifications)) / len(y_values)
                entropy_for_feature += ratio_feature_val * feature_val_entropy
            entropies.append(entropy_for_feature)

        info_gains = np.array([starting_entropy - entropy for entropy in entropies])
        highest_info_gain_i = info_gains.argmax()
        highest_info_feature = feature_names[highest_info_gain_i]
        highest_info_gain = starting_entropy - entropies[highest_info_gain_i]
        # if our info gain is very small, set a classification and stop branching
        if highest_info_gain < self.INFO_GAIN_THRESHOLD:
            counts = np.bincount(y_values.astype(int))
            classification = True if np.argmax(counts) == 1 else False
            decision_node.set_classification(classification)
            return

        # now that we have a feature with the highest info gain for the node
        # we label the node with the feature and split it into children
        decision_node.set_feature(highest_info_feature)

        feature_set = feature_sets[highest_info_gain_i]
        indices_by_feature = {}
        for i, feature_val in enumerate(feature_set):
            if not indices_by_feature.get(feature_val):
                indices_by_feature[feature_val] = []
            indices_by_feature[feature_val].append(i)

        for feature in indices_by_feature:
            feature_indices = indices_by_feature[feature]
            child_data = []
            child_y_values = []
            for i in feature_indices:
                child_data.append(decision_node.data[i])
                child_y_values.append(decision_node.y_values[i])
            child_node = DecisionNode(np.array(child_data), np.array(child_y_values), feature_names)
            decision_node.add_child(feature, child_node)
            self._branch(child_node)


class DecisionNode:
    def __init__(self, data, y_values, feature_names, feature=None, classification=None):
        self.data = data
        self.y_values = y_values
        self.feature_names = feature_names
        self.feature = feature
        self.children_by_attribute = {}
        self.classification = classification

    def add_child(self, attribute, decision_node):
        self.children_by_attribute[attribute] = decision_node

    def set_feature(self, feature):
        self.feature = feature

    def set_classification(self, classification):
        self.classification = classification

