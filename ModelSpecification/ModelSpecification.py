#! usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
import statsmodels.formula.api as smf

raw_data = pd.read_csv("TestExer3.txt", delimiter = "\t")
method = input("0 for general-to-specific, other for specific-to-general.")
if method == 0:
    print(smf.ols(formula = "INTRATE~INFL+PROD+UNEMPL+COMMPRI+PCE+PERSINC+HOUST", data = raw_data).fit().summary())
    print(smf.ols(formula = "INTRATE~INFL+PROD+COMMPRI+PCE+PERSINC+HOUST", data = raw_data).fit().summary())
    print(smf.ols(formula = "INTRATE~INFL+COMMPRI+PCE+PERSINC+HOUST", data = raw_data).fit().summary())
    print(smf.ols(formula = "INTRATE~INFL+PCE+PERSINC+HOUST", data = raw_data).fit().summary())
    print(smf.ols(formula = "INTRATE~INFL+PCE+HOUST", data = raw_data).fit().summary())
    print(smf.ols(formula = "INTRATE~INFL+PCE", data = raw_data).fit().summary())
    print(smf.ols(formula = "INTRATE~INFL", data = raw_data).fit().summary())
else:
    print(smf.ols(formula = "INTRATE~INFL", data = raw_data).fit().summary())
    print(smf.ols(formula = "INTRATE~INFL+PERSINC", data = raw_data).fit().summary())
    print(smf.ols(formula = "INTRATE~INFL+PERSINC+PCE", data = raw_data).fit().summary())
    print(smf.ols(formula = "INTRATE~INFL+PERSINC+PCE+HOUST", data = raw_data).fit().summary())
    print(smf.ols(formula = "INTRATE~INFL+PERSINC+PCE+HOUST+COMMPRI", data = raw_data).fit().summary())
    print(smf.ols(formula = "INTRATE~INFL+PERSINC+PCE+HOUST+COMMPRI+PROD", data = raw_data).fit().summary())
    print(smf.ols(formula = "INTRATE~INFL+PERSINC+PCE+HOUST+COMMPRI+PROD+UNEMPL", data = raw_data).fit().summary())

#Taylor
print(smf.ols(formula = "INTRATE~INFL+PROD", data = raw_data).fit().summary())
