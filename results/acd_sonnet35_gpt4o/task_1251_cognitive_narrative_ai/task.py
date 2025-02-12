import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_models = [
            ("Episodic Memory", "The system that allows humans to recall specific past experiences"),
            ("Working Memory", "The cognitive system responsible for temporarily holding and manipulating information"),
            ("Emotional Regulation", "The process by which individuals influence which emotions they have, when they have them, and how they experience and express them"),
            ("Theory of Mind", "The ability to attribute mental states to oneself and others, and to understand that others have beliefs, desires, and intentions that are different from one's own"),
            ("Cognitive Dissonance", "The mental discomfort experienced when holding two or more contradictory beliefs, ideas, or values")
        ]
        
        psychological_concepts = [
            "Identity Formation",
            "Resilience",
            "Cognitive Bias",
            "Social Influence",
            "Moral Development"
        ]
        
        narrative_elements = [
            "Character Arc",
            "Plot Structure",
            "Symbolism",
            "Point of View",
            "Theme"
        ]
        
        return {
            "1": {
                "cognitive_model": random.choice(cognitive_models),
                "psychological_concept": random.choice(psychological_concepts),
                "narrative_element": random.choice(narrative_elements)
            },
            "2": {
                "cognitive_model": random.choice(cognitive_models),
                "psychological_concept": random.choice(psychological_concepts),
                "narrative_element": random.choice(narrative_elements)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design an AI system capable of generating and analyzing narratives based on cognitive models of human memory and emotion, focusing on the cognitive model of {t['cognitive_model'][0]} ({t['cognitive_model'][1]}). Then, apply this system to create a story that explores the psychological concept of {t['psychological_concept']}, with particular emphasis on the narrative element of {t['narrative_element']}. Your response should include:\n\n1. System Architecture (250-300 words):\n   a) Describe the key components of your AI narrative generation and analysis system.\n   b) Explain how your system incorporates the specified cognitive model.\n   c) Detail how the system integrates principles from AI, cognitive science, and narrative theory.\n   d) Include a diagram or flowchart of your system architecture (describe it in words).\n\n2. Cognitive-Narrative Mapping (200-250 words):\n   a) Explain your approach to mapping cognitive processes to narrative elements.\n   b) Discuss how your system represents and manipulates the specified cognitive model in narrative form.\n   c) Provide an example of how a specific aspect of the cognitive model would be translated into a narrative element.\n\n3. Story Generation Process (200-250 words):\n   a) Describe the step-by-step process your AI system would use to generate a story.\n   b) Explain how the system incorporates the specified psychological concept into the narrative.\n   c) Discuss how the system ensures the prominence of the specified narrative element.\n\n4. Sample Story Outline (200-250 words):\n   Provide a brief outline of a story generated by your system, including:\n   a) A summary of the plot\n   b) A description of the main character(s)\n   c) An explanation of how the story explores the specified psychological concept\n   d) An analysis of how the specified narrative element is utilized\n\n5. Narrative Analysis Capabilities (150-200 words):\n   a) Explain how your AI system would analyze the generated story.\n   b) Describe the key features or metrics the system would use in its analysis.\n   c) Discuss how the system's analysis could provide insights into human cognition and storytelling.\n\n6. Ethical Considerations and Limitations (150-200 words):\n   a) Discuss potential ethical implications of using AI to model human cognitive processes and generate narratives.\n   b) Address concerns about the authenticity and value of AI-generated stories.\n   c) Identify limitations of your system and propose areas for future improvement.\n\n7. Interdisciplinary Implications (150-200 words):\n   a) Discuss how your system could contribute to advancements in AI, cognitive science, and literary studies.\n   b) Propose potential applications of your system in fields such as education, therapy, or entertainment.\n\nEnsure your response demonstrates a deep understanding of AI architectures, cognitive science theories, and narrative techniques. Be creative in your approach while maintaining scientific plausibility. Use appropriate terminology from all relevant fields and provide clear explanations where necessary.\n\nYour total response should be between 1300-1650 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of AI architectures, cognitive science theories, and narrative techniques.",
            "The proposed system effectively incorporates the specified cognitive model and psychological concept.",
            "The story generation process and sample outline are creative, coherent, and aligned with the given parameters.",
            "The narrative analysis capabilities are well-explained and show potential for providing insights into human cognition and storytelling.",
            "Ethical considerations and limitations are thoughtfully addressed.",
            "The interdisciplinary implications and potential applications are innovative and well-reasoned."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
