def calculate_home_advantage(is_home_match):
    if is_home_match:
        return 1.1  # 10% advantage
    else:
        return 1.0
