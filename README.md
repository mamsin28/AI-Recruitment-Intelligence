# AI Recruitment Intelligence

> Multi-Agent RAG System for Intelligent Recruitment

---

## Overview

AI Recruitment Intelligence is an enterprise-grade recruitment platform powered by Large Language Models (LLMs), Retrieval-Augmented Generation (RAG), and Multi-Agent Architecture.

The platform analyzes resumes and job descriptions, retrieves the most relevant candidate information, evaluates candidate-job compatibility, generates interview questions, creates personalized cover letters, and assists recruiters through intelligent automation.

---

## Key Features

- Resume Parsing
- Job Description Analysis
- Retrieval-Augmented Generation (RAG)
- Multi-Agent Workflow
- Candidate Matching
- Missing Skills Detection
- Interview Question Generation
- Cover Letter Generation
- Recruiter Communication Assistant
- Explainable AI Reports

---

## System Architecture

```text
                 User
                   │
                   ▼
             FastAPI Backend
                   │
                   ▼
            Router Controller
                   │
        ┌──────────┴──────────┐
        ▼                     ▼
 Document Service      Job Service
        │                     │
        └──────────┬──────────┘
                   ▼
            RAG Pipeline
                   │
            ChromaDB Vector DB
                   │
                   ▼
             LangGraph Agents
                   │
                   ▼
             Final AI Report
             