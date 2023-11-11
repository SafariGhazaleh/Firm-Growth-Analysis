# Firm-Growth-Analysis
The following assignment script is part of the coursework completed in the lecture "Computational Economics $I$" at TU Chemnitz, presented by Prof. Dr. Heinrich. Comments within the script acknowledge the course context, and where applicable, specify instances where the code is developed based on provided course materials.

## Problem Statement
This assignment explores the conjectured firm growth process using the Kesten process, where firm growth is modeled by the equation $x_{t+1} = \alpha_t x_t + \beta_t$. 
The parameters $\alpha_t$ and $\beta_t$ are sequences of i.i.d. random variables, and the goal is to apply this process to a population of $n = 10000$ hypothetical firms with identical initial sizes $x_0 = 10000$.

## Solution
From the left plot, it is clear that, we have normal distribution. In fact, in this figure, red line represents our given distribution, because we can see the symmetrical shape in some places i.e., it has normal distribution. And based on right plot (semi_log or log_log plot), we encountered Gaussian properties, in the right side of the plot.
 
**Uniform Distribution**
Based on the left plot, we can obviously see the uninform distribution in the bottom of the plot (Blue green) And based on right plot (semilog or log log plot), it also clear that we have strong uniform distribution, the thick band of blue lines in the bottom of the plot represents our given distribution.

**Log normal**
From the left plot, it is clear that, we have log-normal distribution, purple represents our given distribution. In some places, we can see that rightly skewed and we know that if it right skewed is i.e., we have log- normal distribution. And based on left plot (semilog or log log plot), it is not clear about the log-normal distribution, so we conclude that we do not have given distribution according to second plot.

**Right tailed pareto distribution**
The Right tailed pareto distribution will always starts from high and it will have linear downfall, in some cases we witnessed the properties of our given distribution. And based on right plot (semilog or log log plot), it is clear that we do not have the properties of right tailed pareto distribution. We conclude that we do not have the given distribution.
