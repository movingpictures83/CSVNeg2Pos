# CSVNeg2Pos
# Language: Python
# Input: CSV (samples)
# Output: screen
# Tested with: PluMA 1.0, Python 2.7

A PluMA plugin that takes a CSV file as input and adds one
to each value.  This is useful for immediately mapping an edge weight range
from [-1,1] to [0,2], for many network algorithms that cannot handle
negative edges.

The mapped edge weights are sent as output to a CSV file as well.
