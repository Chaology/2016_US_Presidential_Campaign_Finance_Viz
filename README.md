# 2016 Presidential Campaign Finance Across States: Trump vs. Clinton

![](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSeFTF2qomLgdjhO_aavdigcPBSFQWLfVQBQD0t0W1ZYZsI8Jf0Bg)

Author: Chao Pan
Date: Aug 4, 2017

## Summary

I chose to create a visualization of 2016 Presidential Campaign Finance, specifically on Trump and Clinton. The finance amount ratio in each state basically accords with state political affliations. Clinton has a advantage on the total finance amount. Different states have different patterns in terms of donor composition.

The dataset is from [fec.gov](http://classic.fec.gov/disclosurep/PDownload.do).

[Here](https://public.tableau.com/views/donor_0/Story1?:embed=y&:display_count=yes&publish=yes) is the final version of the visualization. 

The previous version can be accessed [here](https://public.tableau.com/views/PresidentialCampaignFinanceAcrossStatesTrumpvs_Clinton/Story1?:embed=y&:display_count=yes&publish=yes).

## Design

I started the process by using python to do some format cleaning and added a merged dataframe file including the donor records of both Trump and Clinton. After making sure the data is in tidy format, I applied Tableau to create a dashboard and used story line to illustrate the oberservation across states and picked a representative state for each party. 

### Dashboard

##### Plot 1

The first plot is the US map plot colored by the ratio of finance amount between the two candidates. I blended the trump and clinton data then calculated the ratio of received donation amount in each state between Trump and Clinton. It turns out that the finance ratio in each state in the most part accords with state political affiliations (Republican: Red, Democrates: Blue).

##### Plot 2

The second plot is the total finance amount of Trump and Clinton. I initially chose the pie chart but I received the feedback that pie chart is not a good visualization practice in this case which can be visually misleading and not accurate. So in the final version I chose bar chart to reflect the both the absolute numeric value and relative level of the finance amount for each. 

##### Plot 3
The third plot is the time series plot reflects the amount of finance for each candidate through time. Initially I chose sum of each week as the measurement but I got the feedback that for this type of data, moving average is a better measurement. So I used moving average amount in the final version. In addition, I added the legend for the two candidate to make readers recognise the indictor for each line easily.

##### Plot 4 
The forth plot is the top 5 occupation types of donors for each candidate. During the process, I excluded the null value, type named "information required" and the retirement type as they are not informative occupation types. I also got the feedback that the label for y axis is not necessary in this case so I removed it in the final version.

### Storyline

##### Card 1
The first card is the general picture. The finance amount ratio between Trump and Clinton in each state bascially accords with state political affliations. Clinton has a huge advantage both on the total finance amount and duration.

##### Card 2
The second card shows a typical Democrates state - New York. Clinton has a absolute advantage over the total finance amount. Interestingly, real estate contributes the 3rd most amount to Trump probably because of his real estate business in NY.

##### Card 3
The third card shows a typical Republican state - Kentucky. Trump has a competitive total finance amount here. Coal miner contirbutes the 3rd most amount to him while does not shows up for Clinton, this probably because of the energy policy of the two candidates. Trump's policy favors coal miners while Clinton prefers new energy.

## Feedback

I showed my visualization to some friends of mine who are professional data analysts. Their feedback is the visualization is generally clear and easy to follow, the top donor occupation types in each state is quite interesting as it reflects the background and policy of the two candidates. They gave me the the following suggestions to improve my work which I have mentioned.

- Use bar chart instead of pie chart in plot 2
- Use moving average instead sum in plot 3
- Add informative legend in plot 3
- Remove unnessary axis label in plot 4

I also adjusted the font and color of the annonation in the final version to improve readablity and aesthetic.

## Resource
[2016 Presidential Campaign Finance](http://classic.fec.gov/disclosurep/PDownload.do)

[Presidential Election Results: Donald J. Trump Wins](https://www.nytimes.com/elections/results/president)

[Hillary Clinton: "We Are Going To Put A Lot Of Coal Miners & Coal Companies Out Of Business"](https://www.youtube.com/watch?v=ksIXqxpQNt0)













