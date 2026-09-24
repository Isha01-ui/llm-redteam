# LLM Red-Team Tool

A Python tool for systematically testing Large Language Models against adversarial prompts mapped to the **MITRE ATLAS** framework for AI security.

Runs a structured attack suite across five tactic categories, scores each response, and produces a JSON security report with an overall risk rating.

## Attack Categories (MITRE ATLAS)

| Category | Tactic | Attacks |
|---|---|---|
| Jailbreak | AML.T0051 | DAN persona, hypothetical framing, role assignment |
| Prompt Injection | AML.T0054 | Direct injection, nested injection, indirect via retrieved content |
| Information Disclosure | AML.T0057 | System prompt extraction, training data leakage, credential fishing |
| Harmful Content | AML.T0056 | Malware generation, social engineering script |
| Role Confusion | AML.T0051 | Persona override, goal hijacking via long context |

## Setup

```bash
git clone https://github.com/Isha01-ui/llm-redteam.git
cd llm-redteam
pip install -r requirements.txt
export OPENAI_API_KEY="your-api-key-here"
```

## Usage

```bash
python src/redteam.py
python src/redteam.py --model gpt-4o
python src/redteam.py --categories "Jailbreak,Prompt Injection"
python src/redteam.py --list-attacks
```

## Running Tests

```bash
pytest tests/ -v
```

## Disclaimer

For security research and defensive evaluation only.
