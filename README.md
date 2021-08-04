# 2048-AI
![game](https://github.com/DanielStoi/2048-AI/blob/master/ai2048.PNG)

an AI that plays 2048. 

User can control the "strength" of the AI.

This project includes a replica of the 2048 game include a GUI dependent on the pygame module. Run "run2048.py" to execute code, and "stimulated_annealing_algorithm.py" to train a classifier

this project is my solo work, without referencing code from any other similar project.

## Preformance:
#### Version 3 (2021):

- this version has an additional machine learning classifier that uses supervised learning (particularly the simulated annealing algorithm) to train a learning algorithm. 

- by using the AI classifier on level 3, the AI is able to reach 2048 around 70% of the time. This is with just 30 minutes of training and almost instant execution.

- hard coded algorithm has similar performance to version 2, reaching 2048 around 20% of the time.

- the machine learning algorithm only controls 10 weights, so there is a natural limit to how well it can perform. Optimising the constraints in itself is also a problem. 

- try weights 93 200 -102 -190 -14 110 -39 146 29 118 for a good performance



#### Version 2 (2020):
- by seeing 2 moves ahead, AI is almost allways able to reach 1024

- advanced AI dynamically ajusts the amount of moves it can see ahead, from 2-4, allowing it to reach 2048 20% of the time



#### Version 1 (2020):
the AI can either see 1,2,3 moves ahead. A tree is constructed and then passed through an evaluation algorithm to deduct the apparant value of potential positions.

- by seeing 1 move ahead, ai can generally reach 256,128.

- by seeing 2 moves ahead, ai can generally reach 1024 50% of the time, and below that for the other turns.

- by seeing 3 moves ahead, ai can generally reach 2048 20% of the time, and almost allways reaching 1024.

## Further Improvements:
- AI can be optimised to potentially see more moves ahead via reducing the possibility tree's width via remove redundances, or to prematurly prune subtrees that are unlikely to lead to good results.

- the evaluation algorithm can be further improved and fine tuned. Polynomial regression can be used to scale the importance of certian observed features within some potential outcome.
