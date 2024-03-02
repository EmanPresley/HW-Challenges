# Module 12 Report Template

## Overview of the Analysis

This analysis is intended to predict the likelihood of a safe loan or a high risk loan based upon various data such as
the amount of the loan, the interest rate, and the borrower's income. For this analysis I used Linear Regression, ADA Boost,
and Gradient Boosting Classifier, with varying rates of success. Using these models, I was able to build a model that has a 
minimum precision of 84% and an accuracy of 99%.

## Results

* Linear Regression: The linear regression model yielded a result of 99% accurate predictions of a good loan, and 89% accuracy 
on bad loans. While these accuracies seem very good, the overall model still has plenty of room for error as the good to bad 
ratio of loans were heavily lop sided with 18765 good loans in the data to analyze versus the 619 bad loans to compare to. The 
confusion matrix yielded 18655 correct good loan predictions and 583 correct bad loan predictions.


* ADA Booster: The ADA booster also gave a 99% accurate prediction rate on good loans and a 92% on bad loans. This is a slightly better model than the Linear regression, but could still benefit from improvements such as scaling. The confusion matrix showed that the model successfully predicted 18650 good loans and 615 bad loans. While the total good loans were slightly less accurate, the model did a better job at predicting those who shouldn't be given loans. 


*Gradient Booster: The last model also had very close accuracies on 99% good loans and 91% bad loans. These percentages put both the ADA and Gradient models neck in neck for candidates being top prediction models. The confusion matrix on the gradient gave a total of 18652 correct guesses on good loans and 613 guesses on bad loans. This to offset the ADA model in regard to guessing who to give good loans out to versus who probably shouldn't. 

## Summary

In summary, I would advise scaling the data and then rerunning the models as well as trying some others just for good measure. But as it stands, I would recommend the Gradient model for it's better predictability on good loans. Also, I checked how the models placed importance on the different data available, and the ADA model seemed to base 100% of it's decision on the interest rate alone. Whereas the gradient model had a more diverse decision base with 84% of its decision based on the interest rate, 8% on the borrower's income, and 4% on the loan size with some smaller percentages being divided among the other catagories. I would much prefer a broader spectrum over the hyper focusing on just one aspect of a loan. 