import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'cognitive_framework': 'Conceptual Metaphor Theory',
                'target_domain': 'time',
                'source_domain': 'space',
                'application_context': 'explaining scientific concepts'
            },
            {
                'cognitive_framework': 'Blending Theory',
                'target_domain': 'emotions',
                'source_domain': 'weather',
                'application_context': 'creative writing'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that generates and interprets metaphors based on the {t['cognitive_framework']}, focusing on metaphors that map from the source domain of {t['source_domain']} to the target domain of {t['target_domain']}. Then, analyze its output and propose experiments to test its effectiveness in enhancing human creativity and communication in the context of {t['application_context']}. Your response should include:

1. System Architecture (250-300 words):
   a) Describe the key components of your AI system for metaphor generation and interpretation.
   b) Explain how it incorporates the specified cognitive framework.
   c) Detail how the system maps between the source and target domains.
   d) Include a simple diagram or flowchart of your system architecture using ASCII art or Unicode characters.

2. Metaphor Generation Process (200-250 words):
   a) Explain how your AI system generates novel metaphors.
   b) Describe how it ensures the metaphors are coherent and meaningful.
   c) Discuss any constraints or guidelines built into the system.

3. Metaphor Interpretation (200-250 words):
   a) Detail how your system interprets and analyzes metaphors.
   b) Explain how it identifies the underlying conceptual mappings.
   c) Discuss how the system handles ambiguity or multiple interpretations.

4. Output Analysis (150-200 words):
   a) Provide an example metaphor generated by your system.
   b) Analyze this metaphor in terms of its cognitive and linguistic structure.
   c) Discuss potential insights into human cognition that could be gained from this system.

5. Application to {t['application_context']} (200-250 words):
   a) Explain how your system could be used in the specified context.
   b) Discuss potential benefits and challenges of using AI-generated metaphors in this area.
   c) Propose a specific use case or scenario.

6. Experimental Design (200-250 words):
   a) Propose an experiment to test the effectiveness of your AI metaphor system in enhancing human creativity and communication.
   b) Describe the methodology, including participant selection, data collection, and analysis techniques.
   c) Explain how you would measure both the quality of the metaphors and their impact on human users.

7. Ethical Considerations (100-150 words):
   a) Discuss potential ethical implications of using AI for metaphor generation and interpretation.
   b) Address concerns related to creativity, authorship, and the role of AI in human communication.
   c) Propose guidelines for responsible development and use of such systems.

Ensure your response demonstrates a deep understanding of cognitive science, linguistics, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility.

Format your answer with clear headings for each section, numbered as above. Your total response should be between 1300-1650 words. Stay within the specified word count for each section.

For the system architecture diagram, use ASCII art or Unicode characters to create a clear and informative representation. The diagram should be no larger than 20 lines by 80 characters."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of the specified cognitive framework and its application to metaphor generation and interpretation.",
            "The AI system design is innovative, coherent, and plausibly incorporates principles from cognitive science, linguistics, and artificial intelligence.",
            "The metaphor generation and interpretation processes are clearly explained and demonstrate an understanding of the complexities involved.",
            "The output analysis shows insightful interpretation of the AI-generated metaphor.",
            "The application to the specified context is well-thought-out and considers both benefits and challenges.",
            "The experimental design is well-structured and addresses the effectiveness of the system in enhancing human creativity and communication.",
            "Ethical considerations are thoughtfully discussed, and proposed guidelines are reasonable.",
            "The response is well-organized, adheres to the specified structure and word counts, and effectively uses technical terminology."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
