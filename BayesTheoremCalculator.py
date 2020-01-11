#Bayes theorem Calculator

#Configurables:
sensitivity = 0.95    #P(+|D)
specificity = 0.95    #P(-|NoD)
prevalence = 0.01 

#Run after configuration. Output will be P(have disease | test=positive)
numerator=(sensitivity*prevalence)
denominator=(sensitivity*prevalence)+((1-specificity)*(1-prevalence))
prob=numerator/denominator
print(prob)
