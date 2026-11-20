
def bayes_theorem(prior_prob, likelihood, evidence):
    posterior_prob = (likelihood * prior_prob) / evidence
    return posterior_prob

if __name__ == "__main__":
    prior_prob = float(input("Enter prior probability: "))
    likelihood = float(input("Enter likelihood: "))
    evidence = float(input("Enter evidence: "))

    posterior_prob = bayes_theorem(prior_prob, likelihood, evidence)

    print("Posterior Probability:", posterior_prob)