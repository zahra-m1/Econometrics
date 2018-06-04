# 4 Endogeneity
**(a)** Use OLS to estimate the parameters of the model：logw = β_1 + β_2educ + β_3exper + β_4exper^2 + β_5smsa + β_6south + ε. Give an interpretation to the estimated β_2 coefficient.

```python
import pandas as pd
import statsmodels.formula.api as smf

raw_data = pd.read_csv("TestExer4.txt")
print(smf.ols(formula = "logw~educ+exper+I(exper**2)+smsa+south", data = raw_data).fit().summary())
```

![OLS_1](https://github.com/lirenjie95/Econometrics/blob/master/Endogeneity/OLS_logw.png)

> We run the python code above and get the result as a picture. we know that e^(β_2) = 1.085, so β_2 can be interpreted as "a person who has received one more year education is likely to earn 8.5% wage than others, if they are the same in other aspects".

**(b)** OLS may be inconsistent in this case as educ and exper may be endogenous. Give a reason why this may be the case. Also indicate whether the estimate in part (a) is still useful.

> Predictors `educ` and `exper` may be endogenous because of omitted factors - factors which we don't observe that are related to `educ` and `exper`, and they will influence the wage.
>
> Such as the factor `major`. A person who learns law or medical will spend more years in school, and also the `major` is related to jobs and income. As the result, the estimators for β_2 and β_3 may be inconsistent.
>
> Estimates from part (a) are not useful when having endogeneity.

**(c)** Give a motivation why age and age^2 can be used as instruments for exper and exper^2.

> The older a person is, the more years experience he will have. However, a person's age is not related to the salary he gets.

**(d)** Run the first-stage regression for educ for the two-stage least squares estimation of the parameters in the model above when age, age^2, nearc, dadeduc, and momeduc are used as additional instruments. What do you conclude about the suitability of these instruments for schooling?

```python
print(smf.ols(formula = "educ~age+I(age**2)+nearc+daded+momed", data = raw_data).fit().summary())
```

![OLS_2](https://github.com/lirenjie95/Econometrics/blob/master/Endogeneity/OLS_educ.png)

> These instruments are suitable for predicting educ. And all of them are significant.

**(e)** Estimate the parameters of the model for log wage using two-stage least squares where you correct for the endogeneity of education and experience. Compare your result to the estimate in part (a).

> For 2SLS, the parameter for education is 0.09 vs 0.08 for OLS. Parameters for experience don't seem to change.

**(f)** Perform the Sargan test for validity of the instruments. What is your conclusion?

> n*R^2 is distributed as χ2(m−k), where m is the number of instruments and k is the number of explanatory variables.
>
> * m=6 : const, age, age2, nearc, daded, momed
>
> * k=6 : const, educ, exper, exper2, smsa, south
>
> Since m=k, we cannot perform the Sargan test, it only can be performed when m>k.
>
> R^2 = 0.0013 of ε and the formula in part (a). Because the p-values of the coefficients are small and R^2 is also small, we may conclude that performing 2SLS still makes sense, even though we cannot formally test the validity of the instruments.