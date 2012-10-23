**Markov Text Generator**

**What**
A Markov Chain is a sequence of values where the next value 
depends only on the current value (and not past values). It's 
basically a really simple state machine, where given the present 
state, the future state is conditionally independent of the past.

Thus we can ask the question: Given the present word, how likely 
is it that this word I've chosen would be the next?

**How**
1) The last two words are the current state.
2) Next word depends on last two words only, or on present state only.

I've simplified this example down to the core elements of a Markov text generator.

Run the following to generate your own nonsensical strings:
    $ python run.py
