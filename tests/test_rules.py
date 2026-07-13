from mailwatch.rules.loader import load_rules


def test_rule_loader():
    rules = load_rules(
        "src/mailwatch/config/rules.yml"
    )

    assert len(rules) == 1
    assert rules[0]("hello message") == "contains: hello"