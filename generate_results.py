import time
import numpy as np
import matplotlib.pyplot as plt
from get_last import last
from reverse_slicing import reverse_slicing
from reverse_method import reverse
from shuffle import random_shuffle
from sort import sort
from sort_mixed import sort_mixed

class Generate_Results():

    def __init__(self, algorithm):
        self.algorithm = algorithm
        self.data = []
        self.x_values = []
        self.y_duration_1 = []
        self.y_duration_2 = []
        self.y_duration_3 = []
        self.y_duration_average = []

    def create_size(self, min, max, steps):
        for i in range(min, max, steps):
            self.x_values.append(i)

    def create_data(self):
        for i in self.x_values:
            self.data.append(np.random.randint(100, size = i))

    def run(self, sample_number):
        for i in self.data:
            start = time.time()
            self.algorithm(i)
            stop = time.time() - start
            self.__record_sample(sample_number, stop)

    def plot_chart(self):
        plt.plot(self.x_values, self.y_duration_average)
        plt.title(self.algorithm)
        plt.ylim(0, 0.00001)
        plt.xlabel('Array Size')
        plt.ylabel('Duration')
        plt.show()

    def __record_sample(self, sample_number, stop):
        if sample_number == 1:
            self.y_duration_1.append(stop)
        elif sample_number == 2:
            self.y_duration_2.append(stop)
        else:
            self.y_duration_3.append(stop)

    def take_average(self):
        self.y_duration_average = np.mean(np.array([self.y_duration_1, self.y_duration_2, self.y_duration_3]), axis=0)

#pick the algorithm
algorithm = reverse

#generate results
generator = Generate_Results(algorithm)

#creates x-values, min, max, step-size
generator.create_size(5000, 105000, 2500)

#random data generation for array of size per x-value
generator.create_data()

#run algorithm and record time - take 3 samples
generator.run(1)
generator.run(2)
generator.run(3)

#take average and plot the chart
generator.take_average()
generator.plot_chart()