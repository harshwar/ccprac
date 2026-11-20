# Practical 6: Crisp vs. Fuzzy Membership for Temperature
# Expected/Sample inputs: 40 (hot), 32 (warm), 20 (cool)

def evaluate_temperature(temperature):
    # PART 1: CRISP MEMBERSHIP
    print("CRISP MEMBERSHIP")
    temperature_set = [20, 25, 30, 35, 40]
    if temperature in temperature_set:
        crisp_output = 1
    else:
        crisp_output = 0

    print("Temperature =", temperature, "°C")
    print("Crisp Membership =", crisp_output)

    # PART 2: FUZZY MEMBERSHIP
    print("FUZZY MEMBERSHIP")
    def hot_membership(temp):
        if temp <= 25:
            return 0
        elif temp >= 40:
            return 1
        else:
            return (temp - 25) / (40 - 25)

    fuzzy_output = hot_membership(temperature)
    print("Temperature =", temperature, "°C")
    print("Fuzzy Membership in HOT =", round(fuzzy_output, 2))

if __name__ == "__main__":
    temp_input = input("Enter temperature in °C (e.g. 40, 32, 20) [Press enter for 40]: ").strip()
    temperature = float(temp_input) if temp_input else 40.0
    evaluate_temperature(temperature)
