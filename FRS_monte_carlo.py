# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load in 

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list the files in the input directory


#below this point is the code that was given - nat
from IPython.display import display, Javascript
import json
from numpy.random import uniform, seed
from numpy import floor
from collections import namedtuple

def _tickets_sold(p, demand_level, max_qty):
        quantity_demanded = floor(max(0, p - demand_level))
        return min(quantity_demanded, max_qty)

def simulate_revenue(days_left, tickets_left, pricing_function, rev_to_date=0, demand_level_min=100, demand_level_max=200, verbose=False):
    if (days_left == 0) or (tickets_left == 0):
        if verbose:
            if (days_left == 0):
                print("The flight took off today. ")
            if (tickets_left == 0):
                print("This flight is booked full.")
            print("Total Revenue: ${:.0f}".format(rev_to_date))
        return rev_to_date
    else:
        demand_level = uniform(demand_level_min, demand_level_max)
        p = pricing_function(days_left, tickets_left, demand_level)
        q = _tickets_sold(demand_level, p, tickets_left)
        if verbose:
            print("{:.0f} days before flight: "
                  "Started with {:.0f} seats. "
                  "Demand level: {:.0f}. "
                  "Price set to ${:.0f}. "
                  "Sold {:.0f} tickets. "
                  "Daily revenue is {:.0f}. Total revenue-to-date is {:.0f}. "
                  "{:.0f} seats remaining".format(days_left, tickets_left, demand_level, p, q, p*q, p*q+rev_to_date, tickets_left-q))
        return simulate_revenue(days_left = days_left-1,
                              tickets_left = tickets_left-q,
                              pricing_function=pricing_function,
                              rev_to_date=rev_to_date + p * q,
                              demand_level_min=demand_level_min,
                              demand_level_max=demand_level_max,
                              verbose=verbose)

def _save_score(score):
    message = {
        'jupyterEvent': 'custom.exercise_interaction',
        'data': {
            'learnTutorialId': 0,
            'interactionType': "check",
            'questionId': 'Aug31OptimizationChallenge',
            'outcomeType': 'Pass',
            'valueTowardsCompletion': score/10000,
            'failureMessage': None,
            'learnToolsVersion': "Testing"
        }
    }
    js = 'parent.postMessage(%s, "*")' % json.dumps(message)
    display(Javascript(js))

def score_me(pricing_function, sims_per_scenario=200):
    seed(0)
    Scenario = namedtuple('Scenario', 'n_days n_tickets')
    scenarios = [Scenario(n_days=100, n_tickets=100),
                 Scenario(n_days=14, n_tickets=50),
                 Scenario(n_days=2, n_tickets=20),
                Scenario(n_days=1, n_tickets=3),
                 ]
    scenario_scores = []
    for s in scenarios:
        scenario_score = sum(simulate_revenue(s.n_days, s.n_tickets, pricing_function)
                                     for _ in range(sims_per_scenario)) / sims_per_scenario
        print("Ran {:.0f} flights starting {:.0f} days before flight with {:.0f} tickets. "
              "Average revenue: ${:.0f}".format(sims_per_scenario,
                                                s.n_days,
                                                s.n_tickets,
                                                scenario_score))
        scenario_scores.append(scenario_score)
    score = sum(scenario_scores) / len(scenario_scores)
    try:
        _save_score(score)
    except:
        pass
    print("Average revenue across all flights is ${:.0f}".format(score))

#someone's pricing function
def pricing_function(days_left, tickets_left, demand_level):
    """Sample pricing function"""
    if days_left == 1:
        price = demand_level - tickets_left
    elif days_left == 2:
        if demand_level > 179:
            price = demand_level - tickets_left
        else:
            price = demand_level - tickets_left/2
    else:
        if days_left > 12:
            if demand_level > 186:
                price = demand_level - 8
            else:
                price = demand_level + 1
        elif days_left > 3:
            if tickets_left/days_left > 2.5:
                if demand_level > 169:
                    price = demand_level - 17
                else:
                    price = demand_level + 1
            else:
                if demand_level > 180:
                    price = demand_level - 20
                else:
                    price = demand_level + 1
        else:
            if demand_level > 169:
                price = demand_level - 13
            else:
                #price = demand_level - tickets_left/days_left
                price = demand_level - 1
    return price

def simulate_revenue(days_left, tickets_left, pricing_function,tickets_over_days, rev_to_date=0, demand_level_min=100, demand_level_max=200, verbose=False):
    if (days_left == 0) or (tickets_left == 0):
        if verbose:
            if (days_left == 0):
                print("The flight took off today. ")
            if (tickets_left == 0):
                print("This flight is booked full.")
            print("Total Revenue: ${:.0f}".format(rev_to_date))
        return rev_to_date
    else:
        demand_level = uniform(demand_level_min, demand_level_max)
        p = pricing_function(days_left, tickets_left, demand_level,tickets_over_days)
        q = _tickets_sold(demand_level, p, tickets_left)
        if verbose:
            print("{:.0f} days before flight: "
                  "Started with {:.0f} seats. "
                  "Demand level: {:.0f}. "
                  "Price set to ${:.0f}. "
                  "Sold {:.0f} tickets. "
                  "Daily revenue is {:.0f}. Total revenue-to-date is {:.0f}. "
                  "{:.0f} seats remaining".format(days_left, tickets_left, demand_level, p, q, p*q, p*q+rev_to_date, tickets_left-q))
        return simulate_revenue(days_left = days_left-1,
                              tickets_left = tickets_left-q,
                              pricing_function=pricing_function,
                              tickets_over_days = tickets_over_days,
                              rev_to_date=rev_to_date + p * q,
                              demand_level_min=demand_level_min,
                              demand_level_max=demand_level_max,
                              verbose=verbose)

def pricing_function_monte_carlo(days_left, tickets_left, demand_level,tickets_over_days):
    """Sample pricing function"""
    if days_left == 1:
        price = demand_level - tickets_left
    elif days_left == 2:
        if demand_level > 179:
            price = demand_level - tickets_left
        else:
            price = demand_level - tickets_left/2
    else:
        if days_left > 12:
            if demand_level > 186:
                price = demand_level - 8
            else:
                price = demand_level + 1
        elif days_left > 3:
            if tickets_left/days_left > tickets_over_days:
                if demand_level > 169:
                    price = demand_level - 17
                else:
                    price = demand_level + 1
            else:
                if demand_level > 180:
                    price = demand_level - 20
                else:
                    price = demand_level + 1
        else:
            if demand_level > 169:
                price = demand_level - 13
            else:
                #price = demand_level - tickets_left/days_left
                price = demand_level - 1
    return price

def score_me_monte_carlo(pricing_function, tickets_over_days, sims_per_scenario=200):
    seed(0)
    Scenario = namedtuple('Scenario', 'n_days n_tickets')
    scenarios = [Scenario(n_days=100, n_tickets=100),
                 Scenario(n_days=14, n_tickets=50),
                 Scenario(n_days=2, n_tickets=20),
                Scenario(n_days=1, n_tickets=3),
                 ]
    scenario_scores = []
    days = []
    tickets = []
    scenario_score_list = []
    for s in scenarios:
        scenario_score = sum(simulate_revenue(s.n_days, s.n_tickets, pricing_function,tickets_over_days)
                                     for _ in range(sims_per_scenario)) / sims_per_scenario
        #print("Ran {:.0f} flights starting {:.0f} days before flight with {:.0f} tickets. "
              #"Average revenue: ${:.0f}".format(sims_per_scenario,
                                                #s.n_days,
                                                #s.n_tickets,
                                                #scenario_score))
        # easier to record data print (days before flight,tickets,average revenue)
        #print(s.n_days,s.n_tickets,scenario_score)                               
        scenario_scores.append(scenario_score)
        days.append(s.n_days)
        tickets.append(s.n_tickets)
        scenario_score_list.append(scenario_score)
    score = sum(scenario_scores) / len(scenario_scores)
    try:
        _save_score(score)
    except:
        pass
    #print(score)
    return [days,tickets,scenario_score_list]

#score_me_monte_carlo(pricing_function_monte_carlo,2.5, sims_per_scenario=200)

def run_monte_carlo():
    for i in range (0,5,1):
        score_me_monte_carlo(pricing_function_monte_carlo,i,sims_per_scenario=200)
        print(i)
def run_monte_carlo2():
    """floats 1-4 step value .1"""
    for i in range (0,51):
        i = i * .1
        score_me_monte_carlo(pricing_function_monte_carlo,i,sims_per_scenario=200)
        print(i)

def run_monte_carlo3():
    variable_value =[]
    days_variable = []
    tickets_variable = []
    scenario_score_variable =[]
    for i in range (0,51):
        i = i*.1
        x = score_me_monte_carlo(pricing_function_monte_carlo,i,sims_per_scenario=200)
        list_days = x[0]
        list_tickets=x[1]
        scenario_score=x[2]
        for day in list_days:
            variable_value.append(i)
            days_variable.append(day)
        for tickets in list_tickets:
            tickets_variable.append(tickets)
        for score in scenario_score:
            scenario_score_variable.append(score)
    return [variable_value,days_variable,tickets_variable,scenario_score_variable]


def print_lists (run_value):
    variable_value = run_value[0]
    days_variable = run_value[1]
    tickets_variable = run_value[2]
    scenario_score_variable = run_value[3]
    for i in range(len(variable_value)):
        print("%f, %f, %f, %f" %(variable_value[i], days_variable[i], tickets_variable[i], scenario_score_variable[i]))

def list_for_pandas (run_value):
    variable_value = run_value[0]
    days_variable = run_value[1]
    tickets_variable = run_value[2]
    scenario_score_variable = run_value[3]
    big_list = []
    for i in range(len(variable_value)):
        mini_list = [variable_value[i],days_variable[i], tickets_variable[i], scenario_score_variable[i]]
        big_list.append(mini_list)
    table = pd.DataFrame(big_list)
    return table

def monte_carlo_df (data_set):
    table = pd.DataFrame(data_set)
    table.transpose()
    return table

#z = run_monte_carlo3()
#monte_carlo_panda_frame = list_for_pandas(z)
#monte_carlo_panda_frame.transpose()
#monte_carlo_panda_frame


