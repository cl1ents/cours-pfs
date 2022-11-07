# DEBUT
r   = 12000
s   = 1250
e   = 10
rh  = 230

assertionUn = (((365 * 3) / (24 - ( 16 - 8))) * (rh) > r) == (e * s < r)

assertionUnPtUn = (((365 * 3) / (24 - ( 16 - 8))) * (rh) > r) # true
assertionUnPtDeux = (e * s < r) # false

# assertionUn === assertionUnPtUn == assertionUnPtDeux
# assertionUn === (15740.625 > 12000) == (12500 < 12000)
# assertionUn === true == false
# assertionUn === false
print(assertionUn)

assertionDeux = (365 * 3) / (4 - (12 - 8)) * (rh) > r == (e * s < r)

assertionDeuxPtUn = ((365 * 3) / (4 - (12 - 8)) * (rh) > r) # ERREUR!
# assertionDeuxPtUn === ((1095) / (0)) * (230) > 12000
#                        ^^^^^^^^^^^^ DIVISION PAR 0!
assertionDeuxPtDeux = (e * s < r) # false

# assertionDeux === assertionDeuxPtUn == assertionDeuxPtDeux
# assertionDeux === false

def calculPtDeux():
    return (e * s < r)

assertionDeux = (365 * 3) / (4 - (12-8)) * (rh) > r == calculPtDeux()

# FIN