from random import randint
from classifier_builder import *
from math import exp

"""
idea:
run the game over and over again with some random modification on the weights
keep the new weights if an impovement has been made, otherwise keep it with
a certain probability
"""
#randint(0,10))
def intro_sim_annealing():
    print("simulated annealing is an iterative algorithm which aims to (in this case) tries to optimise the weights of the different classifiers in determining how good a position is")
    print("this algorithm will go through many iterations through the stimulated_annealing algorithm and returns the weights")
    print("these weights can be passed through classifier_builder that processes these weights into the corresponding classifier")


def generate_random_weights(n,r):
    weights = [0]*n
    for i in range(n):
        weights[i] = randint(-1*r,r)
    return weights

def modify_weights_randomly(w,r):
    w = w.copy()
    for i in range(len(w)):
        w[i]+= randint(-1*r,r)
    return w
    

def stimulated_annealing(T,data):
    r = data["initial_range"]
    step = data["max_step"]
    y = data["evaluation_strength"]
    
    w = generate_random_weights(10,r)
    alg = classifier(w)

    cur = evaluate_effectivness(alg.function,y)
    for i in range(1,T):
        print("current expected score: "+str(cur))
        new_weights = modify_weights_randomly(w,step)
        alg.weights = new_weights
        eff = evaluate_effectivness(alg.function,y)
        if cur <= eff:
            #print("chose new weight due to it being better")
            w = new_weights
            cur = eff
        else:
            p = exp((cur-eff)/(i*10000))
            if randint(0,int(p*1000))>500:
                #print("chose new weight due to probability")
                w = new_weights
                cur = eff
            else:
                pass
                #print("rejected new weight")
    print("weights: ")
    print(" ".join(map(str,w)))
    
    print("expected score: "+ str(evaluate_effectivness(alg.function,y*5)))
    return w
                
            
print()           
data = {"initial_range":100, "max_step":5, "evaluation_strength":1}
iterations = int(input("how many iterations of training: "))
print("expected time in hours: " + str(20*iterations/(60*60)))
stimulated_annealing(iterations,data)

