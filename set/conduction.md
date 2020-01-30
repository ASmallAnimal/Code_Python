# SET

        A={"python",123,("python",123)}
        B=set("pypy123")
    >>>('p','y','1','2','3)

1. NO reapeating
2. NO order
3. {} & divided with ','

## Operation

* S|T--> all factors
* S-T--> except T from S
* S&T--> common factors
* S^T--> not common factors
* S<=T or S< T--> result is "True" &"False"

    method | describe
    --------|----------
    S.add(x) | add x in S
    S.discard(x) | delete x (no error when not existing x)
    S.remove(x) | be error
    S.clear() | remove all factors
    S.pop() | return x in S, if S is empty, it will get KeyError
    S.copy | return a S' copy
    len(S) | number of factors
    x in S | judge
    x not in S | judge
    set(x) | make s a set
