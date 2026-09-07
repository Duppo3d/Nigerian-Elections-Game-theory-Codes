# Vote data — Nigerian presidential elections, 2015 / 2019 / 2023

Source: official INEC declared results, compiled from public secondary
transcriptions:

- `votes_2015.csv` — APC (Buhari) and PDP (Jonathan) vote counts per state.
  Compiled from the results table on the "2015 Nigerian general election"
  Wikipedia article (sourced there to INEC). State-level totals sum exactly
  to the official national totals (APC 15,424,921 / PDP 12,853,162).

- `votes_2019.csv` — APC (Buhari) and PDP (Atiku) vote counts per state.
  Compiled from the results table on the "2019 Nigerian general election"
  Wikipedia article (sourced there to BBC / This Day / Vanguard, collated
  from INEC declarations). State-level totals sum exactly to the official
  national totals (APC 15,191,847 / PDP 11,262,978).

- `votes_2023.csv` — APC, PDP, LP, and NNPP vote counts per state. Compiled
  from Vanguard News's tabulation of INEC's declared 2023 state-by-state
  results.

  ⚠️ **Known data-quality caveat:** the Vanguard table contains visible
  transcription artifacts (stray spaces in numbers, at least one likely
  digit-order typo in the Benue LP figure). Summing this table gives party
  totals within ~0.1–0.2% of the official national aggregates (APC:
  8,805,655 vs. official 8,794,726; LP: 6,098,588 vs. official 6,101,533;
  NNPP: 1,497,688 vs. official 1,496,671; PDP matches exactly at
  6,984,520). This is very likely due to a small number of individual
  state-level transcription errors rather than a systematic issue, but
  **the exact per-state 2023 figures should be verified against INEC's
  IReV portal or another certified result sheet before being treated as
  final** — the 2015 and 2019 files above do not have this issue, as
  their state-level sums match the official totals exactly.

None of these files were part of the manuscript as submitted; they were
compiled afterwards from public sources to satisfy the journal's data
availability requirement, and should be checked against your own working
data/results before being cited as authoritative.
