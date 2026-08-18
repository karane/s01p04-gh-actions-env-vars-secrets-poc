# s01p04-gh-actions-env-vars-secrets-poc

`env:` at workflow/job/step level, the `secrets:` and `vars:` contexts, `GITHUB_ENV`/`GITHUB_OUTPUT`/`GITHUB_PATH` files, and masking secrets with `::add-mask::`.

## Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Run tests

```bash
python3 -m pytest tests/ -v
```

## Run the workflow

Push to `main` or open a PR — `.github/workflows/env-vars-secrets.yml` runs and prints each layer of env resolution to the job logs. Optionally set a repository variable `DEPLOY_TARGET` and secret `API_KEY` to see `vars:`/`secrets:` populated instead of falling back to defaults.

See [BLOG.md](./BLOG.md) for a full walkthrough.
