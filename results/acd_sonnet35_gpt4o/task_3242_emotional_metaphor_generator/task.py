import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        emotions = [
            "Ambivalence",
            "Nostalgia",
            "Schadenfreude",
            "Sehnsucht",
            "Mono no aware",
            "Saudade",
            "Hygge"
        ]
        return {
            "1": {"emotion": random.choice(emotions)},
            "2": {"emotion": random.choice(emotions)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that generates and analyzes metaphors for the complex emotion of {t['emotion']}, then use it to create a 'metaphor map' for navigating this emotional state. Your response should include:

1. Emotion Analysis (200-250 words):
   a) Define and explain {t['emotion']}, including its cultural context and nuances.
   b) Identify key components or aspects of this emotion that could be represented metaphorically.
   c) Discuss any challenges in computationally representing or generating metaphors for this emotion.

2. Metaphor Generation System (250-300 words):
   a) Describe the architecture of your AI system for generating metaphors.
   b) Explain how your system incorporates emotional understanding and creative language use.
   c) Detail any novel techniques or algorithms employed in your metaphor generation process.
   d) Provide two example metaphors generated by your system for {t['emotion']}, explaining their significance.

3. Metaphor Analysis (200-250 words):
   a) Describe how your system would analyze and evaluate the generated metaphors.
   b) Explain the criteria used to assess the quality and emotional resonance of the metaphors.
   c) Discuss how your system might handle cultural variations in metaphor interpretation.

4. Metaphor Map Creation (250-300 words):
   a) Explain the concept of a 'metaphor map' for navigating the emotional state of {t['emotion']}.
   b) Describe how your system would construct this map using the generated metaphors.
   c) Detail how this map could be used to understand or navigate the complexities of {t['emotion']}.
   d) Provide a textual description or ASCII representation of what this metaphor map might look like.

5. Applications and Implications (150-200 words):
   a) Propose two potential applications of your emotional metaphor generation system and metaphor maps.
   b) Discuss the ethical implications of using AI to generate and analyze emotional metaphors.
   c) Explore how this system might contribute to our understanding of emotion, language, and cognition.

Ensure your response demonstrates a deep understanding of emotions, metaphor theory, and artificial intelligence. Use appropriate terminology from psychology, linguistics, and computer science, providing explanations where necessary. Be creative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1050-1300 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of the given emotion and its cultural context.",
            "The AI system design for metaphor generation is innovative, detailed, and scientifically plausible.",
            "The metaphor analysis process is well-explained and considers cultural variations.",
            "The concept of a 'metaphor map' is clearly explained and creatively implemented.",
            "The generated metaphors and metaphor map effectively capture the nuances of the given emotion.",
            "The response shows strong interdisciplinary reasoning, combining insights from psychology, linguistics, and AI.",
            "The applications and implications are thoughtfully explored, including ethical considerations.",
            "The writing is clear, well-structured, and adheres to the specified format and word limits for each section."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
