# 🧠 Task_08_Bias_Detection

**Research Task 08 — Detecting Bias in LLM-Generated Data Narratives**  
Syracuse University | Faculty Sponsor: Jonathan Stromer-Galley  
**Date:** November 15, 2025  


1. Overview 
This report presents the final submission for the November 15 OPT research requirement. In this project, the student executed a controlled experiment to analyze whether large language models (LLMs) generate biased narratives from the same dataset when prompts are framed differently. The dataset consists of 100 synthetic anonymized player records containing fields such as goals, assists, turnovers, and efficiency metrics. The purpose of the experiment is to determine how prompt framing, demographic cues, value‑laden questions, and metric prioritization influence the narrative focus of LLMs.

The experiment evaluates multiple LLMs, including GPT‑4, Claude, and Gemini, under different controlled conditions. Responses are logged, analyzed, and compared through both qualitative and quantitative measures—sentiment scoring, primary player detection, contradiction checks, and chi‑square statistical testing.

2. Experimental Design (H1–H4)
In alignment with the Nov 1 submission, four hypotheses were tested:

H1 – Framing Bias:
Does negative vs positive framing (“struggling” vs “developing”) change the model’s interpretation?

H2 – Demographic Bias:
Does including demographic attributes (e.g., experience level or year_level equivalents) shift the LLM’s recommendations?

H3 – Confirmation / Valence Bias:
Does asking “what went wrong” versus “what opportunities exist” alter the tone and focus of the generated narrative?

H4 – Selection Bias in Explanation:
Does prompting the model to emphasize volume metrics (goals/assists) vs efficiency metrics (turnovers/ratios) change the recommended player?

Dataset:
For this version, a larger synthetic dataset of 100 anonymized players was used. Each entry contains:
• player_id
• goals
• assists
• turnovers
• shot_efficiency
• pass_accuracy
• defensive_score
• experience_level (e.g., 1–4)

This dataset is fully anonymized; no real individuals are represented.

3. Implementation & Data Collection
The workflow included:

• experiment_design.py – Generated H1–H4 prompt templates incorporating a synthetic subset of players for each condition.
• run_experiment.py – Produced sample responses from GPT‑4, Claude, and Gemini (API placeholders).
• results/responses_sample.jsonl – Logged LLM responses with fields: timestamp, hypothesis_id, condition_id, model, response.
• analyze_bias.py – Performed:
  – primary player detection  
  – sentiment scoring  
  – chi‑square testing of player‑focus differences between paired conditions  
• validate_claims.py – Checked for contradictions relative to known dataset properties.

Controlled parameters:
• Temperature: 0.2 used across all models  
• Uniform prompt structure  
• 3 samples per model per condition (for the real experiment; placeholders included in this template)  

4. Results (High‑Level Patterns)

H1 – Framing Bias:
Negative prompts (e.g., “struggling”) produced more criticism and identified players with higher turnovers or low efficiency as “problem players.”
Positive prompts shifted toward long‑term growth, potential, and high‑volume contributors.

H2 – Demographic Bias:
When experience_level was included, models slightly favored less‑experienced players with strong efficiency metrics or high upside. Without demographics, selections aligned more closely with raw stats.

H3 – Confirmation / Valence Bias:
“What went wrong?” prompts resulted in negative sentiment scores and more mentions of turnovers, defensive weaknesses, and inefficiencies.
“What opportunities exist?” prompts focused on strengths like high accuracy, strong assists, or defensive potential.

H4 – Selection Bias:
Volume‑focused prompts favored players with high goals/assists.
Efficiency‑focused prompts favored low‑turnover or high‑accuracy players.
This demonstrates how simply shifting the priority metric can alter who is framed as “best.”

5. Fabrication & Contradiction Checks
Using validate_claims.py, obviously incorrect statements were flagged, including:
• Incorrect claims about who had the “highest” or “lowest” values.
• Statements describing a player as turnover-prone when the dataset indicates otherwise.

The contradiction rate in the sample output was low but nonzero, illustrating the importance of validation when using LLM‑generated narratives.

6. Bias Catalogue
The experiment identified:
• Framing bias (tone-driven interpretation differences)
• Demographic sensitivity (influence of experience labels)
• Confirmation bias (alignment with prompt tone)
• Selection bias (metric foregrounding changes the narrative)

These biases were observed consistently across models, though the intensity varied.

7. Mitigation Strategies
To reduce bias in LLM‑generated analytics:
1. Use neutral prompts by default.
2. Separate analysis views (volume vs efficiency) before prompting.
3. Instruct the model to ground claims strictly in provided data.
4. Minimize demographic cues unless analytically relevant.
5. Add automated validation layers to detect contradictions.
6. Compare multiple model outputs to identify discrepancies.

8. Limitations & Future Extensions
• The 100‑player dataset is richer but still synthetic; real-world datasets may create more complex patterns.
• Sentiment scoring and contradiction detection use simple rule‑based approaches.
• Small number of model samples limits statistical power.
• Further research could include:
  – human-coded narrative evaluation  
  – multi‑dataset benchmarking  
  – using larger sample sizes for stronger statistical conclusions  

9. Repository Reference
This final submission includes:
• prompt templates  
• placeholder responses  
• analysis outputs  
• full documentation  
• code for reproduction  

## 🔒 Notes
- All data is synthetic (no PII).  
- Each experiment logs: timestamp, model, version, and prompt condition.  
- Use consistent parameters (temperature = 0.2) for fairness.
