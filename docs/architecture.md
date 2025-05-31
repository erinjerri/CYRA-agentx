```mermaid
graph TD
    AVP[Apple Vision Pro App] -->|Screenshot + Audio| FlaskAPI[Flask Server (analyze)]
    FlaskAPI -->|Transcribe| Whisper[OpenAI Whisper API]
    FlaskAPI -->|Screenshot + Transcript| GPT4o[OpenAI GPT-4o]
    GPT4o -->|JSON Response| FlaskAPI
    FlaskAPI -->|Parsed JSON| VisionUI[Render UI in AVP app]
    GPT4o -->|Logs| LangGraph[LangGraph Agent Logs]
    subgraph Local JSON Logs
        FlaskAPI --> TaskLog
    end
```