import Lab2.BMI as bmi

def test_bmi_normal_weight():
    assert bmi.calculate_bmi(1.0, 24) == 0

def test_bmi_over_weight():
    assert bmi.calculate_bmi(1.0, 26) == 1

def test_bmi_under_weight():
    assert bmi.calculate_bmi(1.0, 18) == -1