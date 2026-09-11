"""Minimal pedagogical example of exact structural-fragility measurement.

This is NOT the research training code.  It demonstrates the evaluation idea:
freeze a routed model, remove expert sets, reroute among survivors, and measure
one-sided loss increase.
"""
from itertools import combinations
from math import exp, log


def bce_from_logit(logit: float, y: int) -> float:
    # Stable binary cross-entropy with logits.
    if logit >= 0:
        return (1 - y) * logit + log1p_exp(-logit)
    return -y * logit + log1p_exp(logit)


def log1p_exp(x: float) -> float:
    if x > 40:
        return x
    return log(1.0 + exp(x))


def routed_logit(router_scores, expert_logits, removed=()):
    survivors = [e for e in range(len(router_scores)) if e not in removed]
    if not survivors:
        raise ValueError("At least one expert must survive")
    chosen = max(survivors, key=lambda e: router_scores[e])
    return expert_logits[chosen]


def mean_one_sided_damage(dataset, removed):
    damages = []
    for item in dataset:
        clean = routed_logit(item["router"], item["expert_logits"], removed=())
        masked = routed_logit(item["router"], item["expert_logits"], removed=removed)
        clean_loss = bce_from_logit(clean, item["y"])
        masked_loss = bce_from_logit(masked, item["y"])
        damages.append(max(0.0, masked_loss - clean_loss))
    return sum(damages) / len(damages)


def exact_fragility(dataset, n_experts: int, k: int):
    records = []
    for size in range(1, k + 1):
        for removed in combinations(range(n_experts), size):
            records.append((removed, mean_one_sided_damage(dataset, removed)))
    worst_set, worst_damage = max(records, key=lambda t: t[1])
    return worst_damage, worst_set, records


if __name__ == "__main__":
    # Four-expert toy model. Expert 0 is preferred on an important subset, but
    # expert 1 is a partial substitute. Removing both 0 and 1 is more damaging.
    data = [
        {"router": [4.0, 3.0, 1.0, 0.0], "expert_logits": [4.0, 2.5, -1.0, -2.0], "y": 1},
        {"router": [4.2, 3.1, 0.5, 0.0], "expert_logits": [3.5, 2.0, -1.5, -2.5], "y": 1},
        {"router": [0.5, 0.4, 3.0, 2.0], "expert_logits": [-1.0, -0.8, -3.0, -2.0], "y": 0},
        {"router": [0.2, 0.3, 2.8, 2.1], "expert_logits": [-0.5, -0.7, -3.5, -2.2], "y": 0},
    ]

    f1, s1, _ = exact_fragility(data, n_experts=4, k=1)
    f2, s2, _ = exact_fragility(data, n_experts=4, k=2)
    print(f"Exact F1 = {f1:.6f}, worst singleton = {s1}")
    print(f"Exact F2 = {f2:.6f}, worst set       = {s2}")
