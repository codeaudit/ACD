import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_principles = [
            "Superposition",
            "Entanglement",
            "Quantum Interference"
        ]
        musical_elements = [
            "Harmony",
            "Rhythm",
            "Melody"
        ]
        musical_genres = [
            "Jazz",
            "Classical",
            "Electronic Dance Music (EDM)"
        ]
        tasks = {
            "1": {
                "quantum_principle": random.choice(quantum_principles),
                "musical_element": random.choice(musical_elements),
                "musical_genre": random.choice(musical_genres)
            },
            "2": {
                "quantum_principle": random.choice(quantum_principles),
                "musical_element": random.choice(musical_elements),
                "musical_genre": random.choice(musical_genres)
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        quantum_explanations = {
            "Superposition": "the ability of a quantum system to exist in multiple states simultaneously",
            "Entanglement": "a quantum phenomenon where particles become correlated and share properties regardless of distance",
            "Quantum Interference": "the interaction of quantum waves leading to constructive or destructive effects"
        }
        musical_explanations = {
            "Harmony": "the combination of simultaneous musical notes to produce chords and chord progressions",
            "Rhythm": "the pattern of regular or irregular pulses in music",
            "Melody": "a sequence of musical notes that form a recognizable tune"
        }
        return f"""Design a quantum-inspired cognitive model for musical composition that integrates the quantum computing principle of {t['quantum_principle']} ({quantum_explanations[t['quantum_principle']]}) with the musical element of {t['musical_element']} ({musical_explanations[t['musical_element']]}). Apply your model to generate music in the {t['musical_genre']} genre. Your response should include the following sections:

1. Conceptual Framework (250-300 words):
   a) Explain the chosen quantum principle and its relevance to cognitive processes.
   b) Describe how this principle could be applied to musical composition, focusing on the specified musical element.
   c) Discuss potential cognitive mechanisms that could link quantum-like processes to creative musical thinking.

2. Model Architecture (300-350 words):
   a) Outline the key components of your quantum-inspired cognitive model for musical composition.
   b) Explain how these components interact to generate musical ideas or structures.
   c) Describe how your model incorporates the specified quantum principle and musical element.
   d) Propose a novel feature that enhances the model's creative capabilities.
   e) Include a simple diagram or pseudocode snippet illustrating a key aspect of your model.

3. Composition Process (200-250 words):
   a) Detail how your model would approach the process of musical composition in the specified genre.
   b) Provide a specific example of how it might generate or manipulate a musical idea using the specified quantum principle and musical element.
   c) Discuss how your model might handle challenges specific to the chosen musical element and genre.

4. Musical Example (100-150 words):
   Describe a short musical passage or structure that your model might generate, explicitly showing how it incorporates the quantum principle, musical element, and genre characteristics.

5. Comparison with Classical Approaches (150-200 words):
   Compare and contrast your quantum-inspired model with a classical computational approach to musical composition in the specified genre. Highlight the potential advantages and limitations of each approach.

6. Evaluation and Validation (200-250 words):
   a) Propose methods to evaluate the creativity and musical quality of compositions generated by your model.
   b) Discuss potential benchmarks or comparisons with existing AI composition systems.
   c) Analyze potential biases or limitations in your approach.

7. Cognitive and Musical Implications (150-200 words):
   a) Discuss how your model might contribute to our understanding of human musical creativity.
   b) Explore potential applications of your system in music education or therapy.
   c) Propose a research question that could be investigated using your model.

8. Ethical Considerations (100-150 words):
   a) Identify potential ethical issues related to using quantum-inspired AI for creative tasks in music.
   b) Propose guidelines for responsible development and use of such systems in the music industry.

Ensure your response demonstrates a deep understanding of quantum computing principles, cognitive science, music theory, and the specified genre. Be creative in your model design while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations where necessary.

Format your response with clear headings for each section, numbered exactly as above. Begin each section with the heading (e.g., '1. Conceptual Framework:') followed by your response for that section. Adhere strictly to the word limits provided for each section.

Your total response should be between 1450-1850 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response must integrate the specified quantum principle and musical element in a coherent model",
            "The model design should be innovative yet scientifically plausible",
            "The composition process should clearly demonstrate the application of the quantum-inspired approach to the specified genre",
            "The response should include a concrete musical example that incorporates the quantum principle, musical element, and genre characteristics",
            "The response should provide a meaningful comparison between the quantum-inspired approach and classical computational approaches",
            "The response should show a deep understanding of quantum computing, cognitive science, music theory, and the specified genre",
            "The ethical considerations should be thoughtful and relevant to the proposed system and its application in the music industry",
            "The response should adhere to the specified format and word count range (1450-1850 words)"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0