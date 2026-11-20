# Practical 12: Joint and Conditional Probability
# Problem probabilities:
# P(Passing Statistics) = 0.15
# P(Passing Coding | Passes Statistics) = 0.60
# P(Passing Coding | Fails Statistics) = 0.40

def conditional():
    pass_stats = 0.15
    pass_codingWStats = 0.60
    pass_codingWOStats = 0.40

    # Probability of passing both Statistics and Coding
    prob_both = pass_stats * pass_codingWStats
    print("The probability that applicant passes both is", round(prob_both, 3))

    # Probability of passing Coding
    prob_coding = prob_both + ((1 - pass_stats) * pass_codingWOStats)
    print("The probability that he/she passes Coding is", round(prob_coding, 3))

    # Conditional probability: P(Statistics | Coding)
    stats_given_coding = prob_both / prob_coding
    print("Conditional probability is", round(stats_given_coding, 3))

if __name__ == "__main__":
    conditional()
