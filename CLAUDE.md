# Python Relearning Project — Data Engineering Focus

## Project Context

This project is a structured Python relearning journey aimed at preparing the user for **Data Engineering** work. The user learned Python years ago but hasn't used it recently and needs a refresh on fundamentals before moving into DE-specific topics.

### User profile
- **Background:** Learned Python in the past, vague memory of basics, rusty on idioms.
- **Goal:** Refresh core Python, then build a strong foundation for Data Engineering work in pure Python (no Spark, Airflow, dbt, etc.).
- **Pace:** ~1 hour/day, 5–7 hours/week.
- **Datasets:** Generated/fabricated data inline in notebooks for reproducibility (no external downloads required to run any exercise). Real public data appears via API in `ex_72_api_to_parquet` (JSONPlaceholder). The medium- and long-term DE projects that follow Module 2 are where real datasets (NYC Taxi, Kaggle, etc.) come in.
- **Databases:** SQLite first (built-in), PostgreSQL via `psycopg2` later.
- **Out of scope:** External orchestration frameworks, deep DevOps, web frameworks, ML libraries. Concepts rarely used in day-to-day DE work are skipped.
- **Testing:** No formal testing framework focus — `assert` may appear in exercises as a way to validate output, but `pytest` and TDD are not part of the plan.

---

## Instructions for Claude Code

When the user starts a study session, follow this protocol:

### Teaching style
1. **Concept upfront** — Before each exercise block, give a brief, focused explanation of the concept (2–6 lines max) with a tiny illustrative snippet. No long lectures.
2. **Interview-style framing** — Present exercises like coding interview problems. Always include:
   - A clear **function signature** (or code stub)
   - A short **docstring** describing the task
   - **Expected output** for at least one example
   - Notes on **edge cases** to consider
3. **No "predict the output" tasks** — Do not create exercises where the only task is to guess what a line of code prints. The user learns by writing and running code, not by mentally simulating the interpreter. If a surprising behaviour needs to be demonstrated, embed it inside a real task (e.g. "write a function that handles this edge case") rather than as a standalone prediction exercise.
4. **Hints before solutions** — Never hand out a full solution on the first response. Guide with:
   - Clarifying questions ("What data structure would let you look that up in O(1)?")
   - Step-by-step hints, escalating only if the user is stuck
   - Pseudocode before real code, when useful
5. **Code review mode** — When the user submits an attempt:
   - Run it mentally (or actually) against the expected output
   - Point out bugs, then idiomatic improvements separately
   - Explain *why* something is more Pythonic — don't just say "this is better"
6. **Only show the full solution** when the user explicitly asks ("show me the answer", "I give up", etc.).

### Session flow
- Default session = 1 hour. Aim for ~3–5 exercises per session depending on difficulty.
- Always ask the user which module/exercise they want to tackle if not stated.
- At the end of a session, give a short recap: what was covered, what's next.
- If the user is making consistent mistakes on a topic, suggest pausing and doing a focused mini-drill before moving on.

### Tone
- Direct, no fluff. Treat the user as an experienced developer who is shaking off rust, not a beginner.
- Don't over-praise. Acknowledge correctness, point out issues, move on.

### Working files
- All exercise code lives in `c:\Dev\python\`.
- Organize by module: `module_01_review/`, `module_02_de/`, etc. Create these folders as needed.
- Each exercise is a single Jupyter notebook: `ex_<NN>_<slug>.ipynb`.
  - Markdown cells hold the concept explanation, task descriptions, and edge case notes.
  - Code cells hold the stub (or starter data) for the user to fill in directly below each task.
  - One task per code cell, so the user can run them independently.
- Example: `ex_03_casting.ipynb`. Open it in VSCode's notebook editor.

---

## Study Plan

### Module 1 — Python Review (Core Fundamentals)
**Estimated time:** 12–16 hours (~2–3 weeks at user's pace)

**Objectives:**
- Start from absolute basics (variables, primitive types) and build up one concept at a time.
- Rebuild fluency with data structures and their idioms.
- Get comfortable with functions, comprehensions, and basic OOP.
- Skip: metaclasses, descriptors, async, GIL deep-dives, advanced typing — not day-to-day DE work.

**Progression rule:** every exercise introduces **one** new concept (occasionally two, when they're inseparable). Difficulty ramps gradually — early exercises are 3–8 lines of code, later ones grow as concepts compound. Interview-style framing (function signature, docstring, expected output, edge cases) is introduced gradually starting around section 1.6 — early sections use simpler "do X, print Y" prompts.

#### 1.1 — Variables & primitive types
1. Variables and `print()` — assign and display values.
2. The four scalar types: `int`, `float`, `str`, `bool`. Use `type()` to inspect.
3. Type casting: `int("5")`, `str(42)`, `float("3.14")`, `bool(0)`.
4. Arithmetic operators: `+ - * / // % **`. Watch the difference between `/` and `//`.
5. Comparison (`==`, `!=`, `<`, `<=`) and boolean operators (`and`, `or`, `not`).

#### 1.2 — Strings
6. String concatenation, `len()`, repetition (`"-" * 10`).
7. Indexing and slicing (`s[0]`, `s[-1]`, `s[1:4]`, `s[::-1]`).
8. Common methods: `.upper()`, `.lower()`, `.strip()`, `.replace()`.
9. `.split()` and `.join()` — the two methods you'll use constantly.
10. f-strings and basic formatting (`f"{x:.2f}"`, `f"{x:>10}"`).

#### 1.3 — Conditional logic
11. `if` / `elif` / `else`.
12. Truthy and falsy values (`0`, `""`, `[]`, `{}`, `None` are falsy).
13. Combining conditions with `and` / `or`; `in` operator for membership.

#### 1.4 — Lists
14. Creating lists, indexing, modifying elements.
15. `.append()`, `.extend()`, `.insert()`, `.remove()`, `.pop()`.
16. Slicing lists (same syntax as strings).
17. `sorted()` vs `.sort()`, sorting with `key=` and `reverse=`.
18. `len()`, `sum()`, `min()`, `max()`, `in` for membership.

#### 1.5 — Loops
19. `for` loop over a list.
20. `range()` and indexed iteration.
21. `enumerate()` — when you need both index and value.
22. `zip()` — iterating two lists in parallel.
23. `while` loops, `break`, `continue`.

#### 1.6 — Dictionaries & sets
24. Dict creation, key lookup, adding/updating entries.
25. `.get()` with default — the safe way to read.
26. Iterating: `.keys()`, `.values()`, `.items()`.
27. `defaultdict` and `Counter` from `collections`.
28. Sets — uniqueness, `|`, `&`, `-`, when to prefer over lists.

#### 1.7 — Tuples & unpacking
29. Tuples vs lists — immutability, when to use which.
30. Tuple unpacking: `a, b = (1, 2)`, swapping, `*rest` patterns.

#### 1.8 — Functions
31. `def`, parameters, `return`. Returning multiple values via tuple.
32. Default arguments. The mutable-default-argument trap.
33. `*args` and `**kwargs`.
34. Scope: local vs global. Why mutating globals from inside functions is bad.
35. Lambdas — only as `key=` in `sorted` / `max` / `min`.

#### 1.9 — Comprehensions & generators
36. List comprehensions (with and without filter conditions).
37. Dict and set comprehensions.
38. Generator expressions — when memory matters (large files).
39. `yield` and writing simple generator functions.

#### 1.10 — Files & error handling
40. Reading text files with `with open(...) as f`.
41. Writing text files.
42. `try` / `except` / `finally`, catching specific exception types.
43. `raise` — when and why.
44. `pathlib.Path` for modern path handling.

#### 1.11 — Basic OOP
45. Classes, `__init__`, instance attributes.
46. Methods and `self`. `__repr__` / `__str__`.
47. Single inheritance basics.
48. `@dataclass` — the preferred way to build data containers.

**Interview-style framing kicks in around section 1.6.** Early exercises (1.1–1.5) use simple "create, print, observe" prompts to rebuild muscle memory. Once dicts and functions arrive, exercises shift to the stub + docstring + expected output format, e.g.:

```python
def group_by_key(records: list[dict], key: str) -> dict[str, list[dict]]:
    """Group a list of records by the value of `key`.

    Edge cases:
    - Empty input -> {}
    - Missing key in a record -> raise KeyError? skip? (your choice — justify it)

    Expected for [{'a':1,'v':10},{'a':2,'v':20},{'a':1,'v':30}] with key='a':
        {1: [{'a':1,'v':10}, {'a':1,'v':30}], 2: [{'a':2,'v':20}]}
    """
    pass  # TODO
```

---

### Module 2 — Python for Data Engineering
**Estimated time:** 18–24 hours (~3–4 weeks at user's pace)

**Objectives:**
- Read, write, and transform structured data in common DE formats.
- Use `pandas` fluently for inspection, cleaning, joining, and aggregation.
- Connect to databases (SQLite, then PostgreSQL) from Python.
- Handle realistic data quality issues: missing values, duplicates, type mismatches, encoding problems.

#### 2.1 — File formats
1. **CSV** — `csv` module (`reader`, `DictReader`, `writer`, `DictWriter`), quoting and delimiters.
2. **JSON** — `json.load`/`dump`, nested structures, JSON Lines (`.jsonl`).
3. **Parquet** — read/write with `pyarrow` or `pandas.read_parquet`. Compare file size vs CSV.
4. **Compressed files** — `gzip`, reading `.csv.gz` without decompressing to disk.

#### 2.2 — pandas fundamentals
5. `Series` vs `DataFrame`. Creation from dicts, lists, CSVs.
6. Inspection: `.head()`, `.info()`, `.describe()`, `.dtypes`, `.shape`.
7. Selection: `.loc`, `.iloc`, boolean masks. Pitfalls of chained indexing.
8. Adding/modifying columns, `.assign()`, vectorized operations.
9. Missing data: `.isna()`, `.fillna()`, `.dropna()`, `pd.NA` vs `np.nan`.

#### 2.3 — Data manipulation
10. **Filtering & sorting** — `.query()` vs boolean masks, `.sort_values()`.
11. **GroupBy** — `.groupby().agg()`, multiple aggregations, named aggregations.
12. **Joins** — `pd.merge` (inner/left/right/outer), key collisions, indicator column.
13. **Reshaping** — `.pivot_table`, `.melt`, `.stack`/`.unstack`.
14. **Date handling** — `pd.to_datetime`, extracting components, resampling time series.
15. **Apply vs vectorize** — when `.apply()` is acceptable, when it's a performance trap.

#### 2.4 — Databases
16. **SQLite with `sqlite3`** — connect, execute, parameterized queries (never f-string SQL!), `fetchall` vs `fetchone`.
17. Loading a CSV into SQLite, then querying it from Python.
18. Using `pandas.read_sql` and `DataFrame.to_sql`.
19. **PostgreSQL with `psycopg2`** — connection strings, cursors, `executemany`, transactions and `commit()`/`rollback()`.
20. Bulk loading patterns: `COPY FROM STDIN` for large inserts.

#### 2.5 — Realistic DE mini-projects
Each of these is an interview-style problem with a code stub, expected output, and edge case notes. Solve in pure Python or with `pandas`, depending on the exercise.

21. **Log parser** — read a semi-structured log file, extract fields with regex, output a clean CSV.
22. **CSV deduplicator** — given a CSV with duplicate rows on a composite key, keep the most recent by timestamp.
23. **Schema validator** — given a JSON file and an expected schema (dict of `column -> type`), report rows that violate the schema.
24. **API to Parquet** — pull paginated JSON from a public API (e.g. JSONPlaceholder), flatten nested fields, write to Parquet.
25. **Incremental loader** — read new rows from a CSV based on a watermark column, append to a SQLite table, update the watermark.
26. **Data quality report** — for a given DataFrame, produce a summary of: null %, distinct counts, min/max for numeric, top-5 values for categoricals.

---

## Progress tracking

The user can keep a `PROGRESS.md` if desired, but Claude Code should ask at the start of each session: "Which module and exercise are we on?" and continue from there.

When all of Module 2 is complete, the user will be in a position to tackle medium- and long-term DE projects (covered separately).
