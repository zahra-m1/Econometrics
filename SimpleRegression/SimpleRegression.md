# TestExer1-SimpleRegression

**(a) Use all data to estimate the coefficients a and b in a simple regression model, where expenditures is the dependent variable and age is the explanatory factor. Also compute the standard error and the t-value of b.**

In this report, I will utilize R programming language to solve the whole problems. The code and results are displayed below.

```R
setwd('E:/Econometrics/SimpleRegression')
TestExer1 <- read.table('TestExer1.txt', head = TRUE)
lm.sol <- lm(Expenditures~Age, data = TestExer1)
summary(lm.sol)
```

![part_a](https://github.com/lirenjie95/Econometrics/blob/master/SimpleRegression/pics/a.png)

In question (a), the equation could be *E_i=114.24111-0.33360A_i+ε_i*
t-value= -3.498,Standard.Error=0.09537

**(b) Make the scatter diagram of expenditures against age and add the regression line y = a + bx of part (a) in this diagram. What conclusion do you draw from this diagram?**

```R
plot(Expenditures~Age, data = TestExer1, ylim = c(20, 120))
abline(lm.sol)
```

![part_b](https://github.com/lirenjie95/Econometrics/blob/master/SimpleRegression/pics/b.png)

Type the code showed above into the RStudio (the IDE of R programming language) Console, and then the result will be seen as the picture above.

Conclusion: With age going up, expenditure in travelling goes down, but the tendency is quite mild.

**(c) It seems there are two sets of observations in the scatter diagram, one for clients aged 40 or higher and another for clients aged below 40. Divide the sample into these two clusters, and for each cluster estimate the coefficients a and b and determine the standard error and t-value of b.**
 
```R
AgeMoreThan40 <- TestExer1[which(TestExer1$Age >= 40),]
lm.sol <- lm(Expenditures~Age, data = AgeMoreThan40)
summary(lm.sol)
```

![part_c1](https://github.com/lirenjie95/Econometrics/blob/master/SimpleRegression/pics/c1.png)

```R
AgeLessThan40 <- TestExer1[which(TestExer1$Age < 40),]
lm.sol <- lm(Expenditures~Age, data = AgeLessThan40)
summary(lm.sol)
```

![part_c2](https://github.com/lirenjie95/Econometrics/blob/master/SimpleRegression/pics/c2.png)

For those clients aged 40 or more, the equation could be *E_i=88.8719+0.1465A_i+ε_i*,t-value= 0.742,Standard.Error=0.1974

For those clients aged below 40, the equation could be *E_i=100.23228+0.19797A_i+ε_i*,t-value= 4.46,Standard.Error=0.04438

**(d) Discuss and explain the main differences between the outcomes in parts (a) and (c). Describe in words what you have learned from these results.**

The main differences between the outcomes in parts (a) and (c) are as follows: 

1. Coefficient of b

In part (a), the coefficient of b is negative, which means that the increase in the age leads to a decline in daily expenditures during holidays. However, in part (c), for the clients aged 40 or higher and for clients aged below 40, the coefficient of b is positive. This implies that the increase in age leads to an increase in daily expenditures during holidays in both sets. 

2. Standard Error of b 

The standard error of b in part (a) is 0.095 while that of part (c) for the clients aged 40 or higher is 0.197 while that of clients aged below 40 is 0.044. It is clear that the standard error of b for the clients aged below 40 is the least hence implying that the estimate for b for the data for clients aged below 40 is more significant. 

3. t-value of b 

The absolute t-value of b in part (a) is slightly above 2 (3.498) implying that 𝛽 is not equal to zero and hence we reject𝑯𝒐: 𝜷 = 𝟎, implying there is a relationship between the average daily expenditures on holidays and the age in years. In part (c), for the clients aged 40 or higher, the absolute t-value of b is clearly below 2 (0.742) and therefore we accept 𝑯𝒐: 𝜷 = 𝟎 implying no relationship between the average daily expenditures on holidays and ages of clients in 40 or higher. In part (c), for the clients aged below 40, the absolute t-value of b is clearly above 2 (4.460) and higher than those in part (a) and part (c) for the clients aged 40 or higher. We therefore reject the null hypothesis that𝑯𝒐: 𝜷 = 𝟎, hence implying a relationship between the average daily expenditures for clients and the ages of clients below 40. 
