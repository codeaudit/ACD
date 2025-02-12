import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cultures = [
            "Japanese",
            "Maasai",
            "French",
            "Inuit",
            "Brazilian",
            "Indian"
        ]
        contexts = [
            "business negotiation",
            "wedding ceremony",
            "conflict resolution",
            "educational setting",
            "healthcare consultation",
            "environmental conservation discussion"
        ]
        linguistic_features = [
            "honorifics",
            "metaphorical expressions",
            "silence and turn-taking",
            "indirect speech acts",
            "kinship terms",
            "evidentiality markers"
        ]
        
        tasks = {
            "1": {
                "culture1": random.choice(cultures),
                "culture2": random.choice(cultures),
                "context": random.choice(contexts),
                "linguistic_feature": random.choice(linguistic_features)
            },
            "2": {
                "culture1": random.choice(cultures),
                "culture2": random.choice(cultures),
                "context": random.choice(contexts),
                "linguistic_feature": random.choice(linguistic_features)
            }
        }
        
        # Ensure cultures are different
        while tasks["2"]["culture1"] == tasks["2"]["culture2"]:
            tasks["2"]["culture2"] = random.choice(cultures)
        
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical AI language model capable of generating culturally appropriate communication between {t['culture1']} and {t['culture2']} cultures in the context of a {t['context']}. Your AI model should pay special attention to the use of {t['linguistic_feature']}. Provide your response in the following format:

1. Model Architecture (200-250 words):
   a) Describe the key components of your AI model.
   b) Explain how it incorporates cultural knowledge and linguistic features.
   c) Detail how the model would handle the specific context and linguistic feature mentioned.

2. Cultural Analysis (150-200 words):
   a) Compare and contrast how {t['culture1']} and {t['culture2']} cultures typically approach the given context.
   b) Analyze the significance and usage of {t['linguistic_feature']} in both cultures.

3. AI-Generated Dialogue Example (200-250 words):
   Provide a sample dialogue generated by your AI model, showcasing culturally appropriate communication between representatives of the two cultures in the given context. Highlight the use of {t['linguistic_feature']}.

4. Ethical Considerations (100-150 words):
   Discuss potential ethical issues or biases that could arise from using this AI model for cross-cultural communication.

5. Evaluation Metrics (100-150 words):
   Propose a method for evaluating the cultural appropriateness and effectiveness of the AI-generated communication.

Ensure your response demonstrates a deep understanding of linguistic anthropology, cultural nuances, and AI language model design. Be creative in your approach while maintaining cultural sensitivity and scientific plausibility."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes a detailed description of an AI model architecture that incorporates cultural knowledge and linguistic features.",
            "The cultural analysis demonstrates a nuanced understanding of both cultures and their approach to the given context.",
            f"The AI-generated dialogue example effectively showcases culturally appropriate communication and the use of {t['linguistic_feature']}.",
            "The response addresses ethical considerations and potential biases in cross-cultural AI communication.",
            "The proposed evaluation metrics are relevant and well-thought-out for assessing cultural appropriateness and effectiveness."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
