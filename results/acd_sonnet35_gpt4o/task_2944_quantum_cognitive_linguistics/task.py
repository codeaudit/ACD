import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "quantum_principle": "superposition",
                "linguistic_aspect": "semantic ambiguity",
                "target_language": "Mandarin Chinese"
            },
            {
                "quantum_principle": "entanglement",
                "linguistic_aspect": "syntactic dependencies",
                "target_language": "Arabic"
            },
            {
                "quantum_principle": "wave function collapse",
                "linguistic_aspect": "phonological perception",
                "target_language": "Finnish"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical framework that integrates the quantum mechanics principle of {t['quantum_principle']} with cognitive linguistics to model and analyze {t['linguistic_aspect']} in language acquisition and processing. Then, apply this framework to develop a novel language learning system for {t['target_language']}. Your response should include:

1. Theoretical Framework (300-350 words):
   a) Explain how you integrate {t['quantum_principle']} with cognitive linguistic theories.
   b) Describe the key components of your framework and their interactions.
   c) Discuss how this integration provides new insights into {t['linguistic_aspect']}.
   d) Provide a mathematical or conceptual model that represents your framework.

2. Quantum-Linguistic Mapping (250-300 words):
   a) Detail how you map quantum concepts to linguistic phenomena, focusing on {t['linguistic_aspect']}.
   b) Explain any novel predictions or hypotheses generated by this mapping.
   c) Discuss potential challenges or limitations in applying quantum principles to linguistics.

3. Cognitive Processing Model (250-300 words):
   a) Describe how your framework models cognitive processes in language acquisition and processing.
   b) Explain how it accounts for individual differences in language learning.
   c) Discuss how your model might be empirically tested or validated.

4. Language Learning System Design (300-350 words):
   a) Outline a novel language learning system for {t['target_language']} based on your framework.
   b) Explain how it leverages quantum-inspired algorithms to enhance learning of {t['linguistic_aspect']}.
   c) Describe specific features or exercises that target {t['linguistic_aspect']} in {t['target_language']}.
   d) Discuss how your system differs from traditional language learning approaches.

5. Practical Application and Evaluation (200-250 words):
   a) Propose a method to implement and test your language learning system.
   b) Suggest criteria for evaluating its effectiveness compared to conventional methods.
   c) Discuss potential real-world applications beyond language learning.

6. Implications and Future Directions (150-200 words):
   a) Analyze the broader implications of your framework for cognitive science and linguistics.
   b) Suggest two potential extensions or refinements of your approach.
   c) Discuss how this work might influence our understanding of cognition and language.

Ensure your response demonstrates a deep understanding of quantum mechanics, cognitive science, and linguistics. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1450-1750 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of quantum mechanics, cognitive science, and linguistics.",
            "The theoretical framework effectively integrates quantum principles with cognitive linguistics.",
            "The language learning system design is innovative and clearly based on the proposed framework.",
            "The response addresses all required sections with appropriate depth and clarity.",
            "The ideas presented are creative while maintaining scientific plausibility.",
            "The response uses appropriate technical terminology and provides clear explanations for complex concepts."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
