# 📝 タスク管理アプリ (Task Manager)

このリポジトリは、シンプルな **タスク管理アプリ** のソースコードです。  
Flask と SQLite を使った Web アプリで、以下の機能があります。

---

## ⚙️ 機能

- ✅ タスクの追加・削除
- 🚨 締切管理（3日以内は赤色で表示）
- 🔄 完了/未完了の切り替え
- 🎨 Bootstrap による美しい UI
- 📱 レスポンシブデザイン

---

## 🖥️ 動作環境

- Python 3.x
- Flask
- SQLite（ローカルに `tasks.db` が作成されます）

---

## 🚀 セットアップ手順

### Windows
```bash
# 1. 仮想環境作成・有効化
python -m venv venv
venv\Scripts\activate

# 2. Flask インストール
pip install flask

# 3. アプリ起動
python app.py

# 4. ブラウザでアクセス
# http://localhost:5000
```

### Windows
```bash
# 1. 仮想環境作成・有効化
python3 -m venv venv
source venv/bin/activate

# 2. Flask インストール
pip install flask

# 3. アプリ起動
python app.py

# 4. ブラウザでアクセス
# http://localhost:5000
```

---

## 📂 ディレクトリ構成

```
task-manager/
├── app.py              
├── templates/
│   └── index.html      
├── tasks.db            # SQLite データベース（初回起動時に作成）
├── requirements.txt    
└── README.md
```

---

## 🎯 使い方

1. **タスクの追加**
   - タイトル、説明、締切日を入力して「追加」ボタンをクリック

2. **タスクの管理**
   - 「完了」ボタンでタスクを完了状態に変更
   - 「削除」ボタンでタスクを削除

3. **締切の確認**
   - 3日以内の締切があるタスクは🚨マークと赤色背景で表示

---

## 📦 requirements.txt（推奨）

```txt
Flask==2.3.3
```

---

## 🔧 カスタマイズ

- `templates/index.html` - UI デザインの変更
- `app.py` - 機能の追加・変更
- CSS スタイルは `index.html` の `<style>` セクションで編集


## 🚀 Google Colab での実行

このアプリは Google Colab でも実行できます。詳細は以下を参照してください：

1. ngrok アカウントの作成とトークン取得
2. 必要なライブラリのインストール（flask, pyngrok）
3. ngrok を使用した外部アクセスの設定

---
