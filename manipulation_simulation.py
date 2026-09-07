import random
from itertools import permutations

def generate_ic_profile(
    n_voters: int,
    candidates: List[str]
    ) -> List[Tuple[str, ...]]:
    """
    Generate a voter preference profile under the Impartial Culture model.
    Each voter's ranking is drawn uniformly at random from all permutations.
    """
    all_perms = list(permutations(candidates))
    return [random.choice(all_perms) for _ in range(n_voters)]

def simulate_manipulation_rate(
    candidates: List[str],
    n_voters: int,
    n_profiles: int,
    rule
    ) -> float:
    """
    Estimate the manipulation rate under a given voting rule
    across n_profiles randomly generated IC preference profiles.
    """
    manipulable_count = 0
    for _ in range(n_profiles):
        profile = generate_ic_profile(n_voters, candidates)
        sincere_ballots = [v for v in profile]
        true_winner = rule(sincere_ballots)
        for i in range(n_voters):
            true_payoff = profile[i].index(true_winner)
            for alt_ballot in permutations(candidates):
                if alt_ballot == profile[i]:
                    continue
                trial = sincere_ballots.copy()
                trial[i] = alt_ballot
                new_winner = rule(trial)
                # Lower rank index = more preferred
                if profile[i].index(new_winner) < true_payoff:
                    manipulable_count += 1
                    break
            else:
                continue
            break
    return manipulable_count / n_profiles