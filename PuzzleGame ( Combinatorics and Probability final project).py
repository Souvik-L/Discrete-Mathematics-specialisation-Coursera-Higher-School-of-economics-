#Q1 Solve
def count_wins(dice1, dice2):
    assert len(dice1) == 6 and len(dice2) == 6
    dice1_wins = 0
    dice2_wins = 0
    for i in dice1:
      for j in dice2:
        if i > j :
          dice1_wins+=1
        elif j > i:
          dice2_wins +=1
          
          
    
    # write your code here

    return (dice1_wins, dice2_wins)
dice1 =  [1, 1, 6, 6, 8, 8]
dice2 = [2, 2, 4, 4, 9, 9]
print(count_wins(dice1,dice2))

#Q2 Solve
def count_wins(dice1, dice2):
    assert len(dice1) == 6 and len(dice2) == 6
    dice1_wins = 0
    dice2_wins = 0
    for i in dice1:
      for j in dice2:
        if i > j :
          dice1_wins+=1
        elif j > i:
          dice2_wins +=1
          
    return (dice1_wins, dice2_wins)

def find_the_best_dice(dices):
    assert all(len(dice) == 6 for dice in dices)
    

    # write your code here
    # use your implementation of count_wins method if necessary
    
    if len(dices) != 3:
      return -1
    elif len(dices)==3:
      dice_1 = dices[0]
      dice_2 = dices[1]
      dice_3 = dices[2]
      a,b = count_wins(dice_1, dice_2)
      c,d = count_wins(dice_2, dice_3)
      e,f = count_wins(dice_3, dice_1)
      if a>b:
        round_1_winner = dice_1
      else:
        round_1_winner = dice_2
      if c>d:
        round_2_winner = dice_2
      else:
        round_2_winner = dice_3
      if e>f:
        round_3_winner = dice_3
      else:
        round_3_winner = dice_1
        mid_level = []
        if round_1_winner == round_2_winner:
          mid_level.append(round_1_winner)
        elif round_2_winner == round_3_winner:
          mid_level.append(round_2_winner)
        elif round_3_winner == round_1_winner:
          mid_level.append(round_3_winner)
        if len(mid_level) != 1:
          return -1
        for i in range(len(dices)):
          if dices[i] == mid_level[0]:
            return i
        
#Q3 Solve

def count_wins(dice1, dice2):
    assert len(dice1) == 6 and len(dice2) == 6
    dice1_wins = 0
    dice2_wins = 0
    for i in dice1:
      for j in dice2:
        if i > j :
          dice1_wins+=1
        elif j > i:
          dice2_wins +=1
          
          
    
    # write your code here

    return (dice1_wins, dice2_wins)


def compute_strategy(dices):
    assert all(len(dice) == 6 for dice in dices)

    strategy = dict()
    
    my_dice = []
    op_dice = []
    combi = []
    mid_time = []    
    # write your code here
    i = 0
    while i<len(dices):
      j = i + 1
      while j < len(dices):
        a , b = count_wins(dices[i],dices[j])
        if a>b:
          mid_time.append(dices[i])
          my_dice.append(i)
          op_dice.append(j)
        elif b>a:
          mid_time.append(dices[j])
          my_dice.append(j)
          op_dice.append(i)
          
        else:
          mid_time.append(dices[i])
        
        j += 1
      i+=1
    
    for i in range(len(op_dice)):
      combi.append((op_dice[i],my_dice[i]))
    fog  = dict()
    counts = []
    fin = []
    nan = []
    for i in mid_time:
      if str(i) not in fog:
        fog[str(i)] = 1
      else:
        fog[str(i)] += 1
    for a in fog.values():
      counts.append(a)
    counts.sort()
    tik = counts[-1]
    for (a,b) in fog.items():
      if b==tik:
        fin.append(a)
    if len(fin)!=1:
      strategy["choose_first"] = False
      
    else:
      strategy["choose_first"] = True
      kis = fin[0].split(',')
      kis[0] = kis[0][1]
      kis[-1] = kis[-1][1]
      for p in kis:
        n = int(p.strip())
        nan.append(n)
      for i in range(len(dices)):
        if dices[i] == nan:
          vir = i
          strategy["first_dice"] = vir   
    for (a,b) in combi:
      if a not in strategy.keys():
        strategy[a] = b
  
      
    
      
        
    return strategy
compute_strategy( [[1, 1, 4, 6, 7, 8], [2, 2, 2, 6, 7, 7], [3, 3, 3, 5, 5, 8]])        
