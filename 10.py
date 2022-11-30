#import required packages
from geoplotlib.utils import read_csv, BoundingBox, DataAccessObject
import geoplotlib  
import pandas as pd

#dot map
data = read_csv('bus.csv')
geoplotlib.dot(data)
geoplotlib.show()

# Heat Map
df = pd.read_csv('flights.csv')
geoplotlib.kde(df, bw=7, cut_below=1e-4)
geoplotlib.set_bbox(BoundingBox.KBH)
geoplotlib.show()

#histogram
data1 = read_csv('metro.csv')
geoplotlib.hist(data1, colorscale='sqrt', binsize=8)
geoplotlib.set_bbox(BoundingBox.DK)
   geoplotlib.show()
