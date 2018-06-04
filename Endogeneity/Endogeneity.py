#! usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
import statsmodels.formula.api as smf

raw_data = pd.read_csv("TestExer4.txt")
print(smf.ols(formula = "logw~educ+exper+I(exper**2)+smsa+south", data = raw_data).fit().summary())
print(smf.ols(formula = "educ~age+I(age**2)+nearc+daded+momed", data = raw_data).fit().summary())