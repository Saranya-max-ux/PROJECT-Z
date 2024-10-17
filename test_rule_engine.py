from rule_engine import create_rule, combine_rules, evaluate_rule

# Test creating rules
rule1 = create_rule("age > 30 AND department = 'Sales'")
print(f"Rule 1 AST: {rule1.value}")

# Test combining rules
combined_rule = combine_rules([rule1.value, "age < 25 AND department = 'Marketing'"])
print(f"Combined Rule AST: {combined_rule.value}")

# Test evaluating rules
data = {"age": 35, "department": "Sales"}
result = evaluate_rule(combined_rule, data)
print(f"Evaluation result: {result}")
