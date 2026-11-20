# Practical 13: Bayes' Theorem
# Formula: P(A|B) = P(B|A) * P(A) / P(B)
# Sample test inputs:
# Prior probability P(A): 0.2
# Likelihood P(B|A): 0.8
# Evidence P(B): 0.4
# (Result: Posterior probability = 0.4)

def bayes_theorem(prior_prob, likelihood, evidence):
    posterior_prob = (likelihood * prior_prob) / evidence
    return posterior_prob

if __name__ == "__main__":
    prior_prob = float(input("Enter prior probability P(A) (e.g. 0.2): "))
    likelihood = float(input("Enter likelihood P(B|A) (e.g. 0.8): "))
    evidence = float(input("Enter evidence P(B) (e.g. 0.4): "))

    posterior_prob = bayes_theorem(prior_prob, likelihood, evidence)

    print("Posterior Probability:", posterior_prob)
