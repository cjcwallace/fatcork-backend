# fatcork-backend

1. Create .venv: `python -m venv .venv`
2. activate: gitbash = `source .venv/Scripts/activate` or **nix = `source .venv/bin/activate`

## Layout

├── fatcork-backend  => github repo folder
│   ├── fatcorkbackend => main django project folder
│   │   ├── inventory => app folder
│   │   ├── scripts => test scripts, some moved to inventory/management/commands folder
├── credentials.py
└── manage.py


eventually, use `git mv` to move the nested django files out of `fatcorkbackend` into `fatcork-backend`
