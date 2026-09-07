import numpy as np
from typing import Dict, Optional, List, Tuple

# Nigerian state names (36 states + FCT)
STATES = [
    'Abia','Adamawa','Akwa Ibom','Anambra','Bauchi','Bayelsa','Benue',
    'Borno','Cross River','Delta','Ebonyi','Edo','Ekiti','Enugu','FCT',
    'Gombe','Imo','Jigawa','Kaduna','Kano','Katsina','Kebbi','Kogi',
    'Kwara','Lagos','Nasarawa','Niger','Ogun','Ondo','Osun','Oyo',
    'Plateau','Rivers','Sokoto','Taraba','Yobe','Zamfara'
]
N_STATES = 37            # 36 states + FCT
THRESHOLD_STATES = 24    # must win >= 25% in at least 24 states
THRESHOLD_PCT = 0.25     # 25 percent geographic threshold

def nigerian_plurality_winner(
    votes: Dict[str, Dict[str, int]]
    ) -> Optional[str]:
    """
    Determine the winner of a Nigerian presidential election.
    votes: {party_name: {state_name: vote_count}}
    Returns the winning party or None if threshold not met (second round).
    """
    parties = list(votes.keys())
    states = STATES
    # Total national votes per party
    national = {p: sum(votes[p].values()) for p in parties}
    total_votes = sum(national.values())
    # Winner = party with most national votes
    plurality_winner = max(national, key=national.get)
    # Check geographic threshold for plurality winner
    states_above_threshold = 0
    for state in states:
        state_total = sum(votes[p].get(state, 0) for p in parties)
        if state_total == 0:
            continue
        pct = votes[plurality_winner].get(state, 0) / state_total
        if pct >= THRESHOLD_PCT:
            states_above_threshold += 1
    if states_above_threshold >= THRESHOLD_STATES:
        return plurality_winner   # Constitutional winner
    else:
        return None                # Second round required

def vote_share_summary(
    votes: Dict[str, Dict[str, int]]
    ) -> Dict[str, float]:
    """Return national vote share percentage for each party."""
    national = {p: sum(v.values()) for p, v in votes.items()}
    total = sum(national.values())
    return {p: round(100 * national[p] / total, 2) for p in national}