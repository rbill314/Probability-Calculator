import copy
import random
# Consider using the modules imported above.


class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for key, value in kwargs.items():
            for i in range(value):
                self.contents.append(key)
        print(self.contents)

    def __str__(self):
        return ', '.join(self.contents)

    def get_contents(self):
        return self.contents

    def draw(self, number):
        all_removed = []
        if(number > len(self.contents)):
            return self.contents
        for i in range(number):
            removed = self.contents.pop(
                int(random.random() * len(self.contents)))
            all_removed.append(removed)
        return all_removed


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    count = 0
    for i in range(num_experiments):
        expected_copy = copy.deepcopy(expected_balls)
        hat_copy = copy.deepcopy(hat)
        colors_gotten = hat_copy.draw(num_balls_drawn)

        for color in colors_gotten:
            if(color in expected_copy):
                expected_copy[color] -= 1

        if(all(x <= 0 for x in expected_copy.values())):
            count += 1

    return count / num_experiments


# Thanks to Landon Schlangen who walked me through this FreeCodeCamp Project.
# The video I watched that (which he was kind enough to take the time to provide)
# is at his youTube channel Landon Schlangen.. https://www.youtube.com/channel/UC4oRFTHw71_CBSHAcCRmV6w
# The link is https://www.youtube.com/watch?v=iIu4ixFlT-w

# Thank you again to everyone that shares their knowledge to help others learn.
#
# 9/22/2021
# Done on VS Code