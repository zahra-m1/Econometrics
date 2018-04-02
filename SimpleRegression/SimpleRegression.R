# a)
setwd('E:/Econometrics/SimpleRegression')
TestExer1 <- read.table('TestExer1.txt', head = TRUE)
lm.sol <- lm(Expenditures~Age, data = TestExer1)
summary(lm.sol)

# b)
plot(Expenditures~Age, data = TestExer1, ylim = c(20, 120))
abline(lm.sol)

# c)
AgeMoreThan40 <- TestExer1[which(TestExer1$Age >= 40),]
lm.sol <- lm(Expenditures~Age, data = AgeMoreThan40)
summary(lm.sol)

AgeLessThan40 <- TestExer1[which(TestExer1$Age < 40),]
lm.sol <- lm(Expenditures~Age, data = AgeLessThan40)
summary(lm.sol)