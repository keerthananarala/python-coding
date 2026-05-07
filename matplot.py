import matplotlib.pyplot as plt
import numpy as np
overs=np.arrange(1,11)
scores=[9,4,7,8,24,7,8]
plt.bar(overs,scores)
plt.title("INDIA SCORE OVER WISE")
plt.xlabe("OVERS FROM 1 TO 10")
plt.ylable("RUN BASED ON OVERS")
plt.xtickes(OVERS)
plt.grid(axis='y',linestyle="__")
plt.show()
