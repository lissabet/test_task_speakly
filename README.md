**Run task**

`python -m task`

**Run tests**

`python -m unittest discover`



**Question 2**

I think the main problem will be with the speed of loading data. 
Because without limitation and page size in this function can be passed a large 
volume of data(for example 1 million of events), so i think we should add here 
something like a batch size.

The second problem is that the function working only with the 30 days. 
We can create more general solution, and pass the 30 days as parameter.
It will be easy to reuse this function and support.

Example:

`def get_leaderboard_user_ids(engagement_events: List[Event], days: int = 30) -> List[int]:
`


**Question 3**

I found and fixed one anti pattern that i found - _unnamed(magic) numeric or 
strings_ using in the code. For example - `word_learned` is a constant and i convert 
it into enum, because when we talking about large project, without magic numeric 
or strings it is easy to scale and refactor existing code.
