# integrated-F1

This repository is used to easily calculate the penalized and non-penalized integrated F1 score.
In order use, clone this repository and import the desired function:

```
from integratedF1 import penalized
```

In this case, we are importing the function for calculating the penalized integration score.
In order to call the function, the following arguments must be provided:
- List of confidence values
- List of F1 scores
- f value


The format should be as follows:

```
confidence_values = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
F1_scores = [0.0, 0.324, 0.683, 0.712, 0.751, 0.777, 0.703, 0.684, 0.419, 0.0, 0.0]
f = 1

```

The function can be called using these above assigned variables using:

```
[penalized_integration_scores, overall_score, pen_nonpen_ratio] = penalized(confidence_values, F1_scores, f)
```

This will return a list of penalized integration scores for each index, the overall penalized score, and the penalized to non-penalized score ratio.

