from pprint import pprint

from data_processing.probabilities_extraction import form_probabilities

probabilities = form_probabilities()


def estimate_probability(user_input: dict):
    probabilities_list = []
    probabilities_ = form_probabilities()
    datasets_number = len(probabilities_)

    # Iterate through user_input to get corresponding probabilities
    for category, value in user_input.items():
        # Check if the category is in probabilities_dict and if the value is a key in the sub-dictionary
        if category in probabilities_ and value in probabilities_[category]:
            # Append the probability to the list
            probabilities_list.append(probabilities_[category][value])

    total = [probability for probability in probabilities_list]
    prob = round(sum(total) / datasets_number, 2)
    prob_inverted = 100 - round(sum(total) / datasets_number, 2)
    # return round(sum(total) / datasets_number, 2)
    return prob, prob_inverted


# if __name__ == '__main__':
#     # estimate_probability()
#     # print(user_input)
#     pprint(probabilities)
#     pass
