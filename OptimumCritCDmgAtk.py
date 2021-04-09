import random,timeit
import matplotlib.pyplot as plt

#whiteblind R1 7481
#R5 8421
#skyward 5705
#skyward with 2.75AP 6332

start = timeit.default_timer()

ben = 0                             # Bennett Q
base = 799                         # base atk
N = 100000                          # 100000 points gives us a good enough approximation and can consistently run in 1 second
artifactpower = 2.5                 # this value only takes atk, crit and critdmg into consideration
                                    # each 1% of crit dmg is 0.01, crit rate is 0.02, atk is 4/3
                                    # 2.5 is the minimum requirement for a smooth experience, 3.0 is VERY good,
                                    # 3.5 is GODLY (if we consider only values from artifacts), 4.2 is the theoretical ceiling for artifacts

# these are stats from sources other than artifact primary and substats (ie artifact set bonus, talent, ascension, weapon...)
extatk = 0.3
extcrit = 0
extcdmg = 0

effatk = [0]*N
c = [0]*N
hatk = 0

for i in range(N):
    c[i] = random.uniform(0,0.95-extcrit)
    lim = artifactpower - 2*c[i]
    C = random.uniform(0,lim)
    atk = 3/4*(lim - C) * 1.25
    effatk[i] = ((C+1.5+extcdmg)*(c[i]+.05+extcrit)+(.95-c[i]-extcrit))*((1+atk+extatk)*base*1.35+311+ben + (191+674))
    c[i] = c[i] + extcrit + .05
#above line makes it so that crit in graph shows status menu crit instead of artifact crit
    if effatk[i] > hatk:
        hatk = effatk[i]
        optcrit = c[i]
        optcdmg = C + .5 + extcdmg
        optatk = atk + extatk + 311/base

plt.scatter(c,effatk)
plt.title("Eff. atk against crit rate")
plt.xlabel("Crit rate")
plt.ylabel("Effective attack")

stop = timeit.default_timer()
print("Optimum eff atk is",round(hatk,4))
print("Optimum atk is",optatk)
print("Hence,the optimum character status should be\n",round(optcrit*100,1),"% crit rate\n",round(optcdmg*100),"% crit dmg")
print(base,"(white atk) + ", round(optatk*base),"(green atk)")
print('Time: ', stop - start)
plt.show()
