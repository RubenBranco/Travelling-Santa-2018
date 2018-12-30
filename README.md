# Travelling-Santa-2018

Kaggle Travelling Santa 2018 Competition

Unfortunately, due to work and university, I was only able to try genetic algorithm and didn't have time to try other approaches.

## Description

Rudolph the red-nosed reindeer
Had some very tired hooves
But he had a job to finish
Could he do it with the shortest moves?

All of the other reindeer
Used to laugh and mock his code
They always said poor Rudolph
Couldn't handle the workload

Then one foggy Christmas Eve
Santa came to say
I see you've taken number theory
Please make this night a bit less dreary?

Then how the reindeer loved him
and each enrolled in an AI degree
Rudolph the red-nosed reindeer
We get to go to bed early!

Rudolph has always believed in working smarter, not harder. And what better way to earn the respect of Comet and Blitzen than showing the initiative to improve Santa's annual route for delivering toys on Christmas Eve?

This year, Rudolph believes he can motivate the overworked Reindeer team by wisely choosing the order in which they visit the houses on Santa's list. The houses in prime cities always leave carrots for the Reindeers alongside the usual cookies and milk. These carrots are just the sustenance the Reindeers need to keep pace. In fact, Rudolph has found that if the Reindeer team doesn't visit a prime city exactly every 10th step, it takes the 10% longer than it normally would to make their next destination!

Can you help Rudolph solve the Traveling Santa problem subject to his carrot constraint? His team--and Santa--are counting on you!

## Evaluation

Your submission is scored on the Euclidean distance of your submitted path, subject to the constraint that every 10th step is 10% more lengthy unless coming from a prime CityId.

### Submission File

Your submission file contains the ordered Path that Santa should use to visit all the cities. Paths must start and end at the North Pole (CityId = 0) and you must visit every city exactly once. Submission files must have a header and should look like:

```
Path
0
1
2
...
0
```
