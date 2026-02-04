#aggreagtion 

import pandas as pd

# Sample Data
df = pd.DataFrame({
    'Category': ['A', 'A', 'B', 'B', 'C'],
    'Value': [10, 20, 30, 40, 50]
})

# Aggregate: Group by 'Category' and find the mean of 'Value'
result = df.groupby('Category').agg('mean')
print(result)