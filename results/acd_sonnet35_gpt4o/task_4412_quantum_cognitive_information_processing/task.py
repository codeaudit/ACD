class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "quantum_concept": "entanglement",
                "information_theory_concept": "mutual information",
                "cognitive_process": "decision making under uncertainty",
                "application_scenario": "financial market behavior"
            },
            "2": {
                "quantum_concept": "superposition",
                "information_theory_concept": "channel capacity",
                "cognitive_process": "memory consolidation",
                "application_scenario": "learning in artificial neural networks"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical framework that integrates quantum mechanics, information theory, and cognitive science to model human decision-making processes, then apply it to analyze and predict behavior in complex scenarios. Focus on the quantum concept of {t['quantum_concept']}, the information theory concept of {t['information_theory_concept']}, and the cognitive process of {t['cognitive_process']}. Apply your framework to analyze {t['application_scenario']}. Your response should include:

1. Theoretical Framework (300-350 words):
   a) Describe your integrated framework, explaining how it combines quantum mechanics, information theory, and cognitive science.
   b) Explain how you incorporate {t['quantum_concept']} and {t['information_theory_concept']} into your model of {t['cognitive_process']}.
   c) Provide a formal mathematical representation of your framework, including at least two key equations or formulas using appropriate notation from each field.
   d) Discuss how your framework models the specified cognitive process in quantum information terms.

2. Cognitive Process Modeling (250-300 words):
   a) Apply your framework to model {t['cognitive_process']}.
   b) Explain how your model captures key features of this cognitive process.
   c) Provide a specific example or illustration of how your model represents a typical instance of this cognitive process.
   d) Discuss potential insights your model offers into the nature of human cognition.

3. Application Scenario Analysis (250-300 words):
   a) Apply your framework to analyze {t['application_scenario']}.
   b) Describe how your model interprets and predicts behavior in this scenario.
   c) Identify at least three specific predictions or insights generated by your framework.
   d) Compare these predictions to those of classical models in the field.

4. Experimental Design (200-250 words):
   a) Propose an experiment to test the predictions of your framework in the given scenario.
   b) Explain how the experiment would distinguish your model's predictions from classical cognitive models.
   c) Describe the methodology, including sample size, data collection, and analysis techniques.
   d) Discuss potential challenges in implementing and interpreting this experiment.

5. Implications and Ethical Considerations (150-200 words):
   a) Discuss the philosophical implications of your framework for understanding human cognition.
   b) Address ethical considerations in applying quantum models to human behavior.
   c) Explore potential societal impacts of using your framework in the given scenario.

6. Limitations and Future Directions (150-200 words):
   a) Identify at least three limitations of your theoretical framework and proposed experiment.
   b) Suggest two future research directions to extend or refine your approach.
   c) Speculate on how advancements in quantum computing or neuroscience might impact your framework.

Ensure your response demonstrates a deep understanding of quantum mechanics, information theory, and cognitive science. Use appropriate mathematical notation and provide clear explanations for complex concepts. Be creative and speculative in your approach while maintaining scientific rigor and plausibility.

Format your response with clear headings for each section and numbered subsections as outlined above. Adhere strictly to the word limits provided for each section. Your total response should be between 1300-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding and creative integration of quantum mechanics, information theory, and cognitive science, with clear explanations of complex concepts.",
            "The theoretical framework is coherent, innovative, and well-explained, with at least two appropriate mathematical equations or formulas.",
            "The application of the framework to the given scenario is insightful and generates at least three specific predictions or insights.",
            "The proposed experiment is well-designed, with a clear methodology that distinguishes the framework's predictions from classical models.",
            "The discussion of implications, limitations, and future directions is thoughtful and demonstrates a broad understanding of the field, including at least three limitations and two future research directions.",
            "The response adheres to the specified format and word limits for each section."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
