import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        language_features = [
            "Recursion",
            "Grammatical tense",
            "Evidentiality",
            "Ergativity",
            "Honorifics"
        ]
        cognitive_principles = [
            "Theory of Mind",
            "Categorization",
            "Analogical reasoning",
            "Social cognition",
            "Embodied cognition"
        ]
        tasks = {
            "1": {
                "language_feature": random.choice(language_features),
                "cognitive_principle": random.choice(cognitive_principles)
            },
            "2": {
                "language_feature": random.choice(language_features),
                "cognitive_principle": random.choice(cognitive_principles)
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that simulates the evolution of language, incorporating principles from linguistics, cognitive science, and evolutionary theory. Then, use your system to evolve a simple protolanguage into a more complex language that includes the feature of {t['language_feature']}, emphasizing the cognitive principle of {t['cognitive_principle']}. Your response should include:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI system for simulating language evolution.
   b) Explain how your system incorporates principles from linguistics, cognitive science, and evolutionary theory.
   c) Detail how your system models language change and the emergence of new features.
   d) Provide a diagram or flowchart illustrating your system's architecture (describe it textually).

2. Protolanguage Design (200-250 words):
   a) Describe the initial protolanguage, including its basic vocabulary and grammar.
   b) Explain how this protolanguage reflects early stages of human language evolution.
   c) Discuss any assumptions or simplifications made in designing the protolanguage.

3. Evolution Simulation (250-300 words):
   a) Explain how your system simulates the evolution of the protolanguage.
   b) Describe the mechanisms for introducing and selecting new language features.
   c) Detail how the cognitive principle of {t['cognitive_principle']} influences the evolution process.
   d) Provide a step-by-step example of how a new linguistic feature might emerge and spread.

4. Evolved Language Analysis (200-250 words):
   a) Describe the key features of the evolved language, focusing on {t['language_feature']}.
   b) Compare the evolved language to the initial protolanguage, highlighting major changes.
   c) Explain how the evolved language reflects the influence of {t['cognitive_principle']}.
   d) Provide an example sentence or phrase in the evolved language, with translation and analysis.

5. Cognitive and Linguistic Implications (200-250 words):
   a) Discuss what your simulation suggests about the relationship between {t['cognitive_principle']} and language evolution.
   b) Analyze how the emergence of {t['language_feature']} might impact cognitive processes or communication.
   c) Consider how this simulation might inform or challenge current theories in cognitive linguistics.

6. Limitations and Future Directions (150-200 words):
   a) Discuss limitations of your approach and potential biases in the simulation.
   b) Suggest how the system could be improved or expanded in future iterations.
   c) Propose an experiment to test a hypothesis generated by your simulation results.

Ensure your response demonstrates a deep understanding of linguistics, cognitive science, and evolutionary theory. Use appropriate terminology and provide clear explanations where necessary. Be creative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1300-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of linguistics, cognitive science, and evolutionary theory",
            "The AI system design is innovative and plausibly incorporates principles from multiple disciplines",
            f"The evolution simulation effectively demonstrates the emergence of {t['language_feature']}",
            f"The cognitive principle of {t['cognitive_principle']} is meaningfully integrated into the language evolution process",
            "The evolved language analysis is detailed and reflects the specified feature and cognitive principle",
            "The response discusses cognitive and linguistic implications of the simulation results",
            "Limitations of the approach are thoughtfully considered and future directions are proposed"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
