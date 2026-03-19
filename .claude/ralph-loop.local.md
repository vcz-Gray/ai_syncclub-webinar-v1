---
active: true
iteration: 1
session_id:
max_iterations: 11
completion_promise: "COMPLETE"
started_at: "2026-03-19T19:40:00+09:00"
---

Read `slides-review-prd.json` for task plan. Read `slides-review-progress.txt` for status first.
Stay on `main`.
Pick the highest-priority story where `passes` is `false`.
Implement that ONE story.
Run verification:

```bash
python3 - <<'PY'
from pathlib import Path
import re
html = Path('/Users/viewcommz/Downloads/안티그래비티/웨비나0320ppt간.html').read_text() if Path('/Users/viewcommz/Downloads/안티그래비티/웨비나0320ppt간.html').exists() else Path('/Users/viewcommz/Downloads/안티그래비티/웨비나0320ppt가안.html').read_text()
assert '2026.3.20 (금)' in html
assert '추천 알고리즘의 과학' in html
assert '리뷰를 남겨주신 분들 중 5분께' in html
nums = re.findall(r'<div class=\"slide-number\">(\\d+) / 25</div>', html)
assert len(nums) == 25
print('OK')
PY
```

Use browser verification for overflow checks and alignment checks on the target slide before marking a story complete.
On success: commit using Korean gitmoji format, update `slides-review-prd.json`, append to `slides-review-progress.txt`.
If all stories pass: `<promise>COMPLETE</promise>`.
