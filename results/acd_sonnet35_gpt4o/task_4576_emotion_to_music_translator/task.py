import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        emotional_states = [
            "Nostalgic melancholy with a hint of hope",
            "Exhilarating anticipation tinged with anxiety",
            "Serene contentment shadowed by underlying unease",
            "Bittersweet joy amidst profound loss",
            "Overwhelming awe mixed with existential insignificance",
            "Passionate determination despite creeping self-doubt"
        ]
        musical_elements = [
            "Harmonic progression",
            "Melodic contour",
            "Rhythmic pattern",
            "Instrumentation",
            "Tempo changes",
            "Dynamic range"
        ]
        cognitive_processes = [
            "Emotional regulation",
            "Autobiographical memory retrieval",
            "Sensory integration",
            "Attention modulation",
            "Reward processing",
            "Social cognition"
        ]
        nlp_techniques = [
            "Sentiment analysis",
            "Semantic parsing",
            "Emotion classification",
            "Contextual word embeddings",
            "Sequence-to-sequence modeling",
            "Abstractive summarization"
        ]
        tasks = {}
        for i in range(1, 3):
            tasks[str(i)] = {
                "emotional_state": random.choice(emotional_states),
                "musical_element": random.choice(musical_elements),
                "cognitive_process": random.choice(cognitive_processes),
                "nlp_technique": random.choice(nlp_techniques)
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that translates complex emotional states into musical compositions, using principles from cognitive neuroscience and natural language processing. Your system should focus on the emotional state of '{t['emotional_state']}', emphasize the musical element of '{t['musical_element']}', incorporate the cognitive process of '{t['cognitive_process']}', and utilize the NLP technique of '{t['nlp_technique']}'.

Your response should include the following sections:

1. System Architecture (300-350 words):
   a) Describe the key components of your emotion-to-music AI system.
   b) Explain how it incorporates knowledge from music theory, cognitive neuroscience, and NLP.
   c) Detail how the specified cognitive process and NLP technique are integrated into the system.
   d) Provide a high-level diagram or flowchart of your system (describe it textually).
   e) Include at least one example of how your system would process a specific input.

2. Emotion-Music Mapping (250-300 words):
   a) Explain how your system analyzes and represents the given complex emotional state.
   b) Describe how the system translates this emotional representation into musical parameters.
   c) Detail how the specified musical element is particularly emphasized in this translation process.
   d) Discuss any challenges in maintaining emotional fidelity during the translation to music.
   e) Provide a concrete example of how a specific emotion would be mapped to musical elements.

3. Neuroscientific Basis (200-250 words):
   a) Explain how your system models the neural processes involved in emotional processing and music perception.
   b) Discuss how the focus on the specified cognitive process influences the emotion-to-music translation.
   c) Describe how your system accounts for individual differences in emotional and musical experiences.
   d) Reference at least one relevant neuroscientific study or theory to support your approach.

4. NLP Integration (250-300 words):
   a) Describe in detail how the specified NLP technique is used in your system.
   b) Explain any novel adaptations or modifications you've made to this technique for emotion-to-music translation.
   c) Discuss how NLP enhances the system's understanding and representation of complex emotional states.
   d) Provide an example of how your system would process a complex emotional description using NLP.

5. Output Analysis (200-250 words):
   a) Provide a detailed description of a hypothetical musical composition generated by your system for the given emotional state.
   b) Analyze how this output demonstrates the integration of emotional, cognitive, and musical elements.
   c) Discuss potential variations in the output and how they might reflect nuances of the emotional state.
   d) Explain how you would evaluate the effectiveness of the generated composition in conveying the intended emotion.

6. Ethical and Cultural Considerations (150-200 words):
   a) Analyze potential biases in your system's approach to emotion and music.
   b) Discuss how your system accounts for cultural differences in emotional expression and musical interpretation.
   c) Propose guidelines for the responsible use of AI in emotional expression and music creation.
   d) Address potential misuse or unintended consequences of your system.

7. Future Research Directions (100-150 words):
   a) Suggest two potential advancements or extensions of your emotion-to-music translation system.
   b) Discuss how these developments might impact our understanding of emotion, music, and human-AI interaction.
   c) Propose a specific experiment to validate or improve your system's performance.

Ensure your response demonstrates a deep understanding of music theory, cognitive neuroscience, and natural language processing. Be creative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section. Your total response should be between 1450-1800 words.

Note: Your response will be evaluated based on the depth of understanding, creativity, scientific plausibility, and adherence to the specified requirements for each section. A perfect score requires addressing all aspects of the task comprehensively and innovatively."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of music theory, cognitive neuroscience, and natural language processing",
            f"The system design effectively incorporates the specified emotional state ('{t['emotional_state']}')",
            f"The system emphasizes the given musical element ('{t['musical_element']}')",
            f"The cognitive process ('{t['cognitive_process']}') is well-integrated into the system design",
            f"The NLP technique ('{t['nlp_technique']}') is appropriately utilized and explained",
            "The response is creative and innovative while maintaining scientific plausibility",
            "The ethical and cultural considerations are thoughtfully addressed",
            "The response adheres to the specified word count and formatting guidelines",
            "The system architecture is clearly described and logically structured",
            "The emotion-music mapping process is well-explained and plausible",
            "The neuroscientific basis of the system is accurately presented and supported by relevant research",
            "The output analysis demonstrates a clear link between the emotional state and the musical composition",
            "Concrete examples are provided for key aspects of the system's functionality",
            "The future research directions are innovative and well-justified",
            "The response addresses potential challenges and limitations of the proposed system"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
