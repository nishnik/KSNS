# KSNS
Kourse Structre is Not Structured

You can view the project at [ksns.herokuapp](https://ksns.herokuapp.com/).

This repository is about Machine Learning and **Kumar Srinivas**.<br/>
Everyone in our wing knows that there is no one more regular in going to classes than our Kumar Srinivas.<br/>
I watched him every day, crossing my doors with a red bag, *whatta scenery in motion*!<br/>
I always wondered at times like these, **is it this hard to become a Civil Engineer?**<br/>

So:<br/>
- If you don't want to take the classes under a particular department but would like to learn the concepts.
- If you don't want to carry red bags on your shoulders but would like to get smarter two day before exams.

This is for you:<br/>
- Why not look for a similar course in a different department.<br/>
- Why not just say **Kumar Srinivas's Not from South**.

## What is the algorithm behind it?

KSNS compares syllabus of two subjects. The recommendation scores reflect the overlap of the syllabi between two subjects.<br/>
It uses a simple mathematical tool called [Singular Value Decomposition](https://en.wikipedia.org/wiki/Singular-value_decomposition).

## Examples

```
>>> print_top_k('IM21003', sliced, 5, different_dep = True)
Most similar courses to  IM21003   OPERATIONS RESEARCH-I
[[0.5085419334812452, 'MI40036'],
 [0.5085419334812452, 'MI31007 - QUANTITATIVE DECISION MAKING'],
 [0.48840891191756297, 'MA30014 - OPERATION RESEARCH'],
 [0.4018718822832945, 'MA41010 - NON LINEAR PROGRAMMING'],
 [0.3841769601752256, 'MA51122']]
```

```
Most similar courses to  MA21007   DESIGN AND ANALYSIS OF ALGORITHMS
[[0.7550651497969045, 'CS21003 - ALGORITHMS - I'],
 [0.6481640930260969, 'CS60007'],
 [0.6351085358433876, 'CS40008'],
 [0.6330704251733447, 'IT60101'],
 [0.6119399635618148, 'CS60047']]
```

```
>>> print_top_k('MA21007', sliced, 5) # Can be same dep
Most similar courses to  MA21007   DESIGN AND ANALYSIS OF ALGORITHMS
[[0.9871067434313293, 'MA60002'],
 [0.895290263976874, 'MA69004'],
 [0.8497129570752778, 'MA29005 - DESIGN AND ANALYSIS OF ALGORITHMS LAB.'],
 [0.77405422041257, 'MA61014'],
 [0.7550651497969045, 'CS21003 - ALGORITHMS - I']]
```
## Contributions

There are few courses whose name is missing in the file. You can use MetaKGP's dump to rectify that. Thanks!
