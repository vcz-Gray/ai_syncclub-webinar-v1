---
active: false
iteration: 6
session_id:
max_iterations: 17
completion_promise: "COMPLETE"
started_at: "2026-03-19T17:12:00+09:00"
---

Read `prd.json` for task plan. Read `progress.txt` for status, including Codebase Patterns first.
Work on `main` because this repository is empty and GitHub Pages should deploy from `main`.
Pick the highest priority story where `passes` is `false`.
Implement that ONE story, then run the most relevant validation:

- `python3 scripts/validate_site.py --phase bootstrap`
- `python3 scripts/validate_site.py --phase deploy`
- `python3 scripts/validate_site.py --phase content`
- `python3 scripts/validate_site.py --phase examples`
- `python3 scripts/validate_site.py --phase skills`
- `python3 scripts/validate_site.py --phase full`

On failure: fix and retry up to 3 times.
On success: commit using a Korean gitmoji message, update `prd.json`, and append to `progress.txt`.
If all stories pass: `<promise>COMPLETE</promise>`.
When stuck: write the blocker in `notes`, append it to `progress.txt`, and continue only if the next story is independent.
