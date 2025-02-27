import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        dream_scenarios = [
            {
                "scenario": "Flying through a city of mirrors",
                "emotion": "Exhilaration",
                "symbolic_element": "Reflections"
            },
            {
                "scenario": "Underwater conversation with talking fish",
                "emotion": "Curiosity",
                "symbolic_element": "Communication"
            }
        ]
        return {str(i+1): scenario for i, scenario in enumerate(random.sample(dream_scenarios, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of analyzing and generating dream-like experiences, integrating neuroscientific theories of dreaming, cognitive psychology, and advanced AI techniques. Your system should be able to interpret the following dream scenario: "{t['scenario']}", with a focus on the emotion of {t['emotion']} and the symbolic element of {t['symbolic_element']}. Then, use your system to generate a new dream-like experience based on this analysis.

Your response should include the following sections:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI dream analysis and generation system.
   b) Explain how your system integrates neuroscientific theories of dreaming (e.g., activation-synthesis hypothesis, threat simulation theory).
   c) Detail how your system incorporates cognitive psychology principles related to memory, emotion, and symbolism.
   d) Discuss any novel AI techniques or algorithms used in your design.

2. Dream Analysis Process (250-300 words):
   a) Explain the step-by-step process your AI system uses to analyze the given dream scenario.
   b) Describe how your system identifies and interprets emotional content and symbolic elements.
   c) Discuss how your system accounts for individual and cultural variations in dream interpretation.
   d) Provide a sample analysis of the given dream scenario, highlighting key insights.

3. Dream Generation Process (250-300 words):
   a) Detail the process by which your AI system generates new dream-like experiences.
   b) Explain how your system ensures the generated dreams are coherent yet maintain dream-like qualities.
   c) Describe how your system incorporates emotional and symbolic elements in the generated dreams.
   d) Discuss any ethical considerations in AI-generated dream experiences.

4. Neuroscientific Basis (200-250 words):
   a) Explain how your system's design aligns with current neuroscientific understanding of dream processes.
   b) Discuss how your AI model might contribute to or challenge existing theories of dreaming.
   c) Propose a novel hypothesis about the nature of dreaming based on your AI system's architecture.

5. Generated Dream Scenario (150-200 words):
   Present a new dream scenario generated by your AI system, based on the analysis of the given dream. Explain how this new scenario relates to the original in terms of emotional content and symbolism.

6. Evaluation and Validation (200-250 words):
   a) Propose methods for evaluating the accuracy and meaningfulness of your AI's dream analyses.
   b) Describe how you would validate the 'authenticity' of AI-generated dream experiences.
   c) Discuss the challenges in creating a 'ground truth' for dream interpretation and generation.

7. Potential Applications and Future Directions (150-200 words):
   a) Suggest potential applications of your AI dream analysis and generation system in fields such as psychology, neuroscience, or creative arts.
   b) Propose two future research directions that could enhance our understanding of dreams or consciousness through AI.

Ensure your response demonstrates a deep understanding of neuroscience, cognitive psychology, and artificial intelligence. Use appropriate terminology from these fields and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1500-1850 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The AI system design must address the specific dream scenario: '{t['scenario']}', with a focus on the emotion of {t['emotion']} and the symbolic element of {t['symbolic_element']}",
            "The response should demonstrate a deep understanding of neuroscientific theories of dreaming, cognitive psychology principles, and advanced AI techniques",
            "The dream analysis and generation processes should be logically consistent, scientifically plausible, and innovative",
            "The generated dream scenario should be coherent, incorporate emotional and symbolic elements, and relate to the original dream in a meaningful way",
            "The response should address ethical considerations and challenges in AI-based dream analysis and generation",
            "The proposed evaluation methods and future research directions should be comprehensive, relevant, and insightful",
            "The response should be well-structured, following the outlined format, and within the specified word count"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
