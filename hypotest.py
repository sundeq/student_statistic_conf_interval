#!/usr/bin/env python3

import random
import math
import statistics

def main():

    n_samples = 200
    displacement = 0.2

    random_floats = [random.random() for x in range(0, n_samples)]
    
    displaced_random_floats = list(map(lambda x : x + displacement, [random.random() for x in range(0, n_samples)]))

    
    STUDENT_CRITICAL_VALUE = 1.960 # Student critical value for confidence level 95% and infinite degrees of freedom
    
    rf_mean = 1 / n_samples * sum(random_floats)
    drf_mean = 1 / n_samples * sum(displaced_random_floats)

    rf_sample_var_terms = [(xi - rf_mean)**2 for xi in random_floats]
    drf_sample_var_terms = [(xi - drf_mean)**2 for xi in displaced_random_floats]

    rf_sample_var = 1 / (n_samples - 1) * sum(rf_sample_var_terms)
    drf_sample_var = 1 / (n_samples - 1) * sum(drf_sample_var_terms)
    
    print("rf mean: {} rf smple var: {}".format(rf_mean, rf_sample_var))
    print("drf mean: {} drf smple var: {}".format(drf_mean, drf_sample_var))

    print("python vals")
    print("py: rf mean: {} rf smple var: {}".format(statistics.mean(random_floats), statistics.variance(random_floats)))
    print("py: drf mean: {} drf smple var: {}".format(statistics.mean(displaced_random_floats), statistics.variance(displaced_random_floats)))

    rf_lower_confidence_bound = rf_mean - (STUDENT_CRITICAL_VALUE * (rf_sample_var / math.sqrt(n_samples)))
    rf_higher_confidence_bound = rf_mean + (STUDENT_CRITICAL_VALUE * (rf_sample_var / math.sqrt(n_samples)))
    
    drf_lower_confidence_bound = drf_mean - (STUDENT_CRITICAL_VALUE * (drf_sample_var / math.sqrt(n_samples)))
    drf_higher_confidence_bound = drf_mean + (STUDENT_CRITICAL_VALUE * (drf_sample_var / math.sqrt(n_samples)))

    print("rf confidence:", [rf_lower_confidence_bound, rf_higher_confidence_bound])
    print("drf confidence:", [drf_lower_confidence_bound, drf_higher_confidence_bound])

if __name__ == '__main__':
    main()
