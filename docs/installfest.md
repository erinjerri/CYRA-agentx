# Installfest Instructions
```bash
ssh ubuntu@<LAMBDA_LABS_IP>
mkdir agentx-visionpro && cd agentx-visionpro
python3 -m venv venv && source venv/bin/activate
pip install flask openai python-dotenv
export FLASK_APP=app.py
flask run --host=0.0.0.0 --port=5000
```