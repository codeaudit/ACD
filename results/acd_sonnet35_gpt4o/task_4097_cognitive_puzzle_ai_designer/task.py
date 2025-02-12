import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_theories = [
            {
                "name": "Dual Process Theory",
                "description": "Distinguishes between fast, automatic, and unconscious (System 1) and slow, effortful, and conscious (System 2) thinking."
            },
            {
                "name": "Working Memory Model",
                "description": "Proposes a multi-component system for temporary storage and manipulation of information."
            },
            {
                "name": "Cognitive Load Theory",
                "description": "Focuses on the role of working memory in learning and problem-solving."
            },
            {
                "name": "Gestalt Principles",
                "description": "Emphasizes how the mind forms a global whole with self-organizing tendencies."
            },
            {
                "name": "Connectionist Theory",
                "description": "Models cognitive processes as interconnected networks of simple units."
            }
        ]
        modalities = ["visual", "auditory", "spatial", "linguistic", "kinesthetic", "emotional"]
        interdisciplinary_fields = ["neuroscience", "psychology", "computer science", "linguistics", "philosophy of mind"]
        time_constraints = ["6 months", "1 year", "18 months"]
        return {
            str(i+1): {
                "theory": random.choice(cognitive_theories),
                "modalities": random.sample(modalities, 3),
                "difficulty": random.choice(["advanced", "expert"]),
                "interdisciplinary_field": random.choice(interdisciplinary_fields),
                "time_constraint": random.choice(time_constraints)
            } for i in range(2)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that can generate and solve complex, multi-modal puzzles based on {t['theory']['name']} and incorporating {', '.join(t['modalities'])} elements at an {t['difficulty']} level. Additionally, integrate insights from {t['interdisciplinary_field']} into your system design. Your system must be developed and operational within {t['time_constraint']}. Your response should include:

1. System Architecture (250-300 words):
   a) Describe the key components of your AI puzzle generation and solving system.
   b) Explain how your system incorporates {t['theory']['name']} in its design and functioning.
   c) Detail how your system integrates {', '.join(t['modalities'])} modalities in puzzle creation and solution.
   d) Discuss how your system adapts to generate puzzles at the {t['difficulty']} difficulty level.
   e) Explain how insights from {t['interdisciplinary_field']} are incorporated into your system's design.
   f) Outline how you would prioritize development tasks to meet the {t['time_constraint']} deadline.

2. Puzzle Generation Process (200-250 words):
   a) Explain the steps your AI system takes to generate a puzzle based on the given cognitive theory.
   b) Describe how it ensures the puzzle incorporates the specified modalities.
   c) Discuss how your system varies puzzle difficulty and complexity to match the {t['difficulty']} level.
   d) Provide an example of a constraint or rule your system might use to ensure puzzle coherence.
   e) Explain how {t['interdisciplinary_field']} influences the puzzle generation process.
   f) Discuss any trade-offs made in the generation process to meet the time constraint.

3. Puzzle-Solving Algorithm (200-250 words):
   a) Detail the approach your AI uses to solve the puzzles it generates.
   b) Explain how this approach reflects or utilizes {t['theory']['name']}.
   c) Discuss how your system handles the multi-modal nature of the puzzles during the solving process.
   d) Describe any optimization techniques used to improve solving efficiency.
   e) Explain how insights from {t['interdisciplinary_field']} contribute to the solving algorithm.
   f) Analyze how the time constraint influences the choice of algorithms and optimization strategies.

4. Example Puzzle (150-200 words):
   a) Provide a detailed description of a sample {t['difficulty']}-level puzzle generated by your system.
   b) Explain how this puzzle incorporates {t['theory']['name']}, the specified modalities, and insights from {t['interdisciplinary_field']}.
   c) Outline the solution process for this puzzle, highlighting key steps and decisions.
   d) Discuss how this puzzle exemplifies the capabilities of a system developed within the given time constraint.

5. Performance Analysis (200-250 words):
   a) Propose metrics to evaluate your system's performance in puzzle generation and solving.
   b) Discuss potential strengths and limitations of your approach.
   c) Compare your system's expected performance to human problem-solving capabilities at the {t['difficulty']} level.
   d) Suggest how the system's performance might vary across different cognitive theories and modalities.
   e) Analyze how the integration of {t['interdisciplinary_field']} affects the system's performance.
   f) Evaluate the impact of the {t['time_constraint']} development timeline on the system's overall performance.

6. Critical Analysis of Limitations (150-200 words):
   a) Identify and analyze at least three significant limitations or potential failure modes of your AI system.
   b) Discuss how these limitations might impact the system's effectiveness or reliability.
   c) Propose potential solutions or areas for future research to address these limitations.
   d) Consider how these limitations might relate to broader challenges in artificial general intelligence.
   e) Analyze how the time constraint may have contributed to or exacerbated these limitations.

7. Implications for AGI and Ethics (150-200 words):
   a) Analyze how your system's abilities might contribute to the development of artificial general intelligence.
   b) Discuss any insights about human cognition that might be gained from your system.
   c) Consider potential ethical implications of an AI system that can generate and solve complex cognitive puzzles.
   d) Propose guidelines for the responsible development and use of such AI systems in research and practical applications.
   e) Reflect on the ethical considerations of rapid AI development under time constraints.

Ensure your response demonstrates a deep understanding of cognitive science, artificial intelligence, and multi-modal reasoning, as well as the chosen interdisciplinary field. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility and considering the real-world time constraint.

Format your response with clear headings for each section. Your total response should be between 1300-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must demonstrate a clear understanding and application of {t['theory']['name']} in the AI system's design and functioning.",
            f"The system should effectively incorporate {', '.join(t['modalities'])} modalities in both puzzle generation and solving processes.",
            f"The proposed AI system should be innovative yet scientifically plausible, with a well-thought-out architecture and algorithms suitable for {t['difficulty']}-level puzzles.",
            f"The response should demonstrate a meaningful integration of insights from {t['interdisciplinary_field']} into the system design and functioning.",
            f"The example puzzle should be complex, multi-modal, clearly reflect the specified cognitive theory, match the {t['difficulty']} level, and incorporate elements from {t['interdisciplinary_field']}.",
            "The performance analysis should be comprehensive and insightful, considering various factors that might affect the system's effectiveness.",
            "The critical analysis of limitations should identify significant challenges and propose thoughtful solutions or areas for future research.",
            "The discussion of implications for AGI and ethics should be nuanced, considering both potential benefits and risks of the technology.",
            f"The response should demonstrate a realistic approach to developing the system within the {t['time_constraint']} constraint, including appropriate trade-offs and prioritization strategies.",
            "The overall response should show a balance between innovation, scientific rigor, and practical considerations of time-constrained AI development."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
