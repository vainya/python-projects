slow_wumpus = 1000
fast_wumpus = 1
year = 0


while(slow_wumpus > fast_wumpus):
    
    fast_deaths = 0.0
    slow_deaths = 0.0
    
    slow_wumpus *= 2
    
#    print fast_wumpus
#    print slow_wumpus
    
    fast_wumpus *= 2
    
    slow_deaths = slow_wumpus * 0.4
    fast_deaths = fast_wumpus * 0.3
    
    slow_wumpus -= slow_deaths
    fast_wumpus -= fast_deaths
   
    year +=1 

print "After", year, "years there are", fast_wumpus, "fast wumpuses and", slow_wumpus, "slow wumpuses."

  
