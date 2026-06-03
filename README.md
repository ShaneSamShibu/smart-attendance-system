Smart Attendance System

AI-powered attendance system using face recognition and a RAG chatbot.

What it does
- Detects and recognizes faces from webcam in real time
- Automatically logs attendance with name, date and time to CSV
- RAG chatbot lets you ask questions about attendance data in natural language

Technologies Used
- Python
- OpenCV
- DeepFace
- Groq LLM
- python-dotenv

How to run
1. Add known face photos to the known_faces/ folder
2. Create a .env file with your GROQ_API_KEY
3. Run attendance2.py to mark attendance
4. Run chatbot.py to query attendance data
