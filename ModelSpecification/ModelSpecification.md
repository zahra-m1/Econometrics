# Test Exercise 3 - Model Specification

**(a)** Use general-to-specific to come to a model. Start by regressing the federal funds rate on the other 7 variables and eliminate 1 variable at a time.

In part(a), I'd like to introduce a Python model `statsmodels` to help solve the statics problems. First, we read the data from text files into a `pandas` `DataFrame`. And then, we use the `ols` function to get OLS Regression Results provided by `statsmodels`.

```python
#! usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
import statsmodels.formula.api as smf

raw_data = pd.read_csv("TestExer3.txt", delimiter = "\t")
print(smf.ols(formula = "INTRATE~INFL+PROD+UNEMPL+COMMPRI+PCE+PERSINC+HOUST", data = raw_data).fit().summary())
```

We can change the formula in `ols` function in order to make the OLS perform better. And the table below shows the result from general-to-specific model. We assume that the lower p-value and higher t-statistic, the variable is more suitable.

table 1: coefficients(p-value) of OLS model by general-to-specific

turns|(7)|(6)|(5)|(4)|(3)|(2)|(1)
-|-|-|-|-|-|-|-
constant|-0.2212(0.367)|-0.2909(0.218)|-0.2401(0.298)|-0.2136(0.356)|-0.1828(0.436)|0.1012(0.666)|1.6421(0.000)
INFL|0.6961(0.000)|0.6933(0.000)|0.7175(0.000)|0.7448(0.000)|0.5950(0.000)|0.7158(0.000)|0.9453(0.000)
PROD|-0.0577(0.148)|-0.0255(0.323)|||||
UNEMPL|0.1025(0.290)||||||
COMMPRI|-0.0055(0.064)|-0.0065(0.021)|-0.0075(0.005)||||
PCE|0.3444(0.000)|0.3686(0.000)|0.3405(0.000)|0.3110(0.000)|0.4732(0.000)|0.3562(0.000)|
PERSINC|0.2470(0.000)|0.2516(0.000)|0.2402(0.000)|0.2569(0.000)|||
HOUST|-0.0194(0.000)|-0.0210(0.000)|-0.0205(0.000)|-0.0215(0.000)|-0.0247(0.000)||

I'd like to choose the model `INTRATE~INFL+COMMPRI+PCE+PERSINC+HOUST`. The reason is that all variables are significant(p-value < 0.05) enough.

**(b)** Use specific-to-general to come to a model. Start by regressing the federal funds rate on only a constant and add 1 variable at a time. Is the model the same as in (a)?

Use the same codes in part (a). By adding the most significant variable one by one, we can get this table below.

table 2: coefficients(p-value) of OLS model by specific-to-general

turns|(1)|(2)|(3)|(4)|(5)|(6)|(7)
-|-|-|-|-|-|-|-
constant|1.6421(0.000)|0.4472(0.022)|0.0212(0.927)|-0.2136(0.356)|-0.2401(0.298)|-0.2909(0.218)|-0.2212(0.367)
INFL|0.9453(0.000)|1.0122(0.000)|0.8754(0.000)|0.7448(0.000)|0.7175(0.000)|0.6933(0.000)|0.6961(0.000)
PROD||||||-0.0255(0.323)|-0.0577(0.148)
UNEMPL|||||||0.1025(0.290)
COMMPRI|||||-0.0075(0.005)|-0.0065(0.021)|-0.0055(0.064)
PCE|||0.1812(0.001)|0.3110(0.000)|0.3405(0.000)|0.3686(0.000)|0.3444(0.000)
PERSINC||0.4360(0.000)|0.3054(0.000)|0.2569(0.000)|0.2402(0.000)|0.2516(0.000)|0.2470(0.000)
HOUST||||-0.0215(0.000)|-0.0205(0.000)|-0.0210(0.000)|-0.0194(0.000)

`PROD` and `UNEMPL` are not significant when added to the model, so we stop. The result is `INTRATE~INFL+PERSINC+PCE+HOUST+COMMPRI`, and the model is the same as in (a).

**(c)** Compare your model from (a) and the Taylor rule of equation (1). Consider R2, AIC and BIC. Which of the models do you prefer?

model|R^2|AIC|BIC
-|-|-|-
(a):`INTRATE~INFL+COMMPRI+PCE+PERSINC+HOUST`|0.637|2912|2939
Taylor:`INTRATE~INFL+PROD`|0.575|3012|3025

The result from part (a) is better, because it has a higher R^2, a lower AIC, and a lower BIC.

**(d)** Test the Taylor rule of equation (1) using the RESET test, Chow break and forecast test (with in both tests as break date January 1980) and a Jarque-Bera test. What do you conclude?

* The RESET tests has the null hypothesis that additional higher order terms have coefficients of 0. The resulting F-statistic is 2.2 with p-value 0.1. We cannot reject the null hypothesis at the desired 95% confidence interval.
* The JB test produces a value of 12.444 and p-value 0.002 suggesting the residual is not normally distributed.
* Testing for a break in January 1980 does produce signficant results such that we can reject the null hypothesis that there is no break.
