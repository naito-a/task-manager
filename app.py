from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import datetime, timedelta
import os
import traceback

app = Flask(__name__)

# データベース初期化
def init_db():
    try:
        conn = sqlite3.connect('tasks.db')
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT,
                deadline DATE,
                completed BOOLEAN DEFAULT 0,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        conn.commit()
        conn.close()
        print("✅ データベース初期化完了")
    except Exception as e:
        print(f"❌ データベース初期化エラー: {e}")
        traceback.print_exc()

# タスク一覧取得
def get_tasks():
    try:
        conn = sqlite3.connect('tasks.db')
        cursor = conn.cursor()
        cursor.execute('''
            SELECT id, title, description, deadline, completed, created_at
            FROM tasks
            ORDER BY deadline ASC, created_at DESC
        ''')
        tasks = cursor.fetchall()
        conn.close()

        task_list = []
        today = datetime.now().date()

        for task in tasks:
            task_dict = {
                'id': task[0],
                'title': task[1],
                'description': task[2],
                'deadline': task[3],
                'completed': task[4],
                'created_at': task[5],
                'is_urgent': False
            }

            if task[3]:  # 締切がある場合
                try:
                    deadline = datetime.strptime(task[3], '%Y-%m-%d').date()
                    days_left = (deadline - today).days
                    if 0 <= days_left <= 3:  # 3日以内
                        task_dict['is_urgent'] = True
                except:
                    pass  # 日付フォーマットエラーは無視

            task_list.append(task_dict)

        return task_list
    except Exception as e:
        print(f"❌ タスク取得エラー: {e}")
        traceback.print_exc()
        return []

@app.route('/')
def index():
    try:
        tasks = get_tasks()
        return render_template('index.html', tasks=tasks)
    except Exception as e:
        print(f"❌ インデックスページエラー: {e}")
        traceback.print_exc()
        return f"<h1>エラーが発生しました</h1><p>{str(e)}</p>", 500

@app.route('/add_task', methods=['POST'])
def add_task():
    try:
        title = request.form.get('title', '')
        description = request.form.get('description', '')
        deadline = request.form.get('deadline', '')

        if not title:
            return redirect(url_for('index'))

        if not deadline:
            deadline = None

        conn = sqlite3.connect('tasks.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO tasks (title, description, deadline)
            VALUES (?, ?, ?)
        ''', (title, description, deadline))
        conn.commit()
        conn.close()

        return redirect(url_for('index'))
    except Exception as e:
        print(f"❌ タスク追加エラー: {e}")
        traceback.print_exc()
        return redirect(url_for('index'))

@app.route('/delete_task/<int:task_id>')
def delete_task(task_id):
    try:
        conn = sqlite3.connect('tasks.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
        conn.commit()
        conn.close()

        return redirect(url_for('index'))
    except Exception as e:
        print(f"❌ タスク削除エラー: {e}")
        traceback.print_exc()
        return redirect(url_for('index'))

@app.route('/toggle_task/<int:task_id>')
def toggle_task(task_id):
    try:
        conn = sqlite3.connect('tasks.db')
        cursor = conn.cursor()
        cursor.execute('UPDATE tasks SET completed = NOT completed WHERE id = ?', (task_id,))
        conn.commit()
        conn.close()

        return redirect(url_for('index'))
    except Exception as e:
        print(f"❌ タスク切り替えエラー: {e}")
        traceback.print_exc()
        return redirect(url_for('index'))

# デバッグ用ルート
@app.route('/debug')
def debug():
    try:
        import sys
        import platform

        debug_info = f"""
        <h2>デバッグ情報</h2>
        <ul>
        <li>Python version: {sys.version}</li>
        <li>Platform: {platform.platform()}</li>
        <li>Working directory: {os.getcwd()}</li>
        <li>Files in directory: {os.listdir('.')}</li>
        <li>Templates directory exists: {os.path.exists('templates')}</li>
        <li>Template file exists: {os.path.exists('templates/index.html')}</li>
        </ul>
        <h3>タスク一覧</h3>
        <p>タスク数: {len(get_tasks())}</p>
        <a href="/">メインページに戻る</a>
        """
        return debug_info
    except Exception as e:
        return f"デバッグエラー: {str(e)}"

if __name__ == '__main__':
    print("🚀 アプリケーション開始")
    init_db()
    app.run(host='0.0.0.0', port=5000, debug=True)
