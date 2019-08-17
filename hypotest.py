#!/usr/bin/env python3

import random
import math
import statistics
import numpy

def main():

    n_samples = 1000
    dist_mean = 0
    displacement = 0.05
    right_displaced_dist_mean = dist_mean + displacement
    random_std_dev = random.random()
    normal_random_floats = numpy.random.normal(dist_mean, random_std_dev, n_samples)
    
    normal_displaced_random_floats = numpy.random.normal(right_displaced_dist_mean, random_std_dev, n_samples)
     
    print("nrf confidence interval:", student_confidence_interval(normal_random_floats))
    print("ndrf confidence interval:", student_confidence_interval(normal_displaced_random_floats))

    print("absolute t statistic: {}".format(abs(t_test_two_tails(normal_random_floats, 0))))
    print("absolue t statistic: {}".format(abs(t_test_two_tails(normal_random_floats, 2))))

'''
Given a null hypothesis value, calculates the t-test test statistic.
'''
def t_test_two_tails(samples, mu0):
    n_samples = len(samples)
    xbar = sample_mean(samples, n_samples)
    s2 = sample_variation(samples, xbar, n_samples)
    sample_std_dev = math.sqrt(s2)
    print("xbar {}".format(xbar))
    return (xbar - mu0) / (sample_std_dev / math.sqrt(n_samples))

'''
Calculates confidence interval using Student's t-distribution. We assume that the number of samples is large when choosing critical value.
'''
def student_confidence_interval(samples):
    n_samples = len(samples)
    STUDENT_CRITICAL_VALUE = 1.960 # Student critical value for confidence level 95% and infinite degrees of freedom
    
    xbar = sample_mean(samples, n_samples) 
    s2 = sample_variation(samples, xbar, n_samples)
    sample_std_dev = math.sqrt(s2)

    lower_confidence_bound = xbar - (STUDENT_CRITICAL_VALUE * (sample_std_dev / math.sqrt(n_samples)))
    upper_confidence_bound = xbar + (STUDENT_CRITICAL_VALUE * (sample_std_dev / math.sqrt(n_samples)))
    return [lower_confidence_bound, upper_confidence_bound]

def sample_mean(samples, n_samples):
    return sum(samples) / n_samples

def sample_variation(samples, sample_mean, n_samples):
    sample_var_terms = [(xi - sample_mean)**2 for xi in samples]
    return sum(sample_var_terms) / (n_samples - 1)

if __name__ == '__main__':
    main()
