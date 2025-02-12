import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        domains = [
            "physics",
            "biology",
            "psychology",
            "economics",
            "art"
        ]
        concepts = [
            "entropy",
            "evolution",
            "cognition",
            "equilibrium",
            "symmetry"
        ]
        return {
            "1": {
                "source_domain": random.choice(domains),
                "target_domain": random.choice(domains),
                "concept": random.choice(concepts)
            },
            "2": {
                "source_domain": random.choice(domains),
                "target_domain": random.choice(domains),
                "concept": random.choice(concepts)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of modeling and manipulating multidimensional conceptual spaces, then use it to solve a complex analogical reasoning problem. Your task is to create a detailed proposal for this system and apply it to map the concept of {t['concept']} from the domain of {t['source_domain']} to the domain of {t['target_domain']}.

Provide your response in the following format:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI system for modeling and manipulating conceptual spaces.
   b) Explain how your system represents concepts and their relationships in a multidimensional space.
   c) Detail the mechanisms used for mapping concepts between different domains.
   d) Discuss how your system ensures the generated analogies are both novel and meaningful.
   e) Include a simple ASCII art diagram (max 15 lines) illustrating the key components and their interactions.

2. Conceptual Space Modeling (250-300 words):
   a) Explain how your system models the conceptual space of {t['source_domain']}.
   b) Describe how the concept of {t['concept']} is represented within this space.
   c) Discuss any challenges specific to modeling this particular domain and concept.

3. Cross-Domain Mapping Process (250-300 words):
   a) Outline the step-by-step process your AI system uses to map {t['concept']} from {t['source_domain']} to {t['target_domain']}.
   b) Explain how the system identifies relevant features and relationships to preserve in the mapping.
   c) Describe how these features are transformed or reinterpreted in the target domain.

4. Analogical Reasoning Example (200-250 words):
   a) Present a specific analogy generated by your AI system that maps {t['concept']} from {t['source_domain']} to {t['target_domain']}.
   b) Provide a detailed interpretation of the analogy, explaining how it captures key aspects of the concept.
   c) Discuss how this analogy might enhance understanding of {t['concept']} in the context of {t['target_domain']}.

5. Cognitive Science Insights (200-250 words):
   a) Analyze how your AI's approach to conceptual mapping and analogical reasoning compares to human cognitive processes.
   b) Discuss any insights your system might provide into human conceptual thinking and creativity.
   c) Propose a hypothesis about cross-domain reasoning in humans that could be tested using your AI system.

6. Evaluation and Limitations (150-200 words):
   a) Propose criteria for evaluating the quality and effectiveness of the generated analogies.
   b) Discuss potential limitations of your approach and areas for future improvement.
   c) Consider ethical implications of using AI-generated analogies in scientific or educational contexts.

7. Future Directions and Applications (150-200 words):
   a) Suggest potential extensions or improvements to your system.
   b) Propose novel applications of your conceptual space manipulation system in fields such as scientific discovery, education, or creative problem-solving.

Ensure your response demonstrates a deep understanding of cognitive science, artificial intelligence, and the specific domains involved. Be creative in your system design and analogy generation while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section. Your total response should be between 1500-1850 words. Include a word count at the end of each section.

Cite at least 3 relevant research papers or theories from cognitive science and AI to support your design choices throughout your response."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of cognitive science, artificial intelligence, and the specific domains involved.",
            "The system architecture is well-designed, clearly explained, and includes an appropriate ASCII art diagram.",
            "The conceptual space modeling approach is innovative, plausible, and well-suited to the given domains and concept.",
            "The cross-domain mapping process is logically sound, well-described, and demonstrates a clear understanding of analogical reasoning.",
            "The analogical reasoning example is creative, relevant, and effectively maps the concept between the specified domains.",
            "The cognitive science insights are thoughtful, demonstrate interdisciplinary thinking, and propose a testable hypothesis.",
            "The evaluation criteria and limitations are thoroughly considered and relevant to the proposed system.",
            "The future directions and applications are innovative, well-reasoned, and demonstrate potential real-world impact.",
            "The response uses appropriate technical terminology and provides clear explanations for complex concepts.",
            "The overall proposal is creative while maintaining scientific plausibility.",
            "The response includes at least 3 relevant citations to support design choices.",
            "Each section adheres to the specified word count range."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
