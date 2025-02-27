import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        humor_types = [
            "Wordplay",
            "Situational comedy",
            "Sarcasm",
            "Absurdism"
        ]
        cultural_contexts = [
            "Western",
            "East Asian",
            "Middle Eastern",
            "African"
        ]
        cognitive_processes = [
            "Incongruity resolution",
            "Superiority theory",
            "Relief theory",
            "Benign violation theory"
        ]
        tasks = {}
        for i in range(1, 3):
            humor_type = random.choice(humor_types)
            context = random.choice(cultural_contexts)
            process = random.choice(cognitive_processes)
            tasks[str(i)] = {"humor_type": humor_type, "context": context, "process": process}
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design an AI system that simulates and analyzes the cognitive processes involved in humor appreciation and creation, focusing on {t['humor_type']} in a {t['context']} cultural context. Your system should emphasize the {t['process']} of humor. Then, use your system to generate and evaluate jokes. Your response should include:\n\n1. Cognitive Model Design (300-350 words):\n   a) Describe the key components of your AI system for simulating humor-related cognitive processes.\n   b) Explain how your model incorporates the specified humor theory ({t['process']}).\n   c) Detail how your system accounts for cultural context in humor appreciation and creation.\n   d) Discuss any novel computational approaches used to model humor cognition.\n\n2. Humor Generation Process (250-300 words):\n   a) Explain the step-by-step process your AI system uses to generate {t['humor_type']} jokes.\n   b) Describe how the system incorporates {t['context']} cultural elements in joke creation.\n   c) Discuss how the {t['process']} is reflected in the joke generation process.\n\n3. Joke Evaluation Mechanism (200-250 words):\n   a) Describe how your system evaluates the humor and cultural appropriateness of generated jokes.\n   b) Explain how the evaluation process relates to the cognitive model of humor appreciation.\n   c) Discuss any potential biases in your evaluation system and how you address them.\n\n4. Sample Jokes and Analysis (250-300 words):\n   a) Present two jokes generated by your system, targeting the {t['context']} cultural context.\n   b) Analyze these jokes in terms of their use of {t['humor_type']} and alignment with the {t['process']}.\n   c) Provide your system's evaluation of these jokes and explain the reasoning behind the scores.\n\n5. Cognitive Science Implications (200-250 words):\n   a) Discuss how your model contributes to our understanding of humor cognition.\n   b) Analyze any insights your system provides about cultural differences in humor appreciation.\n   c) Propose an experiment to test a key prediction of your model about human humor processing.\n\n6. Ethical Considerations and Limitations (150-200 words):\n   a) Discuss potential ethical issues related to AI-generated humor and cultural representation.\n   b) Analyze the limitations of your system in capturing the full complexity of human humor.\n   c) Propose guidelines for responsible development and use of humor-generating AI systems.\n\n7. Future Directions (100-150 words):\n   a) Suggest two potential improvements or extensions to your cognitive humor AI system.\n   b) Propose a related research question that could further our understanding of humor, cognition, and AI.\n\nEnsure your response demonstrates a deep understanding of cognitive science, humor theory, and artificial intelligence. Use appropriate terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility.\n\nFormat your response with clear headings for each section. Your total response should be between 1450-1800 words. Include a word count at the end of your response."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of {t['humor_type']} and its cognitive processes",
            f"The AI system effectively incorporates the {t['process']} of humor",
            f"The model accounts for {t['context']} cultural elements in humor generation and appreciation",
            "The generated jokes are creative and align with the specified humor type and cultural context",
            "The joke evaluation mechanism is well-explained and considers both humor and cultural appropriateness",
            "The discussion of cognitive science implications shows insight into humor cognition and cultural differences",
            "The ethical considerations and limitations are thoughtfully addressed",
            "The proposed future directions are innovative and promising for advancing the field",
            "The response adheres to the specified word count and formatting guidelines"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
