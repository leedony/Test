# Input these aa sequences, calculate pI values using different pKa sets
# Compare the predicted values and expermential values
# Find the best pKa set or get a expression with some of these sets
# Also, using Lasso or other regression to build a model to predict the pI value
"""
predict PI calculator here
Include:  (1) predict_pI_values based on various pKa datasets
          (2) we mostly focus on Sillero and Nozaki methods
Input: file,  VH and VL in csv
       outdir,  output directory
Ouput: a single file

Author: Dongyu Li
Date: 2023-02-09
"""


from isoelectric import ipc
import pandas as pd
import isoelectric
import sys
import os

pkas = list(ipc.scales.keys())

file = sys.argv[1]
outdir = sys.argv[2]
tag = sys.argv[3]
df = pd.read_csv(file)

CH = 'ASTKGPSVFPLAPSSKSTSGGTAALGCLVKDYFPEPVTVSWNSGALTSGVHTFPAVLQSSGLYSLSSVVTVPSSSLGTQTYICNVNHKPSNTKVDKKVEPKSCDKTHTCPPCPAPELLGGPSVFLFPPKPKDTLMISRTPEVTCVVVDVSHEDPEVKFNWYVDGVEVHNAKTKPREEQYNSTYRVVSVLTVLHQDWLNGKEYKCKVSNKALPAPIEKTISKAKGQPREPQVYTLPPSRDELTKNQVSLTCLVKGFYPSDIAVEWESNGQPENNYKTTPPVLDSDGSFFLYSKLTVDKSRWQQGNVFSCSVMHEALHNHYTQKSLSLSPGK**'
CL = 'RTVAAPSVFIFPPSDEQLKSGTASVVCLLNNFYPREAKVQWKVDNALQSGNSQESVTEQDSKDSTYSLSSTLTLSKADYEKHKVYACEVTHQGLSSPVTKSFNRGEC**'

if tag == '1':
    df['Full'] = df['VH'] + CH + df['VL'] + CL
else:
    df['Full'] = df['VH'] + df['VL']

total = {}
for i in df.index:   
    predict_values = {}
    for pka in pkas:
        predict_values[pka] = ipc.predict_isoelectric_point(df.loc[i,'Full'].replace('*',''),pka)
    total[df.loc[i,'ID']]=predict_values

result = pd.DataFrame.from_dict(total,orient='index')

outfile = os.path.join(outdir,'predict_PI_values.csv')
result.to_csv(outfile)