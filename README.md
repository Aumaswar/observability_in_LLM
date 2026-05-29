<div align="center">

![Header](https://capsule-render.vercel.app/api?type=waving&color=c0392b&height=220&section=header&text=LLM%20Observability&fontSize=55&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=Langfuse%20%C2%B7%20OpenTelemetry%20%C2%B7%20Python%20%C2%B7%20Docker&descAlignY=56&descAlign=50&descSize=16)

![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&size=18&duration=2500&pause=800&color=E74C3C&center=true&vCenter=true&width=700&height=50&lines=Built+during+AI%2FML+Internship+%40+Reliance+Industries;Fault+isolation%3A+8+minutes+%E2%86%92+45+seconds;100%25+failure+detection+rate;r+%3D+0.98+token+%E2%86%92+latency+correlation)

<br/>

![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o--mini-412991?style=for-the-badge&logo=openai&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-Framework-1C3C3C?style=for-the-badge&logo=chainlink&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Deployed-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Research](https://img.shields.io/badge/Research-Published-C0392B?style=for-the-badge&logo=academia&logoColor=white)
![Reliance](https://img.shields.io/badge/Reliance-Industries-C0392B?style=for-the-badge&logoColor=white)

</div>

---

## 🚨 The Problem

LLM apps are **black boxes**.

When something breaks or slows down, traditional logs give you almost nothing useful. Developers spend **minutes guessing** instead of seconds fixing.

| Metric | Traditional Logging |
|---|---|
| Avg Fault Isolation | ⏱ ~8 minutes |
| Failure Detection Rate | ❌ ~60% |
| Token Monitoring | ❌ Not Available |
| Latency Analysis | ⚠️ Basic only |

---

## ✅ What This Framework Achieves

<div align="center">

![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&size=16&duration=2000&pause=500&color=27AE60&center=true&vCenter=true&width=600&height=40&lines=45+seconds+fault+isolation+%E2%86%93+91%25+faster;100%25+failure+detection+rate;Full+token+%2B+latency+visibility;Real-time+Langfuse+dashboard)

</div>

| Metric | Traditional Logging | This Framework |
|---|---|---|
| Fault Isolation Time | ~8 minutes | ✅ **45 seconds** |
| Failure Detection Rate | ~60% | ✅ **100%** |
| Token Monitoring | ❌ Not Available | ✅ Full breakdown |
| Latency Analysis | ⚠️ Basic | ✅ Advanced |
| Telemetry Visualization | ❌ Not Supported | ✅ Langfuse Dashboard |

---

## 🔑 The Key Finding

<div align="center">

![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&size=16&duration=3000&pause=1000&color=E74C3C&center=true&vCenter=true&width=700&height=40&lines=Your+prompt+length+is+your+performance+problem.;Not+your+model.+Not+your+server.+Your+prompts.)

</div>

| Prompt Size | Avg Latency | Trend |
|---|---|---|
| 45 tokens | 0.20s | 🟢 Fast |
| 128 tokens | 0.38s | 🟡 Medium |
| 420 tokens | 0.91s | 🟠 Slow |
| 760 tokens | 1.42s | 🔴 Very Slow |

> **Pearson Correlation r = 0.98** — token count predicts latency with near-perfect accuracy.
>
> **💡 Optimize your prompts before optimizing your infrastructure.**

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
│  OpenTelemetry      │ ← Captures: latency, tokens,
│  Instrumentation    │   traces, errors, metadata
└────────┬────────────┘
         │  OTLP Export
         ▼
┌─────────────────────┐
│  Langfuse Backend   │ ← Deployed via Docker
│  PostgreSQL + Redis │
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│  Langfuse Dashboard │ ← Real-time visualization
│  Traces · Tokens    │
└─────────────────────┘
```

---

## ⚡ Failure Detection — 100% Rate

All **4 failure categories** detected across every single test:

| Failure Type | Cause | Detection Method | Rate | Avg Time |
|---|---|---|---|---|
| 🔑 Invalid API Key | Auth failure | Runtime error logs | 3/3 | **0.4s** |
| 💥 Token Overflow | Context exceeded | Token telemetry | 3/3 | **0.8s** |
| 🌐 Network Interruption | Connection loss | Failed traces | 3/3 | **1.6s** |
| ⏱ API Timeout | Delayed response | Latency monitoring | 3/3 | **2.1s** |

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

Open **http://localhost:3000** → Langfuse Dashboard 🎉

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
- Quantified **r = 0.98** correlation between token count and latency
- **100% failure detection rate** across 4 failure categories
- **91% reduction** in fault isolation time vs traditional logging
- Reusable Docker deployment for local Langfuse infrastructure

---

<div align="center">

![Footer](https://capsule-render.vercel.app/api?type=waving&color=c0392b&height=120&section=footer&text=Aum%20Aswar&fontSize=30&fontColor=ffffff&animation=fadeIn&fontAlignY=65&desc=AI%2FML+Engineer+%C2%B7+Parul+University+%C2%B7+Reliance+Industries&descAlignY=85&descAlign=50&descSize=13)

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/aum-aswar-3837823b3/)
[![Email](https://img.shields.io/badge/Email-Contact-C0392B?style=for-the-badge&logo=gmail&logoColor=white)](mailto:aum.aswar06@gmail.com)

</div>
