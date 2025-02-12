import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        concepts = [
            "time",
            "love",
            "death",
            "success",
            "knowledge"
        ]
        cultures = [
            "Chinese",
            "Indian",
            "Nigerian",
            "Brazilian",
            "Russian"
        ]
        tasks = {}
        for i in range(2):
            tasks[str(i+1)] = {
                "concept": random.choice(concepts),
                "culture": random.choice(cultures)
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of generating and interpreting metaphors across different cultures and languages, then apply it to analyze and create metaphors for the concept of {t['concept']} in {t['culture']} culture. Your response should include:

1. AI System Architecture (300-350 words):
   a) Describe the key components of your AI system for metaphor generation and interpretation.
   b) Explain how the system incorporates cultural knowledge and linguistic patterns.
   c) Detail the data sources or knowledge bases the system would use.
   d) Discuss any novel machine learning models or algorithms employed in the system.

2. Cross-Cultural Metaphor Analysis (250-300 words):
   a) Explain how your AI system would analyze existing metaphors for {t['concept']} in {t['culture']} culture.
   b) Describe the process of extracting cultural nuances and conceptual mappings.
   c) Discuss how the system compares these metaphors with those from other cultures.

3. Metaphor Generation Process (250-300 words):
   a) Detail the step-by-step process your AI system uses to generate new metaphors.
   b) Explain how it ensures cultural appropriateness and linguistic coherence.
   c) Describe any creativity-enhancing mechanisms in your system.

4. Generated Metaphors (200-250 words):
   Present three novel metaphors for {t['concept']} generated by your AI system for {t['culture']} culture. For each metaphor:
   a) Provide the metaphor and its meaning.
   b) Explain the cultural elements it incorporates.
   c) Discuss how it differs from common metaphors for this concept in other cultures.

5. Evaluation and Limitations (200-250 words):
   a) Propose methods to evaluate the cultural authenticity and effectiveness of the generated metaphors.
   b) Discuss potential limitations or biases in your AI system's approach.
   c) Suggest areas for future improvement or expansion of the system.

6. Ethical and Cultural Considerations (150-200 words):
   a) Discuss ethical implications of using AI to generate culturally-specific metaphors.
   b) Address potential concerns about cultural appropriation or misrepresentation.
   c) Propose guidelines for responsible development and use of cross-cultural AI systems.

Ensure your response demonstrates a deep understanding of metaphor theory, cultural anthropology, and AI system design. Use appropriate terminology and provide clear explanations for complex concepts. Be creative and culturally sensitive in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of metaphor theory and cultural nuances.",
            "The AI system design is innovative and plausibly incorporates cultural knowledge and linguistic patterns.",
            "The generated metaphors are creative, culturally appropriate, and coherent.",
            "The analysis includes thoughtful consideration of ethical implications and cultural sensitivity.",
            "The response addresses all required sections with appropriate depth and clarity."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
