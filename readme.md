# Sample Project

A minimal Python project template.

## How to run

```bash
python -m venv .venv
source .venv/bin/activate   # Windows なら .venv\Scripts\activate
pip install -r requirements.txt
python src/main.py
```
```

### `.gitignore`

```
# Python bytecode
__pycache__/
*.py[cod]

# Virtual environment
.venv/

# PyInstaller output
dist/
build/
```

## ステップ 3: 仮想環境を作成し、依存関係をインストール

```bash
python -m venv .venv          # 仮想環境を作成
source .venv/bin/activate    # Windows: .venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt   # 依存関係があればここでインストール
```

## ステップ 4: `src/main.py` を実行

```bash
python src/main.py
```

出力例  
```
Hello from the Python project!
```

---

### 補足：VS Code の設定（任意）

`.vscode/settings.json` に以下を追加すると、VS Code が自動で仮想環境を認識します。

```json
{
    "python.defaultInterpreterPath": "${workspaceFolder}/.venv/bin/python"
}