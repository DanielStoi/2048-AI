# 2048-AI
an AI that plays 2048.

dependent on the pygame module.

this project is my solo work, without referencing code from any other similar project.

## Preformance:
the AI can either see 1,2,3 moves ahead. A tree is contructed and then passed through an evaluation algorithm to deduct the apparant value of potential positions.

-by seeing 1 move ahead, ai can generally reach 256,128.

-by seeing 2 moves ahead, ai can generally reach 1024 50% of the time, and below that for the other turns.

-by seeing 3 moves ahead, ai can generally reach 2048 20% of the time, and almost allways reaching 1024.

## Further Improvements:
-AI can be optimised to potentially see more moves ahead via reducing the possibility tree via remove redundances, or to prematurly prune subtrees that are unlikely to lead to good results.

-the evaluation algorithm can be further improved and fine tuned. Polynomial regression can be used to scale the importance of certian observed features within some potential outcome.
