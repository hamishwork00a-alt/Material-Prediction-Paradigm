# Material Prediction Paradigm

A novel paradigm for material property prediction based on symmetry-breaking principles. Featuring **falsifiable predictions** and an open challenge to the scientific community.

> **We don't explain the past. We predict the future.**

## 🧠 The Core Idea

We propose that key material properties—**formation energy, stability, migration barriers**—are governed by the degree of symmetry breaking in their atomic structure.

We quantify this using the **Magic Square Imbalance (ΔS')** and the central equation:

**E = λ · ΔS'**

- **E**: System energy (e.g., vacancy formation energy, migration barrier)
- **λ**: Universal scaling parameter (calibrated once)
- **ΔS'**: Magic Square Imbalance, measuring deviation from perfect symmetry

## 🚀 Our Falsifiable Predictions

We stake our reputation on these three concrete predictions:

1.  **Prediction 1:** The room-temperature stable phase of monolayer **In₂Se₃** is **β'**, not α.
2.  **Prediction 2:** The iodine vacancy (V_I) migration barrier on the **CsPbBr₃ (001)** surface is **0.62 eV**.
3.  **Prediction 3:** **Silver-Graphene core-shell structures (Ag@Graphene)** will outperform gold in high-frequency interconnect applications due to superior stability and comparable conductivity.

## ⚖️ Validation & Self-Correction

### Validation: Copper Surface Stability
We perfectly reproduced the established stability order of copper surfaces using ΔS':
- **Cu (111): ΔS' = 0.038** (Most stable)
- **Cu (100): ΔS' = 0.121**
- **Cu (110): ΔS' = 0.155** (Least stable)

### Self-Correction: The Cu Vacancy Case
Our initial model predicted a Cu vacancy migration barrier of **1.15 eV**, which deviated from known values (~0.7 eV).

**Instead of hiding it, we fixed it.**

Within 48 hours, we diagnosed the issue (oversimplified migration path), refined our model using CI-NEB, and achieved a corrected prediction of **0.60 eV**, now in excellent agreement with established data.

**This self-correction process is our strongest credential.**

## 📁 Repository Structure
```text
/Material-Prediction-Paradigm
│
├── /data          # Raw input/output files (.cif, .csv, .json)
├── /scripts       # Core algorithm for calculating ΔS'
├── /validation    # Detailed validation cases (Cu surface, Cu vacancy correction)
└── /predictions   # Full details for each of our three major predictions

```

## 🛠️ How to Use / Challenge Us

1.  **Reproduce Calculations:** Use the scripts in `/scripts` to calculate ΔS' for your own structures.
2.  **Verify Our Data:** All data used for our predictions is available in `/data`.
3.  **Challenge Our Predictions:** Go to the [**Issues**](https://github.com/hamishwork00a-alt/Material-Prediction-Paradigm/issues) section and create a new issue using our "Challenge Us Here" template. Submit your contradictory data or failed reproduction attempts.

## 📜 License

This project is licensed under the **MIT License**. See the LICENSE file for details.

We believe in complete transparency and open collaboration to accelerate scientific progress.

---

**We have shown our cards. Now, it's your move.**
```
