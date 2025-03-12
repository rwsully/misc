# Welcome to the Career Probability Calculator!
# This tool helps you estimate the probability of achieving a specific career goal
# (e.g., becoming a web developer) based on various factors like time investment,
# skills, motivation, and more. You'll be asked to rate yourself on a scale of 0 to 5
# for each factor, and the calculator will provide your probability of success.
# Let's get started!

import math

# Define default weights for each factor (positive and negative)
default_weights = {
    "time_investment": 0.1,  # per hour
    "prior_experience": 0.3,
    "access_to_resources": 0.2,
    "mentorship_support": 0.15,
    "motivation": 0.25,
    "technical_skills": 0.2,
    "portfolio_quality": 0.25,
    "job_market_demand": 0.3,
    "networking": 0.15,
    "resilience": 0.2,
    "financial_stability": 0.1,
    "economic_conditions": 0.2,
    "industry_trends": 0.3,
    "consistency": 0.25,
    "access_to_education": 0.2,
    "social_safety_nets": 0.15,
    "burnout_risk": -0.2,
    "imposter_syndrome": -0.15,
    "competition": -0.25,
    "learning_curve": -0.3,
    "financial_constraints": -0.2,
    "location": 0.25,
    "health": 0.2,
    "time_management": 0.15,
    "discrimination": -0.3,
}

# Baseline intercept
baseline_intercept = -2.0

def calculate_log_odds(scores, weights):
    """
    Calculate the log-odds based on user scores and weights.
    """
    log_odds = baseline_intercept
    for factor, score in scores.items():
        log_odds += weights[factor] * score
    return log_odds

def calculate_probability(log_odds):
    """
    Convert log-odds to probability using the logistic function.
    """
    return 1 / (1 + math.exp(-log_odds))

def adjust_weights(default_weights):
    """
    Allow users to adjust the weights of each factor.
    """
    print("\nWould you like to adjust the weights of any factors? (yes/no)")
    adjust = input().strip().lower()
    if adjust == "yes":
        weights = default_weights.copy()
        for factor in weights:
            print(f"Current weight for '{factor}': {weights[factor]}")
            new_weight = float(input(f"Enter new weight for '{factor}' (or press Enter to keep current): ") or weights[factor])
            weights[factor] = new_weight
        return weights
    else:
        return default_weights

def main():
    """
    Main function to collect user inputs and calculate the probability.
    """
    print("Welcome to the Career Probability Calculator!")
    print("Please rate yourself on a scale of 0 to 5 for the following factors:")

    # Allow users to adjust weights
    weights = adjust_weights(default_weights)

    # Collect user inputs
    scores = {
        "time_investment": float(input("Time Investment (hours per week, 0 = 0 hrs, 5 = 20+ hrs): ")),
        "prior_experience": float(input("Prior Experience (0 = none, 5 = expert): ")),
        "access_to_resources": float(input("Access to Resources (0 = poor, 5 = excellent): ")),
        "mentorship_support": float(input("Mentorship/Support (0 = none, 5 = very strong): ")),
        "motivation": float(input("Motivation (0 = not motivated, 5 = extremely motivated): ")),
        "technical_skills": float(input("Technical Skills (0 = beginner, 5 = expert): ")),
        "portfolio_quality": float(input("Portfolio Quality (0 = none, 5 = impressive): ")),
        "job_market_demand": float(input("Job Market Demand (0 = low, 5 = high): ")),
        "networking": float(input("Networking (0 = none, 5 = very active): ")),
        "resilience": float(input("Resilience (0 = low, 5 = high): ")),
        "financial_stability": float(input("Financial Stability (0 = none, 5 = very secure): ")),
        "economic_conditions": float(input("Economic Conditions (0 = recession, 5 = booming): ")),
        "industry_trends": float(input("Industry Trends (0 = outdated, 5 = cutting-edge): ")),
        "consistency": float(input("Consistency (0 = sporadic, 5 = very consistent): ")),
        "access_to_education": float(input("Access to Education (0 = none, 5 = excellent): ")),
        "social_safety_nets": float(input("Social Safety Nets (0 = none, 5 = strong): ")),
        "burnout_risk": float(input("Burnout Risk (0 = low, 5 = high): ")),
        "imposter_syndrome": float(input("Imposter Syndrome (0 = none, 5 = severe): ")),
        "competition": float(input("Competition (0 = low, 5 = high): ")),
        "learning_curve": float(input("Learning Curve (0 = easy, 5 = very hard): ")),
        "financial_constraints": float(input("Financial Constraints (0 = none, 5 = severe): ")),
        "location": float(input("Location (0 = remote, 5 = tech hub): ")),
        "health": float(input("Health (0 = poor, 5 = excellent): ")),
        "time_management": float(input("Time Management (0 = poor, 5 = excellent): ")),
        "discrimination": float(input("Discrimination (0 = none, 5 = high): ")),
    }

    # Calculate log-odds and probability
    log_odds = calculate_log_odds(scores, weights)
    probability = calculate_probability(log_odds)

    # Display results
    print("\nResults:")
    print(f"Log-Odds: {log_odds:.2f}")
    print(f"Probability of Achieving Your Career Goal: {probability * 100:.2f}%")

if __name__ == "__main__":
    main()
