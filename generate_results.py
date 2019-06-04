import time
import numpy as np
import matplotlib.pyplot as plt
from get_last import last
from reverse import reverse
from shuffle import random_shuffle
from sort import sort

class Generate_Results():

    def __init__(self, algorithm):
        self.algorithm = algorithm
        self.data = []
        self.x_values = []
        self.y_duration = []

    def create_size(self, min, max, steps):
        for i in range(min, max, steps):
            self.x_values.append(i)

    def create_data(self):
        for i in self.x_values:
            self.data.append(np.random.randint(100, size = i))

    def run(self):
        for i in self.data:
            start = time.time()
            self.algorithm(i)
            stop = time.time() - start
            self.y_duration.append(stop)


    def plot_chart(self):
        plt.plot(self.x_values, self.y_duration)
        plt.xlabel('Array Size')
        plt.ylabel('Duration')
        plt.show()


#pick the algorithm
algorithm = reverse

#generate results
generator = Generate_Results(algorithm)

#creates x-values
generator.create_size(5000, 105000, 2500)

#random data generation for array of size per x-value
generator.create_data()

#run algorithm and record time
generator.run()

#plot the chart
generator.plot_chart()