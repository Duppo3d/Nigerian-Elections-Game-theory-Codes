# Game Theory in Nigerian Presidential Elections

Code accompanying the manuscript *"Game Theory in Mathematics for Programmers:
A Computational Approach Using Game Theory to Analyse Strategic Voting in
Nigerian Presidential Elections"* (submitted to Humanities and Social Sciences
Communications).

## Contents

- `voting_rule.py` — implementation of Nigeria's modified plurality rule
  (national plurality + 25%-in-24-states geographic threshold), used to
  determine election winners from a vote dictionary.
- `nash_equilibrium.py` — checks whether an observed vote-share profile is
  consistent with Nash equilibrium by testing profitable unilateral
  deviations.
- `manipulation_simulation.py` — Impartial Culture profile generator and
  manipulation-rate simulator used to estimate how often the voting rule is
  manipulable.
- `data/` — state-level INEC vote totals for the 2015, 2019, and 2023
  presidential elections, compiled from public sources. **See
  `data/README.md` for an important accuracy caveat on the 2023 file
  before treating it as final.**

## ⚠️ About the data

The manuscript's own text only reproduced a few illustrative vote counts
(Lagos, Kano, Ogun) as a worked example — the full 36-state + FCT vote
totals used in the actual analysis were not present in the submitted
document. The CSVs in `data/` were compiled afterwards from public INEC
results (via Wikipedia and Vanguard News) to satisfy the journal's data
availability requirement. The 2015 and 2019 files sum exactly to the
official national totals; the 2023 file has small (~0.1–0.2%) discrepancies
from transcription artifacts in the secondary source and should be
verified against INEC's official IReV portal before being cited as final
— see `data/README.md`.

## Requirements

```
pip install -r requirements.txt
```

## Usage

```python
from voting_rule import nigerian_plurality_winner, vote_share_summary
from nash_equilibrium import is_nash_equilibrium
from manipulation_simulation import generate_ic_profile, simulate_manipulation_rate

winner = nigerian_plurality_winner(votes)
```

## Citation

If you use this code, please cite the manuscript (details to be updated on
publication).
