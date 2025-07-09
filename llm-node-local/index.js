// index.js
import ollama from 'ollama';

async function askLLM() {
  const response = await ollama.chat({
    model: 'mistral',
    messages: [
      { role: 'user', content: 'Explain black holes simply' }
    ]
  });

  console.log("AI response:", response.message.content);
}

askLLM();
console.log("hi");