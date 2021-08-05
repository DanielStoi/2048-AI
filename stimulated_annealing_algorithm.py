from random import randint
from classifier_builder import *
from math import exp,log

"""
idea:
run the game over and over again with some random modification on the weights
keep the new weights if an impovement has been made, otherwise keep it with
a certain probability
"""


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
        cur = evaluate_effectivness(alg.function,y)
        alg.weights = new_weights
        eff = evaluate_effectivness(alg.function,y)
        if cur <= eff:
            #print("chose new weight due to it being better")
            w = new_weights
            cur = eff
            print("accepted better scoring weighs")
        else:
            try:
                
                p = exp((log(eff)-log(cur))*i/1000)
                if randint(0,int(p*100))-data["prob"] > 10+ i*1.2:
                    #print("chose new weight due to probability")
                    w = new_weights
                    cur = eff
                    print("randommly accepted worse scoring weighs")
                else:
                    print("rejected new weight")
                    pass
            except:
                print("Overflow occured")
    print("weights: ")
    print(" ".join(map(str,w)))
    
    print("expected score: "+ str(evaluate_effectivness(alg.function,10)))
    return w
                
            
         
data = {"initial_range":100, "max_step":100, "evaluation_strength":10}
iterations = int(input("how many iterations of training: "))
data["evaluation_strength"] = int(input("how many iterations of each classifier should be run in order to gauge their strenghts: "))
data["prob"] = int(input("rareness of switching to lower score probability (integer value divisor): "))
print("expected time in hours: " + str(20*iterations*data["evaluation_strength"]/(60*60)))
stimulated_annealing(iterations,data)
