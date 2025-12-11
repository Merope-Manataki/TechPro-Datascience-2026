import math
from scipy import stats
import numpy as np 

popMean_f = 100

sampleMean_f = 97
sampleStd_f = 2.5
n=50
df = n-1
# -----

tStat_f = (sampleMean_f - popMean_f)/ ( sampleStd_f / math.sqrt(n) )

pValue_f = 2* (1-stats.t.cdf(np.abs(tStat_f),df))
print(tStat_f)
print(pValue_f)

