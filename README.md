# Structural Fragility in Sparse Mixture-of-Experts

This is the **pre-publication public companion repository** for the research project on structural fragility in sparse Mixture-of-Experts (MoEs).

## The problem

Sparse MoEs are usually monitored with quantities such as expert utilization and load balance. These statistics describe **where traffic goes**, but they do not answer a different question: **would a learned capability survive if one expert or a small expert set became unavailable?**

The project calls the worst one-sided performance damage under frozen counterfactual expert removal **structural fragility**.

## What is public during peer review

This repository intentionally contains only material that can be shared before publication:

- the metric specification and evaluation protocol;
- verified aggregate results used in the current submission;
- public-data provenance notes;
- a minimal standalone example of exact singleton/pair fragility measurement;
- a citation stub and repository metadata.

The **full research implementation and manuscript TeX are intentionally not public before publication**. The complete executable code is supplied confidentially to journal reviewers as *Supplementary Code for Review*. After publication, the full versioned implementation and manuscript-associated reproduction artifacts are intended to be released here.

## Main verified result

The confirmatory scikit-learn Digits experiment uses a fixed 60/20/20 split (split seed 2026), development training seeds 0-1, and confirmation training seeds 10-19. With eight experts and top-1 routing, all singleton and unordered-pair removals are evaluated exactly.

FCR reduces mean singleton fragility from **0.1359** (baseline) to **0.0350**, while clean accuracy changes from **0.9425** to **0.9461**. Against load-proportional stress, FCR has lower singleton fragility on all **10/10 paired confirmation seeds** (exact two-sided Wilcoxon `p = 0.001953`).

A UCI Gas Sensor Drift transfer study is also reported. It shows that the current singleton-targeted control rule does **not** automatically control pair-level fragility in that heavier-tailed setting. This boundary motivates a future k-aware intervention objective rather than post-hoc retuning of the present runs.

## Repository layout

- `examples/minimal_structural_fragility_demo.py` - toy exact removal evaluation.
- `docs/metric_specification.md` - definition and evaluation semantics.
- `docs/data_sources.md` - public datasets used in the study.
- `docs/reproducibility_scope.md` - what is and is not released during peer review.
- `results/verified_aggregate_results.csv` - aggregate values from the verified runs.
- `REPOSITORY_METADATA.md` - proposed name, description, topics, and release policy.

## Minimal example

```bash
python examples/minimal_structural_fragility_demo.py
```

The example is pedagogical and is **not** the research training code.

## Data

No new dataset was introduced. The experiments use:

- scikit-learn Digits;
- UCI Gas Sensor Drift at Different Concentrations.

Raw datasets are not mirrored here.

## Citation

A `CITATION.cff` stub is provided. Update the DOI/journal fields after publication.

## License

No general software license is asserted for the unpublished research implementation because that implementation is not included here. Select an appropriate license for the public full-code release after publication.
