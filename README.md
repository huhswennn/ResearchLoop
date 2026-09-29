# ResearchLoop

**From Evidence to Experiment**

ResearchLoop is an executable research-loop agent built around Qwen. It turns a research question or paper into a traceable sequence of evidence, hypotheses, executable experiment specifications, real runs, observations, critique, and next-step experiments.

## v0.1 scope

- Discover mode: question -> evidence -> hypothesis -> experiment -> run -> critique
- Reproduce mode: paper -> claims/methods -> experiment specification -> reproduction
- Human approval gates before experiments run
- Python is the first executor
- HFSS/PyAEDT is an optional scientific-tool adapter, not the product boundary
- Research state is structured data rather than chat history

## Architecture

- Frontend: Next.js / React
- API: FastAPI
- Core reasoning: Qwen through Alibaba Model Studio
- State: PostgreSQL + JSONB
- Queue/cache: Redis
- Artifacts: OSS or local development storage
- Tool layer: unified ResearchTool interface

## Start backend

1. Copy `.env.example` to `.env`
2. Install Python dependencies
3. Start PostgreSQL/Redis with Docker Compose
4. Run `uvicorn apps.api.main:app --reload`

## Start frontend

Run `npm install` and `npm run dev` inside `apps/web`.

## Project status

This repository currently contains the v0.1 engineering skeleton. The next milestones are persistent repositories, Qwen structured-output agents, evidence search, and the first executable loop.
