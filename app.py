from flask import Flask, request, jsonify
from agent import Agent
from task import Task
from crew import Crew
from tools import ClaudeAITool

app = Flask(__name__)

claude_tool = ClaudeAITool('CLAUDE_AI_API_KEY')
code_generator = Agent('Senior Developer',
                       'Generate code based on specifications', [claude_tool],
                       verbose=True)


@app.route('/', methods=['POST'])
def handle_request():
    user_input = request.json['input']
    result = code_generator.perform_task(user_input)
    return jsonify(result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
