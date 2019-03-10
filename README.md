# Resolution Based Inference Engine
- Implement a resolution function resolving two sentences that are already in conjunctive normal form (CNF).
- Reuse it to implement a complete resolution inference engine accepting conjunctive normal form (CNF) sentences.<br><br>

The resolution inference engine provides three main functions
- TELL: add a sentence to the knowledge base.<br>
- ASK: query a proposition is true or false.<br>
- CLEAR: clean the knowedge base.<br>
For example,<br>
/>>> TELL([“or”, [“not”, “a”], “b”])<br>
/>>> TELL([“or”, [“not”, “b”], “c”])<br>
/>>> TELL(“a”)<br>
/>>> ASK(“c”)<br>
True<br>
/>>> ASK(“d”)<br>
False<br><br>

More information about conjunctive normal form (CNF)<br>
https://en.wikipedia.org/wiki/Conjunctive_normal_form<br>

More information about inference engine<br>
https://en.wikipedia.org/wiki/Inference_engine
