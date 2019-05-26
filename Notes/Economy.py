""" When asked, prices of goods and factor costs provided,
the producer class gives an output list in form of an array, 
that contains the amount of the good he is willing to provide first, 
and returns 0 in the places of the goods he is not producing,
but still are part of the economy and the consumer decision. 
Then the amount of factors he demands at that factor price so that he will be able to produce,
at the end, a single profit amount he would make be the transaction succesful.
The consumer class similary, gives an output list (array), that for a given good prices and factor prices, 
and the response of the producer about profit,
first containing the amount of every good he would consume,
and then the amount of every factor he is willing to provide,
in order increase his or her budget constraint.
So if there are 3 goods produced in the economy, and 8 factors in total, 
and goods prices and factor prices are provided,
and the producer produces the third good, his class could return
[0,0,34,3,4,5,6,7,8,7,0,100] in this format. 
The consumer, now taking profit (100) into account and good and factor prices,
returns [4,5,6,6,7,1,2,3,4,5,6,7]. The consumer's list lenght is therefore always one item shorter than the producer's.


The object of the Economy class is to find goods and factor prices that will make the sum of the consumer demanded goods
and supplied factor amounts,
be the same as the sum of the producers demanded amounts of factors and supplied goods.
The way chosen to do this is to substract the difference, and minimize this up to 0."""
