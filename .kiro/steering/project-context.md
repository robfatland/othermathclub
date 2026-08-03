# Project Context

## Overview

This workspace supports a **middle school Python/Science/Math/Engineering club**. All content, code, and activities are designed for students roughly ages 11–14.

## Guiding Principles

- **Accessibility**: Code and explanations should be approachable for beginners. Prefer clarity over cleverness.
- **Educational focus**: Every project should teach something — a math concept, a coding pattern, a scientific principle, or an engineering skill.
- **Python-first**: The primary language is Python. Use standard-library or well-known packages (matplotlib, numpy, etc.) when needed.
- **Visual and interactive**: Prioritize outputs students can see — plots, animations, simulations, and games.
- **Safe and encouraging**: Language and content should be age-appropriate, supportive, and curiosity-driven.

## Technical Conventions

- Target Python 3.10+
- Use Jupyter notebooks (.ipynb) for exploratory/teaching content
- Use standalone .py files for reusable modules and utilities
- Keep dependencies minimal and well-documented
- Include comments that explain *why*, not just *what*
- Prefer descriptive variable names over terse ones

## Python Execution Workflow

The user runs Python locally in WSL (Ubuntu) via miniconda. Kiro cannot execute Python directly. Instead:

- Kiro writes Python scripts to the workspace or provides commands to paste
- The user runs them in their WSL bash shell
- The user reports output back to Kiro if needed
- All Python commands should assume the miniconda base environment is active
- Use `python` (not `python3`) as the command — miniconda aliases it correctly

## Repository Structure

- `A3_Images/` — Generated images organized by math topic
- `torusmare/` — Torus Mare: an exploration game on a toroidal ocean planet

## Torus Mare Project

Torus Mare is a client-server exploration game designed to teach students HTTP communication using Python's `requests` library. Key characteristics:

- **Server**: Stateless HTTP backend deployed as an AWS Lambda function (zip packaging, no containers, no web framework)
- **API Gateway**: AWS HTTP API providing the HTTPS endpoint, routing, and throttling
- **Data store**: DynamoDB (pay-per-request mode) for all game state — grid, player positions, features, roster
- **Client**: Student-written Python code using `requests` for HTTP calls and `matplotlib` for grid visualization
- **World model**: A rectangular grid with torus topology (left↔right, top↔bottom wrapping)
- **Privacy**: No student names stored; players identified by random 7-digit PIDs
- **Access modes**: Anonymous (registration puzzle), Player (gameplay), Admin (management)
- **Educational goals**: HTTP methods, JSON parsing, REST API patterns, coordinate systems, modular arithmetic (wrapping)
- **Deployment**: Single Python handler file, zipped, uploaded directly to Lambda. No Docker, no Flask, no WSGI adapters.
