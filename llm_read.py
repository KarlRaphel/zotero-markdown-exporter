import os
import sqlite3
from pypdf import PdfReader
from dotenv import load_dotenv
import requests

load_dotenv()

api_url = os.getenv("LLM_API_URL")
api_key = os.getenv("LLM_API_KEY")
model = os.getenv("LLM_MODEL")
lang = os.getenv("LLM_LANG")

storage_dir = os.getenv("ZOTERO_STORAGE_DIR")

lang = os.getenv("LLM_LANG", 'zh')

db_path = f'./data/llm_{lang}.db'

prompt = open(f'./prompts/{lang}.txt', 'r').read()


def init_database():
    open(db_path, 'w').close()
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS summary (
                        id TEXT PRIMARY KEY,
                        sum TEXT)
                   '''
    )
    conn.commit()
    conn.close()


def get_response(x):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    data = {
        "model": model,
        "messages": [
            {"role": "user", "content": x},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.4,
        "max_tokens": 16384,
        "top_p": 1,
        "enable_thinking": False,
        "stream": False
   }
    response = requests.post(api_url, headers=headers, json=data)
    response = response.json()
    response = response['choices'][0]['message']['content']
    response = response.strip()
    if "<think>" in response:
        response = response.split('</think>')[-1]
    return response


def get_paper_text(id):
    paper_text = ""
    paper_dir = f"{storage_dir}/{id}"
    files = os.listdir(paper_dir)
    pdf_files = [f for f in files if f.endswith(".pdf")]
    try:
        if len(pdf_files) > 0:
            pdf_file = pdf_files[0]
            pdf_file = f"{paper_dir}/{pdf_file}"
            reader = PdfReader(pdf_file)
            for page in reader.pages:
                paper_text += page.extract_text()
            return paper_text
        html_files = [f for f in files if f.endswith(".html")]
        if len(html_files) > 0:
            html_file = html_files[0]
            html_file = f"{paper_dir}/{html_file}"
            with open(html_file, 'r', encoding='utf-8') as f:
                paper_text = f.read()
            return paper_text
        return ""
    except:
        return ""



class LLMReader:
    def __init__(self):
        if not os.path.exists(db_path):
            init_database()
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
    
    def get_summary(self, id):
        self.cursor.execute(f"SELECT * FROM summary WHERE id = '{id}'")
        result = self.cursor.fetchone()
        if result:
            return result[1]
        else:
            paper_text = get_paper_text(id)
            if len(paper_text) == 0:
                return ""
            summary = get_response(paper_text)
            self.cursor.execute("INSERT INTO summary VALUES (?, ?)", (id, summary))
            self.conn.commit()
            return summary


if __name__ == '__main__':
    reader = LLMReader()
    print(reader.get_summary("ABCDEFG"))