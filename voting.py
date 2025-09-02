"""
Voting System

Task:
- Implement a simple voting system.
- Store candidates in a dictionary { "candidate_name": vote_count }
- Allow voters (by ID) to vote only once.
- Use *args to register multiple candidates at once.
- Use **kwargs to update candidate details like party, region.


// NOT FOR THIS ASSIGNMENT
Future OOP Extension:
- Candidate as a class.
- Voter as a class with has_voted flag.
- Election as a manager class.
"""

candidates = {}
voters = set()

def register_candidates(*args, **kwargs):
    """Register candidates with optional metadata.
    """
    pass

def cast_vote(voter_id, candidate):
    """Cast vote if voter has not voted before.
        after all the vote logic is completeted sucessfully,
        return: Vote casted for {candidate}.
    """
    pass

def election_result():
    """Return the winner(s)."""
    # max_votes = #add logic
    # winners = #add logic
    # return {"winners": winners, "candidates": candidates}

candidates = {}
voters = set()

def register_candidates(*args, **kwargs):
    """Register candidates with optional metadata."""
    for name in args:
        if name not in candidates:
            candidates[name] = {
                "votes": 0
            }
            # Add optional details (party, region, etc.)
            candidates[name].update(kwargs)
        else:
            print(f"Candidate {name} already registered.")


def cast_vote(voter_id, candidate):
    """Cast vote if voter has not voted before."""
    if voter_id in voters:
        return f"Voter {voter_id} has already voted."

    if candidate not in candidates:
        return f"Candidate {candidate} not found."

    candidates[candidate]["votes"] += 1
    voters.add(voter_id)
    return f"Vote casted for {candidate}."


def election_result():
    """Return the winner(s)."""
    if not candidates:
        return "No candidates registered."

    # Find max vote count
    max_votes = max(c["votes"] for c in candidates.values())
    winners = [name for name, c in candidates.items() if c["votes"] == max_votes]

    return {
        "winners": winners,
        "max_votes": max_votes,
        "all_results": {name: c["votes"] for name, c in candidates.items()}
    }


# ---------------- Example Run ----------------
register_candidates("Alice", "Bob", party="Independent")
register_candidates("Charlie", region="North")

print(cast_vote("V1", "Alice"))
print(cast_vote("V2", "Bob"))
print(cast_vote("V1", "Charlie"))  # should be blocked (already voted)
print(cast_vote("V3", "Alice"))

print("\nElection Results:", election_result())

