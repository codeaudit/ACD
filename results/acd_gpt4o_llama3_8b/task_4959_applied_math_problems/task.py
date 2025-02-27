class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"problem": "A company manufactures widgets. The cost to produce x widgets is C(x) = 50x + 2000, and the revenue generated by selling x widgets is R(x) = 100x. Determine the number of widgets the company needs to sell to break even, and calculate the break-even point.", "solution": "The break-even point occurs when the cost equals the revenue. Set C(x) = R(x) and solve for x: 50x + 2000 = 100x. Solving this, we get x = 40 widgets. Therefore, the break-even point is at 40 widgets."},
            "2": {"problem": "A farmer has 100 meters of fencing and wants to enclose a rectangular area. What dimensions should the rectangle have to maximize the enclosed area? Use calculus to find the solution.", "solution": "Let the length of the rectangle be L and the width be W. The perimeter is given by 2L + 2W = 100, or L + W = 50. The area A is given by A = L * W. To maximize the area, express W in terms of L: W = 50 - L. Then, A = L(50 - L) = 50L - L^2. Differentiate A with respect to L and set the derivative to 0: dA/dL = 50 - 2L = 0. Solving this, we get L = 25. Substituting back, we get W = 25. Thus, the dimensions are 25 meters by 25 meters."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Solve the following mathematical problem using the appropriate calculus or linear algebra techniques. Provide a detailed solution and show all your work. Submit your response in the following format:

Problem: {t['problem']}

Solution: [Your detailed solution here, showing all steps]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The solution should correctly apply the appropriate mathematical techniques.", "All steps of the solution should be shown clearly.", "The final answer should be correct."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
