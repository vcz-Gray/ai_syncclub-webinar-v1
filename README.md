# AI Syncclub Webinar Pack

AI 싱크클럽 웨비나를 위한 정적 GitHub Pages 허브입니다.  
수정된 발표 HTML, 참가자용 꿀팁, PRD 템플릿, Stitch 프롬프트, 예시 모음, 설치형 Codex skills를 한 곳에 모았습니다.

## 들어 있는 것

- `index.html`: 저자/책 중심 허브 랜딩
- `webinar/index.html`: 수정된 웨비나 발표본
- `tips/index.html`: 참가자용 꿀팁 페이지
- `examples/index.html`: 30개 예시 카탈로그
- `downloads/`: raw markdown 다운로드 패키지
- `skills/`: 설치형 Codex skill 4종
- `.github/workflows/deploy-pages.yml`: GitHub Pages 자동 배포

## GitHub Pages

이 저장소는 `main` 브랜치에 push 되면 GitHub Actions를 통해 자동 배포되도록 구성되어 있습니다.

예상 URL:

- `https://vcz-gray.github.io/ai_syncclub-webinar-v1/`

## 로컬 미리보기

```bash
python3 -m http.server 8123
```

브라우저에서 아래 경로를 확인합니다.

- `/`
- `/webinar/`
- `/tips/`
- `/examples/`
- `/downloads/index.html`
- `/skills/index.html`

## 검증

```bash
python3 scripts/validate_site.py --phase bootstrap
python3 scripts/validate_site.py --phase deploy
python3 scripts/validate_site.py --phase content
python3 scripts/validate_site.py --phase examples
python3 scripts/validate_site.py --phase skills
python3 scripts/validate_site.py --phase full
```

## Codex Skills

설치형 skill은 아래 4종입니다.

- `skills/service-idea-prd`
- `skills/stitch-prompt-crafter`
- `skills/webinar-followup-kit`
- `skills/event-promo-copy`

각 skill은 `SKILL.md`와 `agents/openai.yaml`을 포함하며, 자세한 예시는 `references/examples.md`에 있습니다.
