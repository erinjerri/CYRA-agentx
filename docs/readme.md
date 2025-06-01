# Create Your Reality Agent (CYRA) App 

* Initial prototype with OpenAI. Later version with OpenAI Operator. 
* Built for UC Berkeley LLM Agents (Advanced) course, after a hackathon last year (VisionDevCamp winning Best Productivity app for app concept) and undergoing Women in Big Data solopreneurship program.
* This project actually tries to build a real prototype with real data.
* This project is a quick MVP for computer use agents and using Lambda.
* Future Directions
* We will attempt to use iOS with simulator storing task created by user speech input, converted to text (JSON for web app, native iOS eventual macOS and VisionOS app UI with storable text that is saved in Apple Private Cloud via CloudKit). This is then integrated with Instacart to test out performance abilities using Playwright to see if an AI agent is able to handle storing a log of a task, completing a task and switching to another web application.

# CYRA Agent Tree

CYRA-agentx/
├── .env                    # Environment variables (e.g., OPENAI_API_KEY)
├── app.py                 # Main Flask app entry point
├── agents/
│   ├── __init__.py         # Initializes LLM and tools
│   └── reasoning.py        # LangChain agent logic (initialize_agent or LLMChain)
├── tools/
│   ├── __init__.py         # Placeholder for tool loading logic
│   └── whisper.py          # Whisper transcription placeholder (e.g., mock or API call)
├── static/
│   └── uploads/            # Where uploaded screenshots or audio will be saved (if needed)
├── requirements.txt        # Python dependencies to install
├── README.md               # High-level overview + usage
├── INSTALL.md              # Installfest guide (step-by-step setup)
├── MVP_CHECKLIST.md        # Features for MVP vs stretch goals
├── architecture.md         # Mermaid system design diagram
└── .gitignore              # Prevents secrets or build files from being committed
mobile-app
├──AppDelegate.swift
├──AudioRecorder.swift
├──NetworkManager.swift
├──ViewController.swift 

# Installfest Instructions
```bash
ssh ubuntu@<LAMBDA_LABS_IP>
mkdir agentx-visionpro && cd agentx-visionpro
python3 -m venv venv && source venv/bin/activate
pip install flask openai python-dotenv
export FLASK_APP=app.py
flask run --host=0.0.0.0 --port=5000
```

# Checklist
- [x] POST data to Flask backend
- [ ] Audio Recorder in Swift (AVFoundation) - Transcribe audio into iOS
- [ ] Screenshot to JPEG SwiftUI
- [ ] Whisper + GPT-4o call with screenshot + audio
- [ ] JSON response rendered in UI
- [ ] TestFlight deployment
- [ ] Vector DB with Chroma

# Stretch Goals
- [ ] Audio Recorder - cross platform - Transcribe audio from user in Apple Vision Pro - VisionOS
- [ ] Handwriting Recognition via MNIST/CoreML upon Apple Office Hours approval 
- [ ] LangGraph tracing
- [ ] Novel 3D Spatial Dataset / Benchmark for tasks emulating WebArena/OSWorld benchmark
