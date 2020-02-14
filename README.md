# SSVC Tests
This is a fork of SSVC repository. The changes are as follows:

- Some minor issues are fixed in original `src/ssvc.py` file.
- `src/ssvc_tests.py` is added, which contains test functions to generate test output files in data folder.
- Following files in `data/*` which are output of running the tests are added so they can be consumed without having to run the tests.
 - `ssvc_1_divergence.txt`
 - `ssvc_1_inner_merge.csv`
 - `ssvc_1_inner_merge_numbers.csv`
 - `ssvc_1_outer_merge.csv`
 - `ssvc_1_outer_merge_numbers.csv`
- This README.md is modified to reflect the changes.

These tests are added in the context of the article: [A Critical First Look at Stakeholder Specific Vulnerability Categorization (SSVC)](https://secursive.github.io/posts/1-Critical-Look-Stakeholder-Specific-Vulnerability-Categorization-SSVC.html).

---

# SSVC
Stakeholder-Specific Vulnerability Categorization

# What's here

`doc/*.pdf`

Both reports referenced below can be found in this directory.

`data/*.csv`

Also included in  are the two lookup tables as csv files which `ssvc.py`
reads in. These are just one row per possible path through the trees as
described in the paper. Changing the "outcome" column in this table will
change what the module above recommends.


`src/ssvc.py`

`ssvc.py` has two methods: `applier_tree()` and `developer_tree()`

The two methods just loop through their respective lookup tables until
they hit a match, then return the outcome. Maybe not the best implementation, but it worked
well enough for what was needed at the time.

`src/ssvc_tests.py`

This performs various tests on SSVC model and store the results in various files in `data/` folder.

## References

1. Spring, J., Hatleback, E., Householder, A., Manion, A., and Shick, D. "Prioritizing Vulnerability Response: A Stakeholder-Specific Vulnerability Categorization." White Paper, Software Engineering Institute, Carnegie Mellon University (2019). https://resources.sei.cmu.edu/library/asset-view.cfm?assetid=636379
2. Spring, J., Hatleback, E., Householder, A., Manion, A., and Shick, D. "Towards Improving CVSS." White Paper, Software Engineering Institute, Carnegie Mellon University (2018). https://resources.sei.cmu.edu/library/asset-view.cfm?assetid=538368
3. Akbar, M. "A Critical First Look at Stakeholder Specific Vulnerability Categorization (SSVC)." Article, Secursive Blog, Secursive (2020). https://secursive.github.io/posts/1-Critical-Look-Stakeholder-Specific-Vulnerability-Categorization-SSVC.html
