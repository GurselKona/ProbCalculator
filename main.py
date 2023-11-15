import copy
import random
# Consider using the modules imported above.


class Hat:

    """ This class defines a hat with colored balls in it and its draw() method.
    The number and colors of balls are determined at initiation. Draw() method simulates
    the action of drawing certain number of balls from the hat. """

    def __init__(self, **kwargs):
        if len(kwargs) < 1:
            raise Exception("The hat  cannot be empty.")
        self.balls = kwargs
        self.contents = []
        for k, v in self.balls.items():
            self.contents += [k] * v

    def draw(self, number_balls_drawn):
        if number_balls_drawn >= len(self.contents):
            return self.contents
        drawn = random.sample(self.contents, number_balls_drawn)
        for item in drawn:
            self.contents.remove(item)
        return drawn


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

    """ The function calculates the probability of getting at least a number of colored balls
    from the hat created by above class, via user-defined number of experiments."""

    n = num_experiments
    mm = 0
    for _ in range(n):  # loop for experiments
        hat_current = copy.deepcopy(hat)  # to  keep original hat in place
        balls_drawn = hat_current.draw(num_balls_drawn)  # draw
        counts = {}
        # List of drawn balls is being converted to a dictionary, color as key and
        # counts as values
        for item in balls_drawn:
            if item in counts:
                counts[item] += 1
            else:
                counts[item] = 1
        match = True  # a dummy control variable, it will be set to false if no match occurs.
        m = 0  # counter to count number of matches
        for key in expected_balls:  # the loop for checking matches
            if key not in counts or counts[key] < expected_balls[key]:  #
                match = False
                break
            else:
                m += 1  # number of matching keys
        # checking the number of matches with the number of keys required to pass
        if m == len(expected_balls):
            mm += 1  # when  all keys pass the test. "mm" is kept for the entire experiment.
    return mm/n

if __name__ == '__main__':
    try:
        hat = Hat(blue=3,red=2,green=6)
        # print(hat.balls)
        # print(hat.contents)
        # print(hat.draw(2))
        # print(hat.contents)
        print(experiment(hat, {'blue':2, 'green':1}, 4,1000))
    except Exception as e:  # Try to catch if an empty hat is created.
        print(e)

