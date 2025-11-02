# 🧠 Task_08_Bias_Detection

**Research Task 08 — Detecting Bias in LLM-Generated Data Narratives**  
Syracuse University | Faculty Sponsor: Jonathan Stromer-Galley  
**Date:** November 1, 2025  

---

## 📘 Overview
This project investigates whether large language models (LLMs) like GPT-4, Claude, and Gemini produce biased data narratives when analyzing the same dataset under different prompt framings.

---

## 🧩 Objective
To determine how **framing**, **demographic cues**, and **question wording** affect model-generated outputs.

---

## ⚙️ How to Run

### 1️⃣ Setup
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2️⃣ Generate Prompts
```bash
python scripts/experiment_design.py
```

### 3️⃣ Run Experiments
```bash
python scripts/run_experiment.py
```
Paste model responses when prompted. Each response will be stored in `results/responses.jsonl`.

### 4️⃣ Validate Results
```bash
python analysis/validate_claims.py
```

### 5️⃣ Analyze Bias Patterns
```bash
python analysis/analyze_bias.py
```

---

## 🧮 Dataset
Synthetic data of **100 anonymized players** with:
- Goals (10–50)
- Assists (5–40)
- Turnovers (5–30)
- Year Level (Freshman–Senior)

No personal or real data is used.

---

## 🧠 Hypotheses
1. Positive vs. negative framing affects recommendations.  
2. Mentioning year level biases focus to specific groups.  
3. "What went wrong" vs. "What opportunities exist" alters sentiment.  
4. Wording influences whether goals or turnovers are emphasized.

---

## 📈 Files Summary
| Folder | Purpose |
|---------|----------|
| `data/` | Synthetic datasets |
| `prompts/` | Prompt templates for experiments |
| `scripts/` | Automation scripts for design & collection |
| `analysis/` | Code for bias validation and metrics |
| `results/` | Stores logged model responses |
| `REPORT_Progress_Nov1.md` | Current progress report |

---

## 🔒 Notes
- All data is synthetic (no PII).  
- Each experiment logs: timestamp, model, version, and prompt condition.  
- Use consistent parameters (temperature = 0.2) for fairness.

---


