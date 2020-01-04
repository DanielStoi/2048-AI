from ai2048 import score
def function(subtrees):
    adv = 0
    c=0
    k= [score(i.cur.board) for i in subtrees]
    mmm= str(max(k))
    mm=str(min(k))
    k = []
    corr={mmm:1,mm:0.1}
    for i,v in zip(subtrees,k):
        adv+=i.value()*corr[v]
        c+=corr[v]
    if len(subtrees) == 0:
        return 0
    return int(adv/c)
