# Pre-publication GitHub release checklist

Before making this repository public:

- Create the repository as `structural-fragility-moe-reproducibility`.
- Use the description in `REPOSITORY_METADATA.md`.
- Upload only the files in this package.
- Confirm there is **no manuscript TeX** and **no full research training/evaluation code**.
- Run `python examples/minimal_structural_fragility_demo.py` once after cloning.
- Keep raw UCI/scikit-learn datasets out of the repository; point users to the public sources in `docs/data_sources.md`.
- After publication, update `CITATION.cff` with DOI/journal metadata and add the full versioned implementation/reproduction artifacts.
