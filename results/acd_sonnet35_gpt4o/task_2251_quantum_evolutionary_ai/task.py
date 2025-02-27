class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "quantum_effect": "Quantum tunneling",
                "biological_process": "Photosynthesis",
                "optimization_goal": "Increase energy capture efficiency"
            },
            "2": {
                "quantum_effect": "Quantum entanglement",
                "biological_process": "Enzyme catalysis",
                "optimization_goal": "Enhance reaction speed and specificity"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""The field of quantum biology explores how quantum mechanical phenomena might play a role in biological processes. Your task is to design an AI system that simulates quantum effects in biological systems and uses quantum-inspired evolutionary algorithms to optimize these processes. This challenge will test your ability to integrate concepts from quantum mechanics, biology, evolutionary algorithms, and artificial intelligence.

Focus on the quantum effect of {t['quantum_effect']} in the biological process of {t['biological_process']}, with the goal of {t['optimization_goal']}. Your response should include:

1. Quantum-Biological Model (300-350 words):
   a) Explain the role of {t['quantum_effect']} in {t['biological_process']}.
   b) Describe how you would model this quantum effect computationally, including specific equations or algorithms.
   c) Discuss the challenges in simulating quantum effects at the biological scale.
   d) Propose a novel approach to overcome one of these challenges.

2. Quantum-Inspired Evolutionary Algorithm (300-350 words):
   a) Design an evolutionary algorithm that incorporates quantum principles, detailing the representation of individuals and genetic operators.
   b) Explain how your algorithm represents and manipulates quantum states, including the mathematical formalism used.
   c) Describe the fitness function for {t['optimization_goal']}, providing a specific mathematical formulation.
   d) Discuss how your algorithm balances exploration and exploitation, giving concrete examples.

3. AI System Architecture (250-300 words):
   a) Describe the overall structure of your AI system, including a block diagram or pseudocode.
   b) Explain how the quantum-biological model and evolutionary algorithm interact within the system.
   c) Discuss any machine learning components in your system, specifying the type of ML algorithms used and their role.
   d) Propose a method for validating the system's outputs, including specific metrics and validation techniques.

4. Simulation and Analysis (200-250 words):
   a) Describe how you would implement and run a simulation of your system, including the software tools or frameworks you would use.
   b) Explain the key parameters and variables you would measure, providing specific examples and units of measurement.
   c) Propose a method to visualize the quantum states and evolutionary progress, describing the type of plots or visualizations you would create.
   d) Discuss how you would analyze the results to evaluate the system's performance, including statistical methods or benchmarks you would use.

5. Potential Applications and Implications (200-250 words):
   a) Suggest at least two potential applications of your system in biology or medicine, explaining how they would work in practice.
   b) Discuss how this approach might advance our understanding of quantum biology, providing specific examples of research questions it could address.
   c) Analyze potential ethical implications of optimizing biological processes, considering both positive and negative consequences.
   d) Propose at least three specific guidelines for responsible development and use of such technology.

6. Future Research Directions (150-200 words):
   a) Suggest two potential extensions or improvements to your system, explaining how they would be implemented.
   b) Discuss how these extensions could address current limitations, providing concrete examples.
   c) Propose an experiment to test a hypothesis generated by your system, including the experimental design and expected outcomes.

Ensure your response demonstrates a deep understanding of quantum mechanics, biology, evolutionary algorithms, and AI. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Begin each section with the heading on a new line, followed by your response for that section. Your total response should be between 1400-1700 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of {t['quantum_effect']} and its role in {t['biological_process']}, including specific equations or algorithms for modeling.",
            "The quantum-inspired evolutionary algorithm is well-designed, with clear explanations of individual representation, genetic operators, and quantum state manipulation.",
            "The AI system architecture is coherent and includes a block diagram or pseudocode, clearly showing how components interact.",
            "The simulation and analysis approach is well-thought-out, with specific software tools, parameters, and visualization methods mentioned.",
            "The discussion of potential applications and ethical implications is insightful, comprehensive, and includes at least two specific applications and three guidelines.",
            "The proposed future research directions are innovative, address relevant limitations, and include a well-designed experiment.",
            "The response is creative and original while maintaining scientific plausibility and rigor.",
            "The writing is clear, well-organized, and adheres to the specified format and word count guidelines.",
            "The response includes specific mathematical formulations, equations, or algorithms where appropriate."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
