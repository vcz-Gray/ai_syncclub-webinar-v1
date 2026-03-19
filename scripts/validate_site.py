#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def check_exists(*paths: str) -> None:
    for rel in paths:
        path = ROOT / rel
        assert path.exists(), rel


def check_contains(path: str, *tokens: str) -> None:
    text = (ROOT / path).read_text()
    for token in tokens:
        assert token in text, (path, token)


def validate_bootstrap() -> None:
    check_exists("index.html", "webinar/index.html", "styles/site.css", "scripts/validate_site.py", "assets/book_cover.jpeg")
    check_contains("index.html", "박규하", "안티그래비티 바이브 코딩 입문", "웨비나 자료", "skills")


def validate_deploy() -> None:
    check_exists(".github/workflows/deploy-pages.yml")
    check_contains(
        ".github/workflows/deploy-pages.yml",
        "actions/configure-pages@v5",
        "actions/upload-pages-artifact@v4",
        "actions/deploy-pages@v4",
        "pages: write",
        "id-token: write",
        "main",
    )


def validate_content() -> None:
    check_exists(
        "tips/index.html",
        "downloads/participant-cheatsheet.md",
        "downloads/prd-template.md",
        "downloads/stitch-prompt-pack.md",
        "downloads/post-webinar-next-steps.md",
        "downloads/stitch-update-summary.md",
        "downloads/faq-and-common-mistakes.md",
        "downloads/promo-copy-kit.md",
    )
    check_contains("tips/index.html", "꿀팁", "PRD", "Stitch", "FAQ")


def validate_examples() -> None:
    check_exists("examples/index.html")
    text = (ROOT / "examples/index.html").read_text()
    assert text.count("data-example-card") >= 24, text.count("data-example-card")


def validate_skills() -> None:
    skills = [
        "service-idea-prd",
        "stitch-prompt-crafter",
        "webinar-followup-kit",
        "event-promo-copy",
    ]
    for skill in skills:
        check_exists(f"skills/{skill}/SKILL.md", f"skills/{skill}/agents/openai.yaml")


def validate_full() -> None:
    validate_bootstrap()
    validate_deploy()
    validate_content()
    validate_examples()
    validate_skills()
    check_exists("README.md", "downloads/index.html", "skills/index.html")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--phase", choices=["bootstrap", "deploy", "content", "examples", "skills", "full"], required=True)
    phase = parser.parse_args().phase
    {
        "bootstrap": validate_bootstrap,
        "deploy": validate_deploy,
        "content": validate_content,
        "examples": validate_examples,
        "skills": validate_skills,
        "full": validate_full,
    }[phase]()
    print("OK")


if __name__ == "__main__":
    main()
