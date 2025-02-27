import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_biases = [
            {
                'name': 'Confirmation Bias',
                'description': 'The tendency to search for, interpret, favor, and recall information in a way that confirms or supports one\'s prior beliefs or values.'
            },
            {
                'name': 'Dunning-Kruger Effect',
                'description': 'A cognitive bias in which people with limited knowledge or competence in a given intellectual or social domain greatly overestimate their own knowledge or competence in that domain.'
            }
        ]
        return {str(i+1): bias for i, bias in enumerate(cognitive_biases)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that generates short stories illustrating the cognitive bias of {t['name']}, then analyze the stories to evaluate how effectively they demonstrate the bias. Your response should include:

1. AI System Design (250-300 words):
   a) Describe the key components of your AI system for generating stories based on cognitive biases.
   b) Explain how your system incorporates knowledge of {t['name']} into the story generation process.
   c) Discuss any novel techniques or algorithms used in your approach.

2. Story Generation (200-250 words):
   a) Outline the step-by-step process your AI system uses to generate a story illustrating {t['name']}.
   b) Explain how your system ensures the story effectively demonstrates the bias.
   c) Discuss any challenges in translating psychological concepts into narrative form.

3. Sample Story (200-250 words):
   Provide a sample short story generated by your AI system that illustrates {t['name']}. The story should be engaging and clearly demonstrate the cognitive bias.

4. Story Analysis (250-300 words):
   a) Analyze the generated story, explaining how it illustrates {t['name']}.
   b) Identify specific elements in the story that demonstrate the bias.
   c) Evaluate the effectiveness of the story in conveying the concept of {t['name']} to a general audience.

5. Bias Detection Algorithm (200-250 words):
   a) Design an algorithm that could automatically detect and measure the presence of {t['name']} in generated stories.
   b) Explain how this algorithm would work and what metrics it would use.
   c) Discuss potential challenges and limitations of this approach.

6. Educational Applications (150-200 words):
   a) Propose how your AI system and generated stories could be used in educational settings to teach about cognitive biases.
   b) Discuss potential benefits and drawbacks of using AI-generated content for this purpose.
   c) Suggest an interactive exercise using your system to help students understand {t['name']}.

Ensure your response demonstrates a deep understanding of cognitive psychology, artificial intelligence, and creative writing. Use appropriate terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific accuracy.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1250-1550 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of {t['name']} and how it manifests in human behavior.",
            "The AI system design is innovative and plausible, incorporating relevant AI and NLP techniques.",
            "The sample story effectively illustrates the cognitive bias in an engaging and clear manner.",
            "The story analysis provides insightful observations about how the bias is demonstrated in the narrative.",
            "The bias detection algorithm is well-thought-out and addresses the challenges of automating bias detection in text.",
            "The educational applications are creative and demonstrate an understanding of effective teaching methods.",
            "The overall response shows interdisciplinary knowledge integration and creative problem-solving."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
