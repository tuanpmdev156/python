"""Functions to prevent a nuclear meltdown."""


def is_criticality_balanced(temperature, neutrons_emitted):
    """Function to check a reactor is balanced in criticality """
    criticality = temperature * neutrons_emitted
    return temperature < 800 and neutrons_emitted > 500 and criticality < 500000


def reactor_efficiency(voltage, current, theoretical_max_power):
    """Function to determine the Power output range"""
    generated_power = voltage * current
    percentage_value = (generated_power/theoretical_max_power)*100
    if percentage_value >= 80:
        return 'green'
    if 60 <= percentage_value < 80:
        return 'orange'
    if 30 <= percentage_value < 60:
        return 'red'
    return 'black'

def fail_safe(temperature, neutrons_produced_per_second, threshold):
    """Function to create a fail-safe mechanism to avoid overload and meltdown."""
    value = temperature * neutrons_produced_per_second
    low_measure = 0.9 * threshold
    start_normal_measure = threshold - 0.1 * threshold
    end_normal_measure =  threshold + 0.1 * threshold
    if  start_normal_measure <= value <= end_normal_measure:
        return 'NORMAL'
    if value < low_measure:
        return 'LOW'
    return 'DANGER'
