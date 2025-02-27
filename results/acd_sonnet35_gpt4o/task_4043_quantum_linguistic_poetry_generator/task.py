import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_concepts = [
            "Superposition",
            "Entanglement",
            "Quantum tunneling",
            "Wave-particle duality",
            "Quantum decoherence"
        ]
        poetic_forms = [
            "Sonnet",
            "Haiku",
            "Free verse",
            "Villanelle",
            "Concrete poetry"
        ]
        linguistic_features = [
            "Syntax",
            "Semantics",
            "Phonology",
            "Pragmatics",
            "Morphology"
        ]
        return {
            "1": {
                "quantum_concept": random.choice(quantum_concepts),
                "poetic_form": random.choice(poetic_forms),
                "linguistic_feature": random.choice(linguistic_features)
            },
            "2": {
                "quantum_concept": random.choice(quantum_concepts),
                "poetic_form": random.choice(poetic_forms),
                "linguistic_feature": random.choice(linguistic_features)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired AI system that generates poetry by mapping quantum states to linguistic structures and poetic elements. Your system should incorporate the quantum concept of {t['quantum_concept']}, generate poetry in the form of {t['poetic_form']}, and focus on the linguistic feature of {t['linguistic_feature']}. Then, analyze its output and potential impact on creative writing and quantum understanding. Your response should include:

1. Quantum-Linguistic Mapping (250-300 words):
   a) Explain how you map the quantum concept to linguistic and poetic elements.
   b) Describe the mathematical or conceptual framework for this mapping.
   c) Discuss how this mapping captures the essence of both quantum behavior and language structure.

2. AI System Architecture (300-350 words):
   a) Outline the key components of your AI system for quantum-inspired poetry generation.
   b) Explain how your system incorporates quantum computing principles or quantum-inspired algorithms.
   c) Describe how the system processes linguistic input and generates poetic output.
   d) Include a high-level diagram or pseudocode representing your system's architecture.
   e) Explain how your system avoids potential biases or overfitting to specific quantum concepts or poetic forms.

3. Poetry Generation Process (200-250 words):
   a) Detail the steps your AI system takes to generate a poem.
   b) Explain how the quantum concept influences the generation process.
   c) Describe how your system ensures adherence to the specified poetic form and linguistic feature.

4. Sample Output Analysis (200-250 words):
   a) Provide a sample poem generated by your system (exactly 12 lines for consistency).
   b) Analyze how the poem reflects the quantum concept, poetic form, and linguistic feature.
   c) Discuss the artistic merit and scientific accuracy of the generated poem.

5. Implications for Creative Writing (150-200 words):
   a) Explore how your system might influence or transform the field of poetry and creative writing.
   b) Discuss potential benefits and challenges for human poets interacting with such a system.
   c) Consider how this approach might lead to new forms of artistic expression.

6. Quantum Understanding and Education (150-200 words):
   a) Analyze how your system might enhance public understanding of quantum concepts.
   b) Discuss the potential use of quantum-inspired poetry in science education.
   c) Consider limitations or misconceptions that might arise from this approach.

7. Ethical Considerations and Future Directions (150-200 words):
   a) Identify potential ethical concerns related to AI-generated poetry and quantum-inspired art.
   b) Propose guidelines for responsible development and use of such systems.
   c) Suggest two future research directions that could extend or refine your approach.

Ensure your response demonstrates a deep understanding of quantum physics, linguistics, poetics, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative and innovative in your approach while maintaining scientific and artistic plausibility.

Format your response with clear headings for each section. Your total response should be between 1400-1750 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of the quantum concept {t['quantum_concept']}, the poetic form {t['poetic_form']}, and the linguistic feature {t['linguistic_feature']}.",
            "The proposed AI system effectively integrates quantum principles with linguistic and poetic elements.",
            "The system architecture includes measures to avoid biases and overfitting.",
            "The sample poem generated by the system reflects the specified quantum concept, poetic form, and linguistic feature, and is exactly 12 lines long.",
            "The analysis of implications for creative writing and quantum understanding is insightful and well-reasoned.",
            "The response addresses ethical considerations and proposes meaningful future research directions.",
            "The overall approach is innovative, creative, and original while maintaining scientific and artistic plausibility."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
