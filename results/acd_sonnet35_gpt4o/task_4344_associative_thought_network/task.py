class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            "1": {
                "scenario": "Solving a complex environmental issue: reducing plastic waste in oceans",
                "domain": "Environmental Science",
                "required_associations": ["marine biology", "polymer chemistry", "behavioral economics"],
                "time_limit": 60
            },
            "2": {
                "scenario": "Developing a new form of non-verbal communication for space exploration",
                "domain": "Astrobiology and Linguistics",
                "required_associations": ["quantum entanglement", "bioluminescence", "dance theory"],
                "time_limit": 60
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""You have {t['time_limit']} minutes to complete this task. Design an AI system that mimics human associative thinking to generate and process information in non-linear ways, then apply it to the following creative problem-solving scenario: {t['scenario']}. Your system should be inspired by cognitive models of human associative memory and thinking. Your response should include the following sections:

1. Associative Thought Network Architecture (250-300 words):
   a) Describe the key components of your AI system, explaining how they mimic human associative thinking.
   b) Detail how your system represents and connects concepts, ideas, and information.
   c) Explain how your system generates new associations and ideas.
   d) Discuss any novel techniques or approaches used in your design to enable non-linear information processing.
   e) Provide a high-level diagram or flowchart of your system (describe it textually).

2. Cognitive Science Foundation (150-200 words):
   a) Explain which cognitive theories or models of human associative thinking inspired your system.
   b) Discuss how your system incorporates key features of human associative memory and thinking.
   c) Address any significant differences between your AI system and human cognition.

3. Information Processing Mechanism (200-250 words):
   a) Describe how your system processes input information related to the given scenario.
   b) Explain the mechanisms for generating new associations and ideas.
   c) Detail how your system evaluates and selects the most relevant or promising associations.
   d) Discuss how your system handles conflicting or contradictory information.

4. Application to the Scenario (250-300 words):
   a) Apply your AI system to the given scenario, walking through each step of the problem-solving process.
   b) Explain how the system generates and evaluates potential solutions using associative thinking.
   c) Provide at least three unique or creative ideas generated by your system for addressing the scenario.
   d) Discuss how these ideas leverage cross-domain knowledge and unexpected associations.
   e) Demonstrate how your system incorporates the required associations: {', '.join(t['required_associations'])}.

5. Comparative Analysis (150-200 words):
   a) Compare your associative AI system's approach to traditional linear problem-solving methods.
   b) Discuss potential advantages and disadvantages of your system for creative problem-solving.
   c) Analyze how your system might perform differently from current AI models in addressing the given scenario.
   d) Provide a specific example of how your system might generate a solution that a traditional AI approach would likely miss.

6. Ethical Considerations and Limitations (100-150 words):
   a) Discuss potential ethical issues related to AI systems that mimic human cognitive processes.
   b) Address limitations of your approach and areas for future research or improvement.
   c) Propose guidelines for responsible development and use of associative AI systems.

7. Self-Evaluation (100-150 words):
   a) Assess the strengths and weaknesses of your proposed system and its application to the given scenario.
   b) Identify any areas where you believe your system may have fallen short or could be improved.
   c) Discuss how well you think your system would perform if implemented in a real-world setting.

Ensure your response demonstrates a deep understanding of cognitive science, artificial intelligence, and the {t['domain']} relevant to the scenario. Use appropriate terminology and provide clear explanations where necessary. Be creative and innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1200-1550 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of cognitive science, artificial intelligence, and the relevant domain.",
            "The proposed AI system effectively mimics human associative thinking and incorporates key features of associative memory.",
            "The application to the given scenario is thorough, creative, and generates unique ideas for addressing the problem.",
            "The response successfully incorporates all required associations in a meaningful way.",
            "The comparative analysis provides a clear example of how the associative AI system might outperform traditional approaches.",
            "The ethical considerations and limitations are thoughtfully addressed.",
            "The self-evaluation demonstrates critical thinking about the proposed system's strengths and weaknesses.",
            "The response is well-structured, comprehensive, and adheres to the word count guidelines for each section."
        ]
        score = sum([0.125 if eval_with_llm_judge(instructions, submission, [criterion]) else 0 for criterion in criteria])
        return score
