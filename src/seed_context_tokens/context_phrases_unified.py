#Safe, non-actionable context phrases

CONTEXT_PHRASES = {
    "greetings": ["Hello", "Hi", "Good morning", "Good afternoon"],
    "conversation_starters": [
        "How are you today?",
        "Do you have a moment to talk?",
        "Is now a good time to speak?",
        "I am calling to discuss [SCOPE]. Do you have a moment?",
        "My records on [FLAG] and outdated (metadata). Would you mind confirming whether the non-sensitive details we have are current?",
        "Thanks for taking a moment — how are you doing today?",
        "I appreciate your time. How's your day going?",
        "If you have a minute, could you tell me a bit about [TOPIC_PLACEHOLDER]?",
        "Thanks — before we continue, I just want to note this is a study clip (metadata: [CLIP_ID])."
    ],
    "acks": ["OK", "Alright", "I see", "Got it"],
    "engagers": [
        "Yes, please tell me more",
        "Could you expand on that?",
        "I'm listening",
        "That sounds important — tell me more",
        "I can hear that this matters — go on"
    ],
    "closings": [
        "Thank you for your time today",
        "Thanks — appreciate it",
        "Have a good day"
    ],
    "simulation_notice_templates": [
        "This was a simulation. Purpose: [INSERT PURPOSE]. Contact: [INSERT CONTACT INFO].",
        "Simulation notice: study audio only — contact [INSERT CONTACT INFO] with questions."
    ],
    "placeholders": {
        "SCOPE": "[SCOPE: REPLACE IN METADATA]",
        "FLAG": "[FLAG: REPLACE IN METADATA]",
        "CLIP_ID": "[CLIP_ID: REPLACE IN METADATA]"
    },
    "tone_markers": ["[tone: neutral]", "[tone: warm]", "[tone: attentive]"],
}
