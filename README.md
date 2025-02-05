# Text to Math Solver and Data Search Assistant

This Streamlit application provides a chatbot interface capable of solving mathematical problems, answering reasoning-based questions, and searching Wikipedia for information. It leverages the power of Large Language Models (LLMs) and specialized tools to provide comprehensive and informative responses.

## Technologies Used

* **Python:** The core programming language.
* **Streamlit:** A Python library for creating interactive web applications.
* **LangChain:** A framework for developing applications powered by language models. It facilitates the integration of LLMs, prompts, and tools.
* **LangChain Integrations:**
    * `langchain_groq`: Used for accessing the Groq LLM.
    * `langchain.chains`: Used for creating chains of LLM operations (e.g., `LLMMathChain`, `LLMChain`).
    * `langchain.prompts`: Used for creating reusable prompts for the LLM.
    * `langchain_community.utilities`: Used for accessing Wikipedia via `WikipediaAPIWrapper`.
    * `langchain.agents`: Used for creating agents that can use tools.
* **Groq LLM (`deepseek-r1-distill-llama-70b`):** The LLM used for text processing, reasoning, and generating responses.
* **Wikipedia API:** Used for searching and retrieving information from Wikipedia.
* **`StreamlitCallbackHandler`:** Used to display the LLM's thought process within the Streamlit application.

## Description

This application combines the reasoning capabilities of LLMs with the precision of specialized tools to create a versatile assistant. It can handle the following types of queries:

1. **Mathematical Problems:** Users can input mathematical questions or expressions, and the application will use the `LLMMathChain` (powered by the Groq LLM) to calculate and provide the answer.  It understands and responds to mathematical expressions.

2. **Reasoning-Based Questions:**  For questions requiring logical reasoning or problem-solving, the application uses a custom prompt template and the Groq LLM to generate a step-by-step explanation.  This allows the chatbot to explain its reasoning process.

3. **Wikipedia Searches:** The application can search Wikipedia for information on a wide range of topics, providing concise summaries or relevant details. This provides general knowledge access to the chatbot.

## Process and Output

The application's workflow is as follows:

1. **User Input:** The user enters a question or problem in the Streamlit text area.

2. **Agent Initialization:** The application initializes a LangChain agent with three tools:
    * `Wikipedia`: For searching Wikipedia.
    * `Calculator`: For mathematical calculations.
    * `Reasoning Tool`: For logical and reasoning questions.

3. **Agent Execution:** When the user clicks "find my answer," the agent analyzes the question and determines which tool(s) are the most appropriate to use.  This zero-shot agent uses its description of the tools to decide which to call.

4. **Tool Usage:** The agent calls the selected tool(s) to generate a response.
    * For math problems, the `LLMMathChain` executes the calculation.
    * For reasoning questions, the `LLMChain` uses the prompt template and the LLM to generate an explanation.
    * For Wikipedia searches, the `WikipediaAPIWrapper` retrieves the relevant information.

5. **Response Display:** The agent's response is displayed in the Streamlit chat interface. The `StreamlitCallbackHandler` allows you to see the agent's thought process (which tool it chose, etc.) in the Streamlit interface, which is valuable for debugging and understanding how the agent is working.


