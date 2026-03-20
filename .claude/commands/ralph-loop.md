# Ralph Loop — 모바일 대응 + 다운로드 버튼

이 프로젝트는 GitHub Pages로 배포되는 정적 사이트입니다.
배포 URL: `https://vcz-gray.github.io/ai_syncclub-webinar-v1/`

## 작업 대상

**웨비나 페이지(`webinar/`)를 제외한** 모든 HTML 페이지:
- `index.html` (루트 허브)
- `tips/index.html` (꿀팁)
- `examples/index.html` (예시 모음)
- `downloads/index.html` (다운로드)
- `skills/index.html` (Skills)

공통 CSS: `styles/site.css`

## Task 1: 모바일 대응

배포된 페이지를 기준으로 모바일(375px~768px)에서 깨지는 부분을 전부 수정하세요.

### 점검 항목

1. **타이포그래피**: h1, h2, section-title이 모바일에서 너무 크지 않은지. `clamp()` 활용.
2. **그리드 레이아웃**: `.card-grid`, `.example-grid`, `.split-grid`, `.meta-list`가 1열로 잘 떨어지는지.
3. **hero 섹션**: `.hero-grid`가 모바일에서 세로 스택으로 전환되는지. 이미지가 넘치지 않는지.
4. **topbar**: 모바일에서 세로 정렬, 터치 타겟 44px 이상, 스크롤 시 가리지 않는지.
5. **카드/패널**: `.card`, `.panel`, `.download-item`, `.example-item`, `.skill-item`의 패딩과 폰트가 적절한지.
6. **버튼**: `.btn`의 터치 타겟(최소 44px), full-width 처리 여부.
7. **가로 스크롤**: 어떤 화면 너비에서도 가로 스크롤이 발생하지 않아야 함.
8. **간격**: 섹션 간 여백, 카드 간 간격이 모바일에서 과도하지 않은지.

### 작업 방법

1. `styles/site.css`의 기존 `@media (max-width: 980px)` 미디어 쿼리를 확인하고 보강.
2. 필요하면 `@media (max-width: 640px)` 추가 breakpoint 생성.
3. 각 HTML 파일의 인라인 스타일 중 모바일에서 문제되는 것 수정.
4. taste-skill 준수: `min-h-[100dvh]` 대신 `min-height: 100dvh`, Grid > Flex-Math, 모바일에서 단일 컬럼 + `px-4 py-8` 패턴.

## Task 2: *.md 파일 다운로드 버튼

`downloads/index.html`에 있는 각 `.md` 파일 링크에 대해:

1. 기존 `<a href="./파일명.md">` 링크는 유지 (브라우저에서 읽기용).
2. 각 download-item에 **별도의 다운로드 버튼**을 추가: `<a href="./파일명.md" download class="btn btn-sm">다운로드</a>`
3. `.btn-sm` 스타일을 `site.css`에 추가 (작은 pill 버튼, 터치 타겟 36px+).
4. `tips/index.html`의 다운로드 섹션에도 동일하게 적용.
5. PDF 파일(`안티그래비티_DAY0-1.pdf`)에는 이미 download 속성이 있으므로 유지.

### 다운로드 버튼 디자인 (taste-skill 준수)

```css
.btn-sm {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 6px 14px;
  border-radius: 10px;
  font-size: 13px;
  font-weight: 600;
  text-decoration: none;
  background: rgba(17, 17, 17, 0.06);
  border: 1px solid var(--line);
  color: var(--ink);
  transition: background 0.2s;
  cursor: pointer;
}
.btn-sm:hover {
  background: rgba(17, 17, 17, 0.1);
}
```

## 검증

작업 후 반드시:
1. 각 페이지를 375px, 768px, 1280px 너비에서 확인.
2. 가로 스크롤이 없는지 확인.
3. 다운로드 버튼이 실제로 파일을 다운로드하는지 확인.
4. `git add`, `git commit` (한국어 gitmoji), `git push origin main`으로 배포.

## 추가 지시사항

$ARGUMENTS
