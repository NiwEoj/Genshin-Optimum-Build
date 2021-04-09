This calculator is more like a simulator than a calculator. It uses N simulations to approximate the answer.
The higher the N value, the better the approximation. 

The damage formula is:
expecteddmg = atk * skilldmg * dmgbonus * critmultiplier * resistance * defence

where atk is the attack stat
skilldmg is the multiplier from talent (ie lv 11 Guoba is 211%, so its 2.11)

dmgbonus is the total of damage bonus + 1
	for example, Xiang Ling has a fire goblet that adds 46.6% pyro dmg and 
	2 pc witch set that gives 15% pyro dmg bonus.
	So, the dmgbonus whenever Xiang Ling uses a pyro move is
		dmgbonus = 0.466 + 0.15 + 1
		         = 1.616

	all sources of "increase X damage by Y%" gets added up in dmgbonus

	another example, Xing Qiu has a passive that gives himself 20% hydro bonus.
	This Xing Qiu also has a goblet that gives him 46.6% hydro ddmg bonus.
	He also has Thundersoother 4 pc set bonus (+35% dmg when attacking enemies
	applied with electro).
	So, when this Xing Qiu uses a hydro move on an enemy applied with electro,
	
	dmgbonus = 0.2 + 0.466 + 0.35 + 1
		 = 2.016

	**Beidou C4, Crescent Pike passive, Fischl C1, Xiang Ling C2 has a different 
	  wording and will not be discussed here

critmultiplier is the expected gain from crit rate and crit dmg
	
	critmultiplier = crit rate * (crit dmg + 1) + (1 - crit rate)

	for example, Xiang Ling has 50% crit rate and 100% crit dmg, so
	critmultiplier = 0.5 * (1 + 1) + (1 - 0.5)
		       = 1.5

resistance is dependent on monsters and has a natural value ranging from
1.2 to 0 (refer to pinned post in discord for more info). Some characters can
reduce resistance like 4 pc Anemo set. Xiang Ling C1 etc

defense is based on monster lv and your lv. If both are same lv, it has a 
value of 0.5. This value most likely plusminus 0.06. This formula more 
complicated, can look it up online on your own.



AS YOU CAN SEE, artifact substats only affect atk and crtimultiplier, so in my
calculator, I combine them into effatk (effective attack)

effatk = atk * critmultiplier

I also assume Goblet is dmgbonus goblet so goblet primary stats is not included
for effatk calculations 


