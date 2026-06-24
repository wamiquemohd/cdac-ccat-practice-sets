# CDAC C-CAT Mock Test

A free, browser-based mock exam for the **CDAC C-CAT 2026** entrance test — built as a single static HTML file, hosted on GitHub Pages, no login or backend required.

🔗 **Live Site:** [wamiquemohd.github.io/CCAT_Mock_Test_with_Claude](https://wamiquemohd.github.io/CCAT_Mock_Test_with_Claude/)

*Prepared by **Mohd Wamique (ex-CDACian)***

---

## About CDAC & C-CAT

**C-DAC (Centre for Development of Advanced Computing)** is a premier R&D organisation under India's Ministry of Electronics and Information Technology (MeitY). It is known for developing India's supercomputing infrastructure and running some of the country's top postgraduate programmes in computing and technology.

The **C-CAT (C-DAC Common Admission Test)** is a national-level entrance examination conducted by C-DAC for admission to its PG Diploma / PG Certificate programmes such as:

- **PG-DITISS** — IT Infrastructure Systems & Security
- **PG-DAC** — Advanced Computing
- **PG-DBDA** — Big Data Analytics
- **PG-DESD** — Embedded Systems Design
- **PG-DVLSI** — VLSI Design
- **PG-DIoT** — Internet of Things

The exam consists of **multiple-choice questions** with **+3 / −1 marking** and is divided into sections:

| Section | Topics | Duration |
|---------|--------|----------|
| **Section A** | English, Quantitative Aptitude, Reasoning | 1 Hour |
| **Section B** | C Programming, Data Structures, OOP (C++), OS & Networking, Big Data & AI Basics | 1 Hour |
| **Section C** | Digital Electronics, Microprocessors (8085/8086), Embedded Systems *(PG-DESD/DVLSI/DIoT only)* | 1 Hour |

---

## Practice Sets

| Set | Level | Sections | Questions | Duration |
|-----|-------|----------|-----------|----------|
| **Practice Set 1** | Normal | A + B | 100 | 2 Hours |
| **Practice Set 2** | Advanced | A + B | 100 | 2 Hours |
| **Practice Set 3** | Advanced + Section C | A + B + C | 150 | 3 Hours |
| **Practice Set 4** | Advanced (Original Sample Paper) | A + B | 100 | 2 Hours |

**What's included:**
- Reading Comprehension passages in all sets (Cloud Computing, Neural Networks, AI Ethics)
- Big Data & AI Basics questions in every Section B (Hadoop, MapReduce, Spark, ML concepts)
- Section C (Set 3) covers: Digital Electronics, 8085/8086 Microprocessors, Embedded C, RTOS, ARM Architecture, Serial Interfaces (I2C/SPI/UART/CAN), IoT Basics
- **+3 / −1 marking** throughout

---

## Features

- **Set selector** on the home screen — choose your practice set before starting
- **Timed sections** — each section has its own 60-minute countdown timer
- **Question palette** — colour-coded (Not Visited / Not Answered / Answered / Marked for Review)
- **Section transitions** — confirms before moving to the next section
- **Nickname entry** — personalises the exam and result
- **Auto-submit** — exam submits automatically when the timer runs out
- **Results page** — score, section breakdown, time spent, and full solutions with explanations
- **PDF export** — save results as a printable PDF
- **Admin snapshot** — results are submitted to admin via Formspree (includes practice set name)
- **Answer key protection** — XOR + Base64 encoded; DevTools detection during exam

---

## How to Use

1. Open the [live link](https://wamiquemohd.github.io/CCAT_Mock_Test_with_Claude/)
2. Select a Practice Set from the home screen
3. Enter your nickname and agree to data sharing
4. Complete Section A → Section B (→ Section C for Set 3)
5. Review your results and download as PDF

No installation, no login, no ads — works entirely in your browser.

---

## Tech Stack

- Pure **HTML / CSS / JavaScript** — single file, no frameworks
- Hosted on **GitHub Pages**
- Results submitted via **Formspree**
- Questions generated and encoded via a **Python script** (`generate.py`)

---

## Repository Structure

```
├── index.html       # The complete exam (all sets, all logic)
├── generate.py      # Python script to rebuild index.html with updated questions
└── README.md
```

To regenerate `index.html` after editing questions in `generate.py`:

```bash
python3 generate.py
```

---

## Disclaimer

This is an **unofficial** practice resource created for educational purposes. Questions are based on the publicly available C-CAT syllabus and are not sourced from any official C-DAC question papers. Always refer to the [official C-DAC website](https://www.cdac.in) for the latest syllabus and exam dates.
