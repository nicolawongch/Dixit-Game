# Dixit Scorekeeper for Remote/Group Play
# Author: Copilot for nicolawonggg

def get_int_input(prompt, valid_fn=None, error_msg="Invalid input. Try again."):
    """Prompt for integer input, with optional validation."""
    while True:
        try:
            value = int(input(prompt))
            if valid_fn is not None and not valid_fn(value):
                print(error_msg)
                continue
            return value
        except ValueError:
            print("Please enter a valid integer.")

def main():
    print("Welcome to Dixit Scorekeeper!")
    # Number of teams
    num_teams = get_int_input("Number of teams (3-5): ",
                              lambda x: 3 <= x <= 5,
                              "Number of teams must be between 3 and 5.")
    # Team setup
    teams = []
    for i in range(num_teams):
        while True:
            name = input(f"Team {i+1} name: ").strip()
            if name:
                teams.append({"name": name, "score": 0})
                break
            else:
                print("Team name cannot be empty.")
    # Main loop
    round_num = 1
    while True:
        print(f"\n--- Round {round_num} ---")
        for idx, t in enumerate(teams):
            print(f"{idx}: {t['name']} (Score: {t['score']})")
        # Storyteller selection
        storyteller = get_int_input("Storyteller team index: ",
                                   lambda x: 0 <= x < num_teams,
                                   "Select a valid team index.")

        # Card assignment: map card number => team index
        card_map = {}
        assigned_cards = set()
        print("\nAssign a unique card number to each team's card (e.g. 1,2,3...)")
        for idx, t in enumerate(teams):
            while True:
                card = get_int_input(f"Card number for {t['name']}: ")
                if card in assigned_cards:
                    print("Card number already used. Choose a different number.")
                    continue
                card_map[card] = idx
                assigned_cards.add(card)
                break

        # Voting: which card each team voted for
        votes = {}
        valid_card_numbers = set(card_map.keys())
        team_card_dict = {v: k for k, v in card_map.items()} # team index -> their card number
        for idx, t in enumerate(teams):
            if idx == storyteller:
                continue  # storyteller doesn't vote
            while True:
                vote = get_int_input(f"{t['name']} votes for card number: ")
                # Team can't vote for their own card
                if vote == team_card_dict[idx]:
                    print("You can't vote for your own card. Try again.")
                    continue
                # Must vote for a played card
                if vote not in valid_card_numbers:
                    print(f"Invalid card number. Please enter one of the played card numbers: {sorted(valid_card_numbers)}")
                    continue
                votes[idx] = vote
                break

        # Calculate which cards got votes:
        card_votes = {c: [] for c in card_map}
        for voter, card_voted in votes.items():
            card_votes[card_voted].append(voter)

        # Points calculation
        correct_guessers = [team for team, voted_card in votes.items() if card_map[voted_card] == storyteller]
        num_correct = len(correct_guessers)
        all_possible = len(teams) - 1
        if num_correct == 0 or num_correct == all_possible:
            # All or none guessed
            print("All or none guessed: Storyteller gets 0, other teams get 2 points each.")
            for i, t in enumerate(teams):
                if i != storyteller:
                    t["score"] += 2
        else:
            teams[storyteller]["score"] += 3
            for i in correct_guessers:
                teams[i]["score"] += 3

        # Bonus for non-storytellers whose cards received votes
        for card, voters in card_votes.items():
            owner = card_map[card]
            if owner != storyteller:
                teams[owner]["score"] += len(voters)

        # Show votes (optional)
        print("\nVote Breakdown:")
        for team_idx, vote in votes.items():
            print(f"{teams[team_idx]['name']} voted for card {vote} ({teams[card_map[vote]]['name']}'s card)")
        print("\nCards with votes:")
        for card, voters in card_votes.items():
            vnames = ', '.join([teams[v]["name"] for v in voters])
            owner = teams[card_map[card]]["name"]
            print(f"Card {card} ({owner}): {len(voters)} vote(s) [{vnames}]")

        # Show scores
        print("\nSCORES after this round:")
        for t in teams:
            print(f"{t['name']}: {t['score']}")
        round_num += 1
        cont = input("\nContinue to next round? (y/n): ").strip().lower()
        if cont not in ["y", "yes"]:
            print("Game ended. Final scores:")
            for t in teams:
                print(f"{t['name']}: {t['score']}")
            break

if __name__ == "__main__":
    main()
