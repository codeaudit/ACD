import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        visual_stimuli = [
            {
                'type': 'abstract painting',
                'style': 'cubism',
                'dominant_colors': ['blue', 'orange', 'gray']
            },
            {
                'type': 'nature scene',
                'style': 'photograph',
                'dominant_elements': ['forest', 'waterfall', 'sunset']
            }
        ]
        return {str(i+1): random.choice(visual_stimuli) for i in range(2)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that simulates musical synesthesia by translating visual input into musical compositions. Your system should be based on cognitive models of cross-modal perception and focus on the following visual input: a {t['type']} in the style of {t['style']}.

Your response should include the following sections:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI system for simulating musical synesthesia.
   b) Explain how your system processes visual input and translates it into musical elements.
   c) Detail how your system incorporates cognitive models of cross-modal perception.
   d) Discuss any novel AI techniques or algorithms used in your simulation.
   e) Provide a high-level diagram of your system architecture (describe it textually).

2. Visual-Auditory Mapping (250-300 words):
   a) Explain how your system maps visual features (e.g., color, shape, texture) to musical elements (e.g., pitch, rhythm, timbre).
   b) Describe the cognitive principles or theories that inform these mappings.
   c) Discuss how your system handles the complexity and subjectivity of synesthetic experiences.

3. Musical Composition Process (250-300 words):
   a) Outline the steps your AI system takes to generate a musical composition from the visual input.
   b) Explain how your system ensures musical coherence and structure in the output.
   c) Describe any music theory principles or compositional techniques incorporated into your system.

4. Cognitive Model Integration (200-250 words):
   a) Detail how your system integrates specific cognitive models of perception and cross-modal processing.
   b) Explain how these models influence the synesthetic translation process.
   c) Discuss any assumptions or simplifications made in applying these cognitive models to AI.

5. Sample Output Analysis (200-250 words):
   a) Describe a hypothetical musical composition generated by your system for the given visual input.
   b) Explain how specific visual elements are reflected in the musical output.
   c) Analyze how the composition reflects both synesthetic principles and musical aesthetics.

6. Evaluation and Validation (150-200 words):
   a) Propose methods to evaluate the quality and authenticity of your system's synesthetic translations.
   b) Discuss how you would validate your system using data from human synesthetes or psychological studies.
   c) Suggest an experiment to compare your AI's output with human-generated synesthetic music.

7. Potential Applications and Implications (150-200 words):
   a) Propose potential applications of your AI system in fields such as art, therapy, or human-computer interaction.
   b) Discuss the implications of this technology for our understanding of perception and creativity.
   c) Address any ethical considerations related to simulating or augmenting human sensory experiences.

Ensure your response demonstrates a deep understanding of cognitive science, music theory, and AI capabilities. Use appropriate terminology and provide clear explanations where necessary. Be creative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Use subheadings a), b), c) etc. as appropriate. Your total response should be between 1500-1850 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a thorough understanding of cognitive science, music theory, and AI principles related to cross-modal perception and synesthesia.",
            "The proposed AI system architecture is innovative, coherent, and clearly explained.",
            "The visual-auditory mapping process is well-thought-out and grounded in cognitive theories.",
            "The musical composition process incorporates both synesthetic principles and musical structure.",
            "The integration of cognitive models is detailed and shows a deep understanding of cross-modal processing.",
            "The sample output analysis provides a clear and creative example of the system's capabilities.",
            "The evaluation and validation methods proposed are scientifically sound and appropriate for the task.",
            "The discussion of potential applications and implications is insightful and considers ethical aspects.",
            "The response is well-structured, within the specified word count, and demonstrates originality and interdisciplinary integration throughout."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
