import random,math,timeit,numpy
import matplotlib.pyplot as plt


start = timeit.default_timer()

ben = 670*.7                             # Bennett Q
base = 667                          # base atk
ovbase = 2406                       # overloaded base dmg, scales with char lv; 1893 at lv 80, 2406 at lv 90
N = 100000                          # use 1000000 for better accuracy
artifactpower = 2.8                 # considers atk, cdmg, crit and em; 1 em is 62.2/18700
                                    # each 1% of crit dmg is 0.01, crit rate is 0.02, atk is 4/300
                                    # 2.5
                                    # 4.59 is the theoretical ceiling for artifacts
skldmg = 2.42*3                     # skill damage
dmgbns = 1.46+.15                       # damage bonus

extatk = 0.25 + .12 + .2
extcrit = 0
extcdmg = 0
extem = 165
extreactv = 0                       # extra vape reaction multiplier
extreacto = 0                       # extra overloded reaction multiplier

dmg = [0]*N
ovdmg = [0]*N
c = [0]*N
hdmg1 = 0
hdmg2 = 0

for i in range(N):
    em = random.uniform(0,474)
    lim = artifactpower - em*62.2/18700
    if lim >= (0.95-extcrit)*2:
        c[i] = random.uniform(0, .95-extcrit)
    else:
        c[i] = random.uniform(0, lim)/2
    C = random.uniform(0,lim-2*c[i])
    atk = 3/4*random.uniform(0,lim-2*c[i]-C)
    dmg[i] = ((C+1.5+extcdmg)*(c[i]+.05+extcrit)+(.95-c[i]-extcrit))*((1+atk+extatk)*base+311+ben)*(skldmg)*(dmgbns)*(2.78*(em+extem)/(em+1400+extem)+1+extreactv)*1.5*.5
    ovdmg[i] = ((C + 1.5 + extcdmg) * (c[i] + .05 + extcrit) + (.95 - c[i] - extcrit)) * ((1 + atk + extatk) * base + 311 + ben)*skldmg*dmgbns*.5 + ovbase * (6.66 * (em + extem) / (em + 1400 + extem) + 1 + extreacto)
    if dmg[i] > hdmg1:
        hdmg1 = dmg[i]
        optcrit1 = c[i]
        optcdmg1 = C
        optatk1 = atk
        optem1 = em
    if ovdmg[i] > hdmg2:
        hdmg2 = ovdmg[i]
        optcrit2 = c[i]
        optcdmg2 = C
        optatk2 = atk
        optem2 = em

optcrit1 = optcrit1 + .05 + extcrit
optcdmg1 = optcdmg1 + .5 + extcdmg
optatk1 = optatk1 + extatk + 311/base
optem1 = optem1 + extem

optcrit2 = optcrit2 + .05 + extcrit
optcdmg2 = optcdmg2 + .5 + extcdmg
optatk2 = optatk2 + extatk + 311/base
optem2 = optem2 + extem

plt.subplot(1,2,1)
plt.scatter(c,dmg)
plt.title("Eff. dmg against crit rate for Vapes")
plt.xlabel("Crit rate")
plt.ylabel("Effective damage")

plt.subplot(1,2,2)
plt.scatter(c,ovdmg)
plt.title("Eff. dmg against crit rate for Overloaded")
plt.xlabel("Crit rate")
plt.ylabel("Effective damage")

stop = timeit.default_timer()
print("Highest dmg for vape is",round(hdmg1))
print("Optimum atk is",round(optatk1,4), ", em is",round(optem1))
print("Hence,the optimum character status should be\n",round(optcrit1*100,1),"% crit rate\n",round(optcdmg1*100),"% crit dmg")
print(base,"(white atk) + ", round(optatk1*base),"(green atk) = ",base+round(optatk1*base) ,"\n")

print("Highest dmg for overloaded is",round(hdmg2))
print("Optimum atk is",round(optatk2,4), ", em is",round(optem2))
print("Hence,the optimum character status should be\n",round(optcrit2*100,1),"% crit rate\n",round(optcdmg2*100),"% crit dmg")
print(base,"(white atk) + ", round(optatk2*base),"(green atk)= ",base+round(optatk2*base) ,"\n")
print('Time: ', stop - start)
plt.show()