# dobeutech Dotfiles

Production-ready starter dotfiles repository for GitHub user `dobeutech`.

**Aligned with Ona dotfiles** (primary reference: https://ona.com/docs/ona/configuration/dotfiles/overview) and modern best practices for maintainable, cross-platform developer environments.

From Dobeu Tech Solutions, Neptune City, NJ — honest tools, built right.

## Repository Structure

```
.
├── .agent/                  # Bootstrap progress, tasks, state (for agent handoff)
├── .flake8                  # PEP 8 / flake8 configuration
├── pyproject.toml           # Black + isort configuration (modern Python formatting)
├── README.md
├── scripts/
│   ├── hello_dotfiles.py    # Sample clean Python utility (demo + validation target)
│   └── validate-python.sh   # Portable Python syntax + style checker
└── (future: shell/, git/, install.sh, etc.)
```

## Prerequisites

- Bash or compatible shell
- Python 3.8+ (for validation script and sample)
- Git (recommended)

## Installation / Apply Flow

1. Clone the repo:
   ```bash
   git clone https://github.com/dobeutech/dotfiles.git ~/.dotfiles
   cd ~/.dotfiles
   ```

2. (Future) Run bootstrap:
   ```bash
   # ./install.sh   # (to be added in later task)
   ```

3. For Python projects in this repo or your work:
   ```bash
   ./scripts/validate-python.sh path/to/your/code
   ```

## Python PEP 8 Support (pep8-code-reviewer skill)

This repo includes first-class support for clean Python code:

- `.flake8` and `pyproject.toml` for consistent style (black-compatible, 88 char lines)
- `scripts/validate-python.sh` for quick syntax and basic checks
- The **pep8-code-reviewer skill** is active for structured, educational reviews of any Python code added here.

### How to Use

- Run validation: `./scripts/validate-python.sh scripts/`
- For full review: Provide Python code to the pep8-code-reviewer (structured feedback on layout, naming, whitespace, structure, with actionable fixes and strengths highlighted).
- Recommended stack: `black`, `isort`, `flake8` + pre-commit hooks.

See `scripts/hello_dotfiles.py` for a minimal compliant example.

## Adding Personal or Machine-Specific Overrides

- Create `local/` or `private/` (gitignored) for machine-specific configs.
- Never commit secrets, API keys, or personal data.
- Use templates or `.example` files for shared patterns.

## What Should Never Be Committed

- Secrets, tokens, passwords
- Machine-specific paths or IDs
- Large binaries or caches
- Personal SSH keys or credentials

## How to Extend Safely

1. Add new shell config in `shell/` (future)
2. Add scripts with clear purpose and validation
3. For Python: follow the pep8-code-reviewer principles (or run the skill)
4. Update README and progress artifacts
5. Validate before marking complete

## Validation Steps

- Shell scripts: syntax + executable bit
- Python: `./scripts/validate-python.sh` + pep8-code-reviewer review
- No broken references or tracked secrets
- Docs (README + .agent/) in sync with code

## Credits & Philosophy

Built incrementally with agentic discipline, checkpoints, and validation-first approach.
Inspired by strong public dotfiles repos (conservative, documented, lightweight).
Part of Dobeu Tech Solutions ecosystem — helping pick, build, and ship the right tools without the noise.

For questions or contributions: @dobeutech on X or dobeu.tech

---

*This is a living first version. More layers (shell, git, install) coming in subsequent tasks.*