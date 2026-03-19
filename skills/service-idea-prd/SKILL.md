---
name: service-idea-prd
description: Turn a rough service idea into a compact 4-question PRD for AI UI generation. Use this when a user has an idea but needs help defining user, problem, core features, and screen count before using Stitch or coding tools.
---

# Service Idea PRD

Use this skill when the user says they have an app, service, tool, or product idea but it is still vague.

## Workflow

1. Ask for the service in one sentence.
2. Identify one primary user.
3. Define one concrete pain point.
4. Limit features to three.
5. Limit the initial screen plan to three or four.
6. Output a short PRD that can be pasted into Stitch or another AI tool.

## Output Format

```md
### 서비스 이름
### 핵심 사용자
### 핵심 문제
### 핵심 기능 3개
### 화면 구성
### 한 줄 설명
```

## Rules

- Do not let the scope grow beyond a first usable flow.
- Push the user to pick one user and one problem.
- If the idea is too broad, split into “지금 버전” and “다음 버전”.

Read `references/examples.md` for sample PRDs when needed.
