import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cultures = ['Japanese', 'Brazilian', 'Kenyan', 'Norwegian']
        communication_modes = ['Facial expressions', 'Gestures', 'Posture', 'Proxemics', 'Paralanguage']
        emotions = ['Joy', 'Anger', 'Surprise', 'Confusion', 'Empathy']
        contexts = ['Business negotiation', 'Casual conversation', 'Conflict resolution', 'Storytelling']
        
        return {
            "1": {
                "culture": random.choice(cultures),
                "primary_mode": random.choice(communication_modes),
                "secondary_mode": random.choice([m for m in communication_modes if m != "primary_mode"]),
                "emotion": random.choice(emotions),
                "context": random.choice(contexts)
            },
            "2": {
                "culture": random.choice(cultures),
                "primary_mode": random.choice(communication_modes),
                "secondary_mode": random.choice([m for m in communication_modes if m != "primary_mode"]),
                "emotion": random.choice(emotions),
                "context": random.choice(contexts)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a simulation system that models embodied multimodal communication, focusing on {t['culture']} culture, with primary emphasis on {t['primary_mode']} and secondary emphasis on {t['secondary_mode']}. Use this system to generate and analyze an interaction scenario expressing {t['emotion']} in the context of {t['context']}. Your response should include:\n\n1. Simulation System Architecture (300-350 words):\n   a) Describe the key components of your simulation system.\n   b) Explain how it integrates verbal and non-verbal communication modes.\n   c) Detail how cultural nuances are incorporated into the model.\n   d) Discuss any novel algorithms or techniques used in your system.\n\n2. Cultural and Cognitive Modeling (250-300 words):\n   a) Analyze how {t['culture']} culture typically expresses {t['emotion']} through {t['primary_mode']} and {t['secondary_mode']}.\n   b) Explain how your model captures these cultural and emotional nuances.\n   c) Discuss challenges in computationally representing embodied cognition and cultural variations.\n\n3. Interaction Scenario Generation (250-300 words):\n   a) Describe an interaction scenario generated by your system for expressing {t['emotion']} in {t['context']}.\n   b) Explain how {t['primary_mode']} and {t['secondary_mode']} are used in this scenario.\n   c) Analyze how cultural factors influence the generated scenario.\n\n4. AI Language Model Integration (200-250 words):\n   a) Propose a method to present this multimodal scenario to an AI language model.\n   b) Discuss challenges in translating non-verbal cues into a format understandable by current language models.\n   c) Suggest how this integration could enhance AI's understanding of human communication.\n\n5. Evaluation and Validation (200-250 words):\n   a) Propose methods to validate the accuracy and cultural authenticity of your simulation.\n   b) Discuss how you would measure an AI's performance in interpreting the multimodal scenario.\n   c) Address potential biases and limitations in your approach.\n\n6. Ethical Considerations and Future Directions (150-200 words):\n   a) Discuss ethical implications of modeling and simulating cultural communication patterns.\n   b) Propose guidelines for responsible development and use of such technology.\n   c) Suggest future research directions to enhance the system's capabilities.\n\nEnsure your response demonstrates a deep understanding of linguistics, cognitive science, cultural anthropology, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific and cultural authenticity.\n\nFormat your response with clear headings for each section, numbered as above. Your total response should be between 1350-1650 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of linguistics, cognitive science, cultural anthropology, and artificial intelligence.",
            "The simulation system design is innovative, plausible, and effectively integrates verbal and non-verbal communication modes.",
            "The cultural and cognitive modeling shows a nuanced understanding of the specified culture and emotion.",
            "The generated interaction scenario is culturally authentic and effectively uses the specified communication modes.",
            "The proposed AI language model integration method is creative and addresses key challenges.",
            "Ethical considerations are thoughtfully analyzed and addressed.",
            "The response is well-structured, clear, and within the specified word count."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
