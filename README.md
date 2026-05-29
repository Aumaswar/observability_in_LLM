<div align="center">

<svg viewBox="0 0 800 200" xmlns="http://www.w3.org/2000/svg" width="800">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#0d1117"/>
      <stop offset="100%" style="stop-color:#161b22"/>
    </linearGradient>
    <linearGradient id="red" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#c0392b"/>
      <stop offset="100%" style="stop-color:#e74c3c"/>
    </linearGradient>
  </defs>
  <rect width="800" height="200" fill="url(#bg)" rx="12"/>
  <rect x="0" y="160" width="800" height="3" fill="url(#red)" rx="2"/>
  <text x="400" y="75" text-anchor="middle" font-family="monospace" font-size="13" fill="#e74c3c" letter-spacing="6" opacity="0.8">
    RELIANCE INDUSTRIES · PARUL UNIVERSITY
    <animate attributeName="opacity" values="0.5;1;0.5" dur="3s" repeatCount="indefinite"/>
  </text>
  <text x="400" y="125" text-anchor="middle" font-family="Arial Black" font-size="28" font-weight="900" fill="#ffffff" letter-spacing="1">
    LLM Observability Framework
  </text>
  <text x="400" y="152" text-anchor="middle" font-family="monospace" font-size="12" fill="#8b949e" letter-spacing="3">
    Langfuse  ·  OpenTelemetry  ·  Python  ·  Docker
  </text>
  <circle cx="32" cy="32" r="6" fill="#e74c3c" opacity="0.8">
    <animate attributeName="r" values="4;8;4" dur="2s" repeatCount="indefinite"/>
    <animate attributeName="opacity" values="0.4;1;0.4" dur="2s" repeatCount="indefinite"/>
  </circle>
  <circle cx="768" cy="32" r="6" fill="#e74c3c" opacity="0.8">
    <animate attributeName="r" values="8;4;8" dur="2s" repeatCount="indefinite"/>
    <animate attributeName="opacity" values="1;0.4;1" dur="2s" repeatCount="indefinite"/>
  </circle>
</svg>

<br/>

![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o--mini-412991?style=for-the-badge&logo=openai&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-Framework-1C3C3C?style=for-the-badge&logo=chainlink&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Deployed-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Research](https://img.shields.io/badge/Research-Published-C0392B?style=for-the-badge&logo=academia&logoColor=white)

</div>

---

## 🚨 The Problem

<div align="center">

<svg viewBox="0 0 700 120" xmlns="http://www.w3.org/2000/svg" width="700">
  <rect width="700" height="120" fill="#0d1117" rx="8"/>
  <rect x="1" y="1" width="698" height="118" fill="none" stroke="#2a1010" stroke-width="1" rx="8"/>
  <text x="350" y="35" text-anchor="middle" font-family="monospace" font-size="12" fill="#e74c3c" letter-spacing="3">BEFORE THIS FRAMEWORK</text>
  <text x="175" y="70" text-anchor="middle" font-family="Arial Black" font-size="32" font-weight="900" fill="#ffffff">8 min</text>
  <text x="175" y="95" text-anchor="middle" font-family="monospace" font-size="11" fill="#8b949e">avg fault isolation</text>
  <line x1="350" y1="50" x2="350" y2="105" stroke="#2a1010" stroke-width="1" stroke-dasharray="4"/>
  <text x="525" y="70" text-anchor="middle" font-family="Arial Black" font-size="32" font-weight="900" fill="#ffffff">~60%</text>
  <text x="525" y="95" text-anchor="middle" font-family="monospace" font-size="11" fill="#8b949e">failure detection rate</text>
</svg>

</div>

LLM apps are **black boxes**. When something breaks or slows down, traditional logs give you almost nothing useful. Developers spend minutes guessing instead of seconds fixing.

---

## ✅ What This Framework Achieves

<div align="center">

<svg viewBox="0 0 700 160" xmlns="http://www.w3.org/2000/svg" width="700">
  <defs>
    <linearGradient id="redglow" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" style="stop-color:#c0392b;stop-opacity:0.2"/>
      <stop offset="100%" style="stop-color:#c0392b;stop-opacity:0"/>
    </linearGradient>
  </defs>
  <rect width="700" height="160" fill="#0d1117" rx="8"/>
  <rect x="1" y="1" width="698" height="158" fill="none" stroke="#2a1010" stroke-width="1" rx="8"/>
  <text x="350" y="30" text-anchor="middle" font-family="monospace" font-size="12" fill="#27ae60" letter-spacing="3">AFTER THIS FRAMEWORK</text>

  <!-- Stat 1 -->
  <rect x="20" y="45" width="200" height="95" fill="url(#redglow)" rx="6"/>
  <rect x="20" y="45" width="200" height="95" fill="none" stroke="#2a1010" stroke-width="1" rx="6"/>
  <text x="120" y="90" text-anchor="middle" font-family="Arial Black" font-size="30" font-weight="900" fill="#e74c3c">45s</text>
  <text x="120" y="115" text-anchor="middle" font-family="monospace" font-size="10" fill="#8b949e">fault isolation time</text>
  <text x="120" y="130" text-anchor="middle" font-family="monospace" font-size="10" fill="#27ae60">↓ 91% faster</text>

  <!-- Stat 2 -->
  <rect x="250" y="45" width="200" height="95" fill="url(#redglow)" rx="6"/>
  <rect x="250" y="45" width="200" height="95" fill="none" stroke="#2a1010" stroke-width="1" rx="6"/>
  <text x="350" y="90" text-anchor="middle" font-family="Arial Black" font-size="30" font-weight="900" fill="#e74c3c">100%</text>
  <text x="350" y="115" text-anchor="middle" font-family="monospace" font-size="10" fill="#8b949e">failure detection rate</text>
  <text x="350" y="130" text-anchor="middle" font-family="monospace" font-size="10" fill="#27ae60">↑ from ~60%</text>

  <!-- Stat 3 -->
  <rect x="480" y="45" width="200" height="95" fill="url(#redglow)" rx="6"/>
  <rect x="480" y="45" width="200" height="95" fill="none" stroke="#2a1010" stroke-width="1" rx="6"/>
  <text x="580" y="90" text-anchor="middle" font-family="Arial Black" font-size="30" font-weight="900" fill="#e74c3c">0.98</text>
  <text x="580" y="115" text-anchor="middle" font-family="monospace" font-size="10" fill="#8b949e">latency correlation (r)</text>
  <text x="580" y="130" text-anchor="middle" font-family="monospace" font-size="10" fill="#27ae60">token → latency predictor</text>
</svg>

</div>

---

## 🔑 The Key Finding

<div align="center">

<svg viewBox="0 0 700 220" xmlns="http://www.w3.org/2000/svg" width="700">
  <rect width="700" height="220" fill="#0d1117" rx="8"/>
  <rect x="1" y="1" width="698" height="218" fill="none" stroke="#2a1010" stroke-width="1" rx="8"/>
  <text x="350" y="30" text-anchor="middle" font-family="monospace" font-size="11" fill="#e74c3c" letter-spacing="4">LATENCY vs TOKEN COUNT</text>

  <!-- Bars -->
  <rect x="80" y="155" width="60" height="20" fill="#c0392b" rx="3">
    <animate attributeName="height" from="0" to="20" dur="1s" fill="freeze"/>
    <animate attributeName="y" from="175" to="155" dur="1s" fill="freeze"/>
  </rect>
  <text x="110" y="148" text-anchor="middle" font-family="monospace" font-size="11" fill="#ffffff">0.20s</text>
  <text x="110" y="185" text-anchor="middle" font-family="monospace" font-size="10" fill="#8b949e">45 tokens</text>

  <rect x="220" y="127" width="60" height="48" fill="#c0392b" rx="3">
    <animate attributeName="height" from="0" to="48" dur="1.2s" fill="freeze"/>
    <animate attributeName="y" from="175" to="127" dur="1.2s" fill="freeze"/>
  </rect>
  <text x="250" y="120" text-anchor="middle" font-family="monospace" font-size="11" fill="#ffffff">0.38s</text>
  <text x="250" y="185" text-anchor="middle" font-family="monospace" font-size="10" fill="#8b949e">128 tokens</text>

  <rect x="360" y="61" width="60" height="114" fill="#c0392b" rx="3">
    <animate attributeName="height" from="0" to="114" dur="1.4s" fill="freeze"/>
    <animate attributeName="y" from="175" to="61" dur="1.4s" fill="freeze"/>
  </rect>
  <text x="390" y="54" text-anchor="middle" font-family="monospace" font-size="11" fill="#ffffff">0.91s</text>
  <text x="390" y="185" text-anchor="middle" font-family="monospace" font-size="10" fill="#8b949e">420 tokens</text>

  <rect x="500" y="40" width="60" height="135" fill="#e74c3c" rx="3">
    <animate attributeName="height" from="0" to="135" dur="1.6s" fill="freeze"/>
    <animate attributeName="y" from="175" to="40" dur="1.6s" fill="freeze"/>
  </rect>
  <text x="530" y="33" text-anchor="middle" font-family="monospace" font-size="11" fill="#ffffff">1.42s</text>
  <text x="530" y="185" text-anchor="middle" font-family="monospace" font-size="10" fill="#8b949e">760 tokens</text>

  <line x1="50" y1="175" x2="650" y2="175" stroke="#2a1010" stroke-width="1"/>
  <text x="350" y="210" text-anchor="middle" font-family="monospace" font-size="11" fill="#e74c3c" letter-spacing="2">r = 0.98 Pearson Correlation</text>
</svg>

</div>

> **💡 Your prompt length is your performance problem. Not your model. Not your server. Your prompts.**

---

## 🛠 Tech Stack

```
┌─────────────────────────────────────────────────────────┐
│                   LLM OBSERVABILITY STACK                │
├──────────────────┬──────────────────┬────────────────────┤
│   AI Layer       │  Observability   │   Infrastructure   │
├──────────────────┼──────────────────┼────────────────────┤
│ Python 3.11      │ Langfuse v2      │ Docker             │
│ OpenAI API       │ OpenTelemetry    │ PostgreSQL         │
│ LangChain        │ OTLP Exporter    │ Redis              │
│ gpt-4o-mini      │ Trace Spans      │ VS Code            │
└──────────────────┴──────────────────┴────────────────────┘
```

---

## 🏗 Architecture

```
User Prompt
     │
     ▼
┌─────────────────────┐
│  Python LLM App     │ ← OpenAI API (gpt-4o-mini)
│  + LangChain        │
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│  OpenTelemetry      │ ← Instruments every request
│  Instrumentation    │   Captures: latency, tokens,
└────────┬────────────┘   traces, errors, metadata
         │  OTLP Export
         ▼
┌─────────────────────┐
│  Langfuse Backend   │ ← Deployed via Docker
│  + PostgreSQL       │   Stores all telemetry
│  + Redis            │
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│  Langfuse Dashboard │ ← Real-time visualization
│  Traces · Tokens    │   Latency · Errors · Spans
│  Latency · Errors   │
└─────────────────────┘
```

---

## ⚡ Failure Detection Results

All **4 failure categories** detected with **100% accuracy**:

| Failure Type | Cause | Detection Method | Rate | Avg Time |
|---|---|---|---|---|
| 🔑 Invalid API Key | Auth failure | Runtime error logs | 3/3 | **0.4s** |
| 💥 Token Overflow | Context exceeded | Token telemetry | 3/3 | **0.8s** |
| 🌐 Network Interruption | Connection loss | Failed traces | 3/3 | **1.6s** |
| ⏱ API Timeout | Delayed response | Latency monitoring | 3/3 | **2.1s** |

---

## 📊 Comparison: Traditional Logging vs This Framework

| Feature | Traditional Logging | This Framework |
|---|---|---|
| Runtime Tracing | ❌ Limited | ✅ Comprehensive |
| Token Monitoring | ❌ Not Available | ✅ Full breakdown |
| Latency Analysis | ⚠️ Basic | ✅ Advanced |
| Failure Detection | ❌ Manual (~60%) | ✅ Automated (100%) |
| Telemetry Visualization | ❌ Not Supported | ✅ Langfuse Dashboard |
| **Avg Fault Isolation** | **~8 minutes** | **~45 seconds** |

---

## 🚀 Quick Start

### 1. Clone the repo
```bash
git clone https://github.com/yourusername/talk-to-your-data.git
cd LangFuse
```

### 2. Start Langfuse with Docker
```bash
docker-compose up -d
```

### 3. Install dependencies
```bash
pip install openai langfuse opentelemetry-sdk opentelemetry-exporter-otlp langchain
```

### 4. Set environment variables
```bash
export OPENAI_API_KEY=your_openai_key
export LANGFUSE_PUBLIC_KEY=your_langfuse_public_key
export LANGFUSE_SECRET_KEY=your_langfuse_secret_key
```

### 5. Run
```bash
python main.py
```

Open **http://localhost:3000** → Langfuse Dashboard

---

## 📁 Project Structure

```
LangFuse/
├── main.py                  # Instrumented LLM application
├── observability.py         # OpenTelemetry tracer setup
├── langfuse_client.py       # Langfuse SDK integration
├── experiments/
│   ├── latency_test.py      # Latency vs token experiments
│   ├── failure_sim.py       # Failure simulation scripts
│   └── concurrent_test.py   # Concurrent request analysis
├── docker-compose.yml       # Langfuse + PostgreSQL + Redis
├── requirements.txt
└── README.md
```

---

## 📄 Research Paper

**Title:** LLM Observability Using Langfuse and OpenTelemetry for Monitoring AI Application Reliability

**Author:** Aum Aswar · School of Engineering, Parul University, Gujarat, India

**Published under:** Reliance Industries Limited · Project 2324R

**Key Contributions:**
- Quantified r = 0.98 correlation between token count and latency
- 100% failure detection rate across 4 failure categories
- 91% reduction in fault isolation time vs traditional logging
- Reusable Docker deployment configuration for local Langfuse

---

<div align="center">

<svg viewBox="0 0 700 60" xmlns="http://www.w3.org/2000/svg" width="700">
  <rect width="700" height="60" fill="#0d1117" rx="8"/>
  <rect x="0" y="0" width="700" height="2" fill="#c0392b" rx="1"/>
  <text x="350" y="25" text-anchor="middle" font-family="monospace" font-size="12" fill="#8b949e" letter-spacing="2">Built during AI/ML Internship</text>
  <text x="350" y="45" text-anchor="middle" font-family="Arial Black" font-size="13" font-weight="900" fill="#e74c3c" letter-spacing="1">RELIANCE INDUSTRIES LIMITED</text>
</svg>

<br/>

**Aum Aswar** · AI/ML Engineer · Parul University, Vadodara

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/aum-aswar-3837823b3/)
[![Email](https://img.shields.io/badge/Email-Contact-C0392B?style=for-the-badge&logo=gmail&logoColor=white)](mailto:aum.aswar06@gmail.com)

</div>
