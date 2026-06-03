Smart Attendance System

AI-powered attendance system using real-time face recognition and a RAG chatbot.
Built with Python, OpenCV, DeepFace, Groq LLM, and python-dotenv.



What it does
- Detects and recognizes faces from webcam in real time
- Automatically logs attendance with name, date and time to CSV
- Supports multiple people — just add their photo to known_faces/
- RAG chatbot lets you ask questions about attendance data in natural language


Project Structure
This project was built incrementally — each file represents a learning step:

- webcam.py — step 1: open webcam and display live feed
- recognize.py — step 2: add face recognition against a known photo
- attendance.py — step 3: log verified faces to CSV automatically
- attendance2.py — step 4: scale to multiple people using a folder of photos
- chatbot.py — step 5: RAG chatbot that reads attendance CSV and answers questions

The final working system uses attendance2.py and chatbot.py together.



Technologies Used
- Python 3.12
- OpenCV — webcam capture and frame display
- DeepFace — face verification using VGG-Face neural network
- Groq LLM — natural language chatbot (LLama 3)
- pandas — CSV reading for chatbot context
- python-dotenv — secure API key management



How to run
1. Clone the repo
2. Install dependencies: pip install opencv-python deepface groq pandas python-dotenv
3. Add face photos to known_faces/ folder — name each file after the person (e.g. john.jpg)
4. Create a .env file with your Groq API key: GROQ_API_KEY=your_key_here
5. Run attendance2.py to mark attendance via webcam
6. Run chatbot.py to query attendance records in natural language



What I learned building this
- How face verification works mathematically using neural networks
- How RAG works — retrieving real data and passing it as context to an LLM
- How to manage API keys securely using environment variables
- How to use Git and GitHub for version control
- How each layer of an AI system connects through shared data files
