import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

bugfile = 'stinkbug.png'

# read image
bug = mpimg.imread(bugfile)
print bug

imgplot = plt.imshow(bug)
plt.show()
