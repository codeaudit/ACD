import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        challenges = [
            "optimizing photosynthesis efficiency using quantum coherence",
            "enhancing enzyme catalysis through quantum tunneling"
        ]
        tasks = {
            "1": {"challenge": random.choice(challenges)},
            "2": {"challenge": random.choice(challenges)}
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that applies principles of quantum biology to solve complex biological problems, then use it to address the challenge of {t['challenge']}. Your response should include the following sections:

1. Quantum Biology AI System Architecture (250-300 words):
   a) Describe the key components of your AI system for quantum biology problem-solving.
   b) Explain how your system integrates quantum mechanical principles with biological processes.
   c) Detail how the system models and simulates quantum effects in biological systems.
   d) Include a high-level diagram or pseudocode illustrating the system's architecture (describe it textually).

2. Quantum-Biological Modeling (200-250 words):
   a) Explain how your AI system models quantum effects in biological systems.
   b) Describe any novel algorithms or approaches used in your design.
   c) Discuss how your model handles the transition between quantum and classical regimes in biological systems.

3. Application to the Specific Challenge (250-300 words):
   a) Analyze how you would apply your AI system to the challenge of {t['challenge']}.
   b) Describe the key parameters and initial conditions for addressing this challenge.
   c) Predict potential outcomes and improvements that might arise from your approach.
   d) Discuss how quantum effects might influence the biological process in your simulation.

4. Data Analysis and Interpretation (200-250 words):
   a) Propose methods for analyzing the results generated by your AI system.
   b) Explain how you would validate the quantum biological model against experimental data.
   c) Discuss the potential implications of your results for our understanding of biological systems.

5. Comparative Analysis (150-200 words):
   a) Compare your quantum biology AI approach to traditional computational biology methods.
   b) Discuss the potential advantages and limitations of your system.
   c) Explain how your system might provide insights that classical models cannot.

6. Ethical Considerations and Future Directions (150-200 words):
   a) Address potential ethical concerns related to using AI for quantum biology simulations.
   b) Suggest future research directions or potential applications of your system in fields such as medicine, biotechnology, or environmental science.
   c) Discuss how your system might be extended to incorporate other quantum or biological phenomena.

Ensure your response demonstrates a deep understanding of quantum mechanics, biology, and artificial intelligence. Be innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section. Your total response should be between 1200-1500 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of quantum mechanics, biology, and artificial intelligence.",
            "The AI system design is innovative and scientifically plausible.",
            "The specific challenge is thoroughly addressed using the proposed AI system.",
            "The response addresses all required sections with appropriate depth and clarity.",
            "Technical terminology is used correctly and complex concepts are clearly explained."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
