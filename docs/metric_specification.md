# Structural fragility: metric specification

For a trained routed model `f`, freeze all parameters. For an unavailable expert set `S`, mask those experts before route normalization and reroute only among surviving experts.

For each held-out example `(x_i, y_i)`, define one-sided damage

`Z_S(i) = max(0, loss(f_without_S(x_i), y_i) - loss(f(x_i), y_i))`.

For an allowed family of nonempty removal sets with size at most `k`, structural fragility is

`F_k = max_S mean_i Z_S(i)`.

A capability-conditional form computes the mean inside each semantically fixed capability group first, then maximizes over both groups and allowed expert sets.

## Exact enumeration in the proof-of-concept

The primary experiments use 8 experts and evaluate:

- 8 singleton sets;
- 28 unordered pairs;
- 36 nonempty sets in total for `k <= 2`.

No sampled ablation approximation is used for the reported `F_1` and `F_2` values.

## Important distinction

Expert utilization is not structural fragility. Utilization measures traffic; fragility measures functional dependence under removal.
