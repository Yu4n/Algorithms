""" The dynamic-programming method works as follows. Having observed that a
    naive recursive solution is inefficient because it solves the same subproblems re-
    peatedly, we arrange for each subproblem to be solved only once, saving its solu-
    tion. If we need to refer to this subproblem’s solution again later, we can just look it
    up, rather than recompute it. Dynamic programming thus uses additional memory
    to save computation time; it serves an example of a time-memory trade-off. The
    savings may be dramatic: an exponential-time solution may be transformed into a
    polynomial-time solution. A dynamic-programming approach runs in polynomial
    time when the number of distinct subproblems involved is polynomial in the input
    size and we can solve each such subproblem in polynomial time.

    There are usually two equivalent ways to implement a dynamic-programming
    approach. We shall illustrate both of them with our rod-cutting example.

    The first approach is top-down with memoization.2 In this approach, we write
    the procedure recursively in a natural manner, but modified to save the result of
    each subproblem (usually in an array or hash table). The procedure now first checks
    to see whether it has previously solved this subproblem. If so, it returns the saved
    value, saving further computation at this level; if not, the procedure computes the
    value in the usual manner. We say that the recursive procedure has been memoized;
    it “remembers” what results it has computed previously.

    The second approach is the bottom-up method. This approach typically depends
    on some natural notion of the “size” of a subproblem, such that solving any par-
    ticular subproblem depends only on solving “smaller” subproblems. We sort the
    subproblems by size and solve them in size order, smallest first. When solving a
    particular subproblem, we have already solved all of the smaller subproblems its
    solution depends upon, and we have saved their solutions. We solve each sub-
    problem only once, and when we first see it, we have already solved all of its
    prerequisite subproblems.

    These two approaches yield algorithms with the same asymptotic running time,
    except in unusual circumstances where the top-down approach does not actually
    recurse to examine all possible subproblems. The bottom-up approach often has
    much better constant factors, since it has less overhead for procedure calls."""
import math


def cut_rod_recursive(p, n):
    if n == 0:
        return 0
    q = - math.inf
    for i in range(1, n + 1):
        q = max(q, p[i] + cut_rod_recursive(p, n - i))
    return q


def memoized_cut_rod(p, n):
    r = [-1 for _ in range(n + 1)]

    return memoized_cut_rod_aux(p, n, r)


""" Here, the main procedure MEMOIZED-CUT-ROD initializes a new auxiliary ar-
    ray r[0..n] with the value -inf., a convenient choice with which to denote “un-
    known.” (Known revenue values are always nonnegative.) It then calls its helper
    routine, MEMOIZED-CUT-ROD-AUX.
    
    The procedure MEMOIZED-CUT-ROD-AUX is just the memoized version of our
    previous procedure, CUT-ROD. It first checks in line 1 to see whether the desired
    value is already known and, if it is, then line 2 returns it. Otherwise, lines 3–7
    compute the desired value q in the usual manner, line 8 saves it in r[n], and line 9
    returns it."""


def memoized_cut_rod_aux(p, n, r):
    if r[n] >= 0:
        return r[n]  # Return the optimal solution for n.
    q = p[0]
    if n == 0:
        q = 0
    else:
        for i in range(1, n + 1):
            q = max(q, p[i] + memoized_cut_rod_aux(p, n - i, r))

    r[n] = q
    return q


def bottom_up_cut_rod(p, n):
    r = [0 for _ in range(n + 1)]

    for j in range(1, n + 1):
        q = p[0]
        for i in range(1, j + 1):
            q = max(q, p[i] + r[j - i])
        r[j] = q

    return r[n]


prc = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]  # Price
for i in range(0, 11):
    print(bottom_up_cut_rod(prc, i))
