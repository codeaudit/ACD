import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        source_domains = [
            "journey",
            "war",
            "building",
            "plant",
            "machine"
        ]
        target_domains = [
            "love",
            "time",
            "idea",
            "economy",
            "life"
        ]
        abstract_concepts = [
            "justice",
            "consciousness",
            "democracy",
            "innovation",
            "sustainability"
        ]
        tasks = {}
        for i in range(1, 3):
            tasks[str(i)] = {
                "source_domain": random.choice(source_domains),
                "target_domain": random.choice(target_domains),
                "abstract_concept": random.choice(abstract_concepts)
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design an AI system capable of generating and interpreting novel conceptual metaphors, then apply it to the following scenario:\n\nSource domain: {t['source_domain']}\nTarget domain: {t['target_domain']}\nAbstract concept to explore: {t['abstract_concept']}\n\nYour response should include the following sections:\n\n1. Conceptual Metaphor System Design (300-350 words):\n   a) Describe the key components and processes of your AI system for generating and interpreting conceptual metaphors.\n   b) Explain how your system integrates knowledge from cognitive linguistics, psychology, and artificial intelligence.\n   c) Discuss any novel algorithms or approaches used in your system.\n   d) Provide a high-level diagram or flowchart of your system (describe it textually).\n\n2. Metaphor Generation and Analysis (250-300 words):\n   a) Use your AI system to generate a novel conceptual metaphor mapping the given source domain to the target domain.\n   b) Explain the reasoning behind this metaphor and how it illuminates aspects of the target domain.\n   c) Analyze the strengths and limitations of this metaphor.\n\n3. Abstract Concept Exploration (250-300 words):\n   a) Apply your system to explore the given abstract concept using the generated metaphor.\n   b) Describe any new insights or perspectives on the abstract concept that emerge from this metaphorical mapping.\n   c) Discuss how your system handles the complexities and potential ambiguities in mapping concrete domains to abstract concepts.\n\n4. Cross-domain Inference (200-250 words):\n   a) Explain how your system could use the generated metaphor to make inferences or predictions about the target domain or abstract concept.\n   b) Provide an example of a non-obvious inference derived from the metaphorical mapping.\n   c) Discuss the potential risks or limitations of relying on metaphorical reasoning for understanding complex domains.\n\n5. Evaluation and Implications (200-250 words):\n   a) Propose methods for evaluating the quality, novelty, and usefulness of the metaphors generated by your system.\n   b) Discuss potential applications of your conceptual metaphor AI system in fields such as education, scientific research, or creative problem-solving.\n   c) Explore the philosophical implications of an AI system capable of generating and manipulating conceptual metaphors.\n\nEnsure your response demonstrates a deep understanding of conceptual metaphor theory, cognitive linguistics, and artificial intelligence. Be creative and innovative in your approach while maintaining scientific plausibility. Use clear headings for each section and number your paragraphs within each section.\n\nYour total response should be between 1200-1450 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of conceptual metaphor theory and how it can be applied to AI systems",
            f"The proposed AI system design is innovative, plausible, and effectively addresses the generation and interpretation of conceptual metaphors",
            f"The generated metaphor mapping {t['source_domain']} to {t['target_domain']} is novel and insightful",
            f"The exploration of the abstract concept '{t['abstract_concept']}' using the generated metaphor provides new perspectives or insights",
            "The response shows strong interdisciplinary knowledge integration between cognitive linguistics, psychology, and artificial intelligence",
            "The cross-domain inference example is non-obvious and demonstrates the potential of metaphorical reasoning",
            "The evaluation methods and discussion of implications are thoughtful and consider both potential benefits and risks"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
