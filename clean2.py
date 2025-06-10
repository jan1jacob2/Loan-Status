import pandas as pd

loanDF = pd.read_csv('./data/loan.csv')

# One-hot encode purpose column and combine certain values
oneHotDF = pd.get_dummies(loanDF['purpose'], dtype = int)
loanDF.loc[:, 'education_or_small_business'] = oneHotDF['educational'] + oneHotDF['small_business']
loanDF.loc[:, 'major_purchase_or_credit_card'] = oneHotDF['major_purchase'] + oneHotDF['credit_card']

# Create demerits column by combining existing ones
loanDF.loc[:, 'demerits'] = loanDF['delinq.2yrs'] + loanDF['pub.rec'] + loanDF['inq.last.6mths']
loanDF = loanDF.drop(['purpose', 'log.annual.inc', 'dti', 'fico', 'revol.util', 'days.with.cr.line'], axis = 1)

# New Dataset
loanDF.to_csv('./data/loanCleaned.csv')