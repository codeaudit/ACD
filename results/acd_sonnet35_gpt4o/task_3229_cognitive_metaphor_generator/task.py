import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        abstract_concepts = [
            {
                "concept": "Time",
                "source_domain": "Space",
                "target_domain": "Economics"
            },
            {
                "concept": "Consciousness",
                "source_domain": "Light",
                "target_domain": "Information Theory"
            }
        ]
        return {
            "1": random.choice(abstract_concepts),
            "2": random.choice(abstract_concepts)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of generating and analyzing novel metaphors based on cognitive linguistics theories, then use it to explore the abstract concept of {t['concept']} by creating a metaphor that maps from the source domain of {t['source_domain']} to the target domain of {t['target_domain']}. Your response should include:

1. Cognitive Linguistics Foundation (200-250 words):
   a) Explain the key principles of cognitive linguistics relevant to metaphor generation and analysis.
   b) Discuss how these principles inform your AI system's approach to metaphor creation.
   c) Describe how your system incorporates theories of conceptual metaphor and mental spaces.

2. AI System Architecture (250-300 words):
   a) Describe the overall structure of your AI metaphor generation and analysis system.
   b) Explain how it incorporates cognitive linguistics principles and theories.
   c) Detail the components for conceptual mapping, metaphor generation, and metaphor analysis.
   d) Discuss how the system handles creative decision-making in metaphor creation.

3. Metaphor Generation Process (200-250 words):
   a) Outline the step-by-step process your AI system uses to generate a novel metaphor.
   b) Explain how the system maps concepts from the source domain to the target domain.
   c) Describe how the system ensures the metaphor is both novel and coherent.

4. Novel Metaphor Creation (200-250 words):
   a) Present a novel metaphor generated by your AI system that explores the concept of {t['concept']} by mapping from {t['source_domain']} to {t['target_domain']}.
   b) Explain the conceptual mappings and entailments of this metaphor.
   c) Discuss how this metaphor provides new insights into the abstract concept.

5. Metaphor Analysis (200-250 words):
   a) Analyze the generated metaphor using your AI system's analytical capabilities.
   b) Discuss the cognitive and linguistic implications of the metaphor.
   c) Explain how the metaphor reflects or challenges existing conceptual frameworks.

6. Evaluation and Refinement (150-200 words):
   a) Propose a method for evaluating the novelty, coherence, and insightfulness of AI-generated metaphors.
   b) Describe how your AI system could improve its metaphor generation based on feedback.
   c) Discuss potential applications of your system in fields such as creative writing, science communication, or cognitive therapy.

7. Ethical and Cultural Considerations (100-150 words):
   a) Discuss potential ethical implications of using AI-generated metaphors in various contexts.
   b) Address how cultural differences might affect the interpretation and effectiveness of generated metaphors.
   c) Propose guidelines for responsible use of AI-generated metaphors in communication and education.

Ensure your response demonstrates a deep understanding of cognitive linguistics, metaphor theory, and AI systems design. Be creative and innovative while maintaining scientific plausibility. Use appropriate terminology throughout your answer.

Your total response should be between 1300-1650 words. Format your response with clear headings for each section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must thoroughly explain an AI system capable of generating and analyzing metaphors based on cognitive linguistics theories.",
            f"The AI system design should demonstrate a clear and plausible integration of cognitive linguistics principles and AI techniques.",
            f"The generated metaphor should explore the concept of {t['concept']} by mapping from {t['source_domain']} to {t['target_domain']}.",
            "The submission must include all seven required sections, adequately addressing each topic.",
            "The response should demonstrate creativity and innovation in AI metaphor generation and analysis while maintaining scientific plausibility.",
            "The analysis of the generated metaphor should be insightful and well-reasoned, showing a deep understanding of cognitive linguistics and metaphor theory.",
            "The response must show a deep understanding of both cognitive linguistics and AI systems design.",
            "The evaluation and refinement section should propose realistic methods for assessing and improving AI-generated metaphors.",
            "The ethical and cultural considerations should be thoughtful and comprehensive."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
