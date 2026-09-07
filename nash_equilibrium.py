def is_nash_equilibrium(
    observed_shares: Dict[str, float],
    rule,
    perturbation_pct: float = 0.02
    ) -> Tuple[bool, Dict]:
    """
    Test whether the observed vote-share profile is consistent
    with Nash equilibrium by checking that no party benefits from
    a small reallocation of their support.
    observed_shares : {party: national_vote_share}
    rule            : function that determines winner from shares
    perturbation_pct: fraction of votes to reallocate in each test
    Returns (is_ne, deviations) where deviations records profitable ones.
    """
    parties = list(observed_shares.keys())
    current_winner = rule(observed_shares)
    deviations = {}
    for party in parties:
        for target in parties:
            if party == target:
                continue
            # Try shifting perturbation_pct of votes from target to party
            trial = observed_shares.copy()
            shift = perturbation_pct * observed_shares.get(target, 0)
            trial[target] = max(0, trial[target] - shift)
            trial[party] = trial[party] + shift  # Normalise
            total = sum(trial.values())
            trial = {p: v/total for p, v in trial.items()}
            new_winner = rule(trial)
            if new_winner != current_winner:
                deviations[(party, target)] = {
                    'shift_pct': perturbation_pct,
                    'old_winner': current_winner,
                    'new_winner': new_winner,
                }
    return len(deviations) == 0, deviations