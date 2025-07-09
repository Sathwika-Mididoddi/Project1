import ollama from 'ollama';

async function askLLM() {
  console.log("Sending request to Ollama...");

  try {
    const response = await ollama.chat({
      model: 'mistral',
      messages: [
        { role: 'user', content: 'What is a black hole?' }
      ]
    });
    console.log("Output");
    console.log("AI response:", response.message.content);
  } catch (err) {
    console.error("❌ Error talking to Ollama:", err.message);
  }
}

askLLM();
