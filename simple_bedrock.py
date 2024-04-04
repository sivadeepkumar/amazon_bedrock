from flask import Flask, render_template, request
from bedrock_kb_agent import BedrockKBAgent

app = Flask(__name__)
kb = BedrockKBAgent()


@app.route('/bedrock', methods=['POST'])
def bedrock_tech():
    data = request.get_json()
    query = data.get('query')
    kb_id = ""
    response = kb.retrieve_from_kb(kb_id, query)
    return response['retrievalResults'][0]['content']

if __name__ == '__main__':
    app.run(debug=True)

