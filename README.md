# Anomaly Detection

Detecting Anomalies in a Univariate Unsupervised Time Series Muscle Movement Data .

### In this project we detect Amomalies in a Time Series Data using the 'lsanomaly' package.

We look at the data at hand, compute and plot the moving averages.
We then look at the residue by plotting it.

The residue plot provides us with a better clarity in order to extract anomalies.

Anomalies are detected and the times at which they occur are stored in numpy arrays.

These arrays are quite unstructured and thus they are clustered.

The longest clusters are then printed and anomalies are most dense in these time series.
