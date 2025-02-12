import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        sensory_modalities = [
            'visual',
            'auditory',
            'olfactory',
            'gustatory',
            'tactile'
        ]
        problem_domains = [
            'data visualization',
            'music composition',
            'product design',
            'abstract art generation',
            'natural language processing'
        ]
        
        tasks = [
            {
                'primary_modality': random.choice(sensory_modalities),
                'secondary_modality': random.choice([m for m in sensory_modalities if m != primary]),
                'problem_domain': random.choice(problem_domains)
            } for primary in sensory_modalities
        ]
        
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that simulates synesthesia by mapping {t['primary_modality']} inputs to {t['secondary_modality']} outputs to solve problems or generate creative content in the domain of {t['problem_domain']}. Your response should include the following sections:

1. Synesthetic AI Architecture (300-350 words):
   a) Describe the overall structure of your AI system and its key components.
   b) Explain how your system processes {t['primary_modality']} inputs and generates {t['secondary_modality']} outputs.
   c) Detail any novel algorithms or neural network architectures used in your design.
   d) Discuss how your system learns or is trained to create meaningful synesthetic associations.

2. Cognitive Science Foundation (200-250 words):
   a) Explain the relevant principles of synesthesia and cross-modal perception that inform your AI design.
   b) Discuss how your system mimics or diverges from natural synesthetic experiences.
   c) Describe any specific neurological or psychological models that inspired your approach.

3. Application to {t['problem_domain']} (250-300 words):
   a) Provide a detailed example of how your synesthetic AI system could be applied to {t['problem_domain']}.
   b) Explain the potential advantages of using a synesthetic approach in this domain.
   c) Discuss any challenges or limitations specific to this application and how you address them.

4. Creative Output Analysis (200-250 words):
   a) Describe a hypothetical output generated by your system for the given problem domain.
   b) Analyze how the synesthetic mapping contributes to the novelty or effectiveness of the output.
   c) Compare your system's potential creative capabilities to traditional AI approaches in the field.

5. Ethical Considerations and Societal Impact (150-200 words):
   a) Discuss potential ethical implications of simulating synesthesia in AI systems.
   b) Analyze how this technology might impact human creativity and cognitive enhancement.
   c) Propose guidelines for responsible development and use of synesthetic AI systems.

6. Future Research Directions (150-200 words):
   a) Suggest two potential extensions or modifications to your synesthetic AI system.
   b) Propose a research question that arises from your design and its application.
   c) Discuss how this technology might evolve and impact related fields in the next decade.

Ensure your response demonstrates a deep understanding of cognitive science, artificial intelligence, and the specific problem domain. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative and innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section and use subheadings where appropriate. Number your paragraphs within each section as shown above (a, b, c, etc.). Your total response should be between 1250-1550 words. Include a word count at the end of your submission."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of synesthesia, cognitive science, and AI systems.",
            f"The AI architecture clearly incorporates a mapping from {t['primary_modality']} inputs to {t['secondary_modality']} outputs.",
            f"The application to {t['problem_domain']} is well-explained and innovative.",
            "The proposed system and its applications are creative while maintaining scientific plausibility.",
            "Ethical considerations and future research directions are thoughtfully discussed.",
            "The response is well-structured, using appropriate technical terminology and clear explanations.",
            "The response follows the specified format with numbered paragraphs and includes a word count."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
