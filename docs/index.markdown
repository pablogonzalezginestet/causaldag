---
layout: default
---

CausalDAG is a Python package for the creation, manipulation, and learning
of Causal DAGs. CausalDAG requires Python 3.5+.

## Install
Install the latest version of CausalDAG:
```
$ pip3 install causaldag
```

## Documentation
Documentation is available at [https://causaldag.readthedocs.io/en/latest/index.html](https://causaldag.readthedocs.io/en/latest/index.html)

## Simple Example
Find the CPDAG (complete partially directed acyclic graph,
AKA the *essential graph*) corresponding to a DAG:
```
>>> import causaldag as cd
>>> dag = cd.DAG(arcs={(1, 2), (2, 3), (1, 3)})
>>> cpdag = dag.cpdag()
>>> iv = dag.optimal_intervention(cpdag=cpdag)
>>> icpdag = dag.interventional_cpdag([iv], cpdag=cpdag)
>>> dag.reversible_arcs()
{(1,2), (2,3)}
```

## Sample structure learning algorithms
### [Difference Causal Inference (DCI)](./dci.html)
DCI is a structure learning algorithm that directly learns the difference between two causal graphs given two datasets. It has been applied to learning differences between gene regulatory networks given gene expression data corresponding to two condtions.

![](images/dci.png)

### [Unknown Target Interventional Greedy Sparsest Permutations (UT-IGSP)](./utigsp.html)
UT-IGSP is a structure learning algorithm that uses interventional data, with unknown or only partially known targets,
to discover a causal graph. It has been applied to learning protein signalling networks from protein mass spectroscopy data.

## License

Released under the 3-Clause BSD license (see LICENSE.txt):
```
Copyright (C) 2018
Chandler Squires <csquires@mit.edu>
```

