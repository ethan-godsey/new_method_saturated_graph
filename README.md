# Saturated Graph Testing
- This function tests a new way to find if a graph, bipartite or non bipartite, is saturated.
* This means that the maximum number of edges are highlighted in a graph under the following constraints:
  1. Each highlighted edge touches two nodes.
  2. No two highlighted edges touch the same node
- Background
  * I had this idea in class and created this method to test it.
  * It works on all cases, so a new method was found
  * However, this runs in O(n^3) in the worst case, which is worse than the current method that runs in o(n^2 log n)
