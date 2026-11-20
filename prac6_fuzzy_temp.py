def evaluate_temperature(temperature):
    print("CRISP MEMBERSHIP")
    temperature_set = [20, 25, 30, 35, 40]
    if temperature in temperature_set:
        crisp_output = 1
    else:
        crisp_output = 0

    print("Temperature =", temperature, "°C")
    print("Crisp Membership =", crisp_output)

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
    for t in [40, 32, 20]:
        print(f"\n--- Testing for Temperature: {t}°C ---")
        evaluate_temperature(t)
