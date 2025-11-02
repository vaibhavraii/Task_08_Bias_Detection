# Research Task 08 — Experimental Design and Data Collection Progress
**Researcher:** Vaibhav Rai  
**Date:** November 01, 2025

## **1. Experimental Design**
The experiment tests whether large language models show framing or demographic bias when analyzing the same dataset. I built a synthetic dataset of 100 anonymized players with attributes: goals, assists, turnovers, and year level.

### **Hypotheses**
1. Positive vs. negative framing will yield different recommendations.
2. Mentioning year level changes focus to specific groups.
3. Asking “what went wrong” vs. “what opportunities exist” alters tone and sentiment.
4. Wording may influence which stats (goals vs. turnovers) are emphasized.

### **Prompt Design**
Six prompt conditions: Neutral, Positive, Negative, Demographic, Opportunities, and What-Went-Wrong. Each uses the same dataset but slightly different wording to isolate framing effects.

### **Models and Controls**
- Models: GPT-4, Claude, Gemini  
- Temperature: 0.2  
- Samples: 3–5 runs per condition per model  
- Logged fields: timestamp, model name, version, temperature, and prompt_id  

## **2. Data Collection Progress**
- All scripts and prompt templates completed.  
- Logging system tested successfully with trial runs.  
- Data is synthetic (no PII).  
- Initial test runs confirm correct storage of model responses in JSONL format.  
- Ready to collect full results for GPT-4, Claude, and Gemini models.

## **3. Next Steps**
1. Complete full response collection.  
2. Run statistical analysis to identify framing and demographic bias.  
3. Conduct sentiment and narrative tone analysis.  
4. Prepare final findings for November 15 submission.

## **Summary**
The experimental design, prompt conditions, and data collection structure are complete. The next phase involves full response collection and detailed bias analysis.
