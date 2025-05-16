from pyzotero import zotero
from dotenv import load_dotenv
import os
import re
import shutil
from html import unescape

load_dotenv()

output_dir = os.getenv("OUTPUT_DIR")
def init_dirs():
    os.makedirs(output_dir, exist_ok=True)
    for sub_dir in ['tags', 'journals', 'authors', 'papers', 'collections']:
        if os.path.exists(f"{output_dir}/{sub_dir}"):
            shutil.rmtree(f"{output_dir}/{sub_dir}")
        os.makedirs(f"{output_dir}/{sub_dir}", exist_ok=True)

def safe_filename(filename, replacement=' ', max_length=128):
    """
    将字符串转换为可以作为文件名的格式
    :param filename: 原始字符串
    :param replacement: 非法字符替换为的字符，默认下划线
    :param max_length: 文件名最大长度
    :return: 安全的文件名字符串
    """
    # 定义非法字符（包括Windows和部分Unix非法字符）
    invalid_chars = r'[\\\/\:\*\?\"\<\>\|\n\r\t]'
    # 替换非法字符
    filename = re.sub(invalid_chars, replacement, filename)
    # 文件名长度截断
    if len(filename) > max_length:
        filename = filename[:max_length]
    # 去除首尾空格和点（避免只有空格或点的文件名）
    filename = filename.strip(' .')
    return filename.strip()

def dict_to_markdown(data, coll_dict):
    def get_authors(creators, title):
        if not creators:
            return ""
        result_list = []
        for c in creators:
            if c.get('creatorType') == 'author':
                name = f"{c.get('firstName', '')} {c.get('lastName', '')}".strip()
                open(f"{output_dir}/authors/{name}.md", "a+").write(f"- [[{title}]]\n")
                result_list.append(f'[[{name}]]')
        return ', '.join(result_list)

    def get_tags(tags, title):
        if not tags:
            return ""
        result_list = []
        for tag in tags:
            tag_text = unescape(tag.get('tag', '')).lower()
            tag_text = safe_filename(tag_text)
            open(f"{output_dir}/tags/{tag_text}.md", "a+").write(f"- [[{title}]]\n")
            result_list.append(f'[[{tag_text}]]')
        return ', '.join(result_list)

    try:
        file_url = data['links']['attachment']['href']
        file_url = "zotero://open-pdf/library/items/" + file_url.split("/")[-1]
    except:
        file_url = ""

    d = data.get("data", {})
    full_title = d.get("title", "")
    if not full_title:
        full_title = d.get("shortTitle", "")
    title = safe_filename(full_title)
    authors = get_authors(d.get("creators", []), title)
    journal = d.get("publicationTitle", d.get("journalAbbreviation", ""))
    year = d.get("date", "")[:4]
    volume = d.get("volume", "")
    pages = d.get("pages", "")
    doi = d.get("DOI", "")
    url = d.get("url", "")
    abstract = d.get("abstractNote", "")
    tags = get_tags(d.get("tags", []), title)
    extra = d.get("extra", "")
    language = d.get("language", "")
    collections = d.get("collections", [])
    collections = [coll_dict[c] for c in collections]
    
    open(f"{output_dir}/journals/{safe_filename(journal)}.md", "a+").write(f"[[{title}]]\n")

    md = []
    md.append(f"# {full_title}")
    if authors:
        md.append(f"**Authors:** {authors}")
    if journal:
        md.append(f"**Journal:** [[{journal}]]")
    if file_url:
        md.append(f"**Zotero:** [Open]({file_url})")

    for coll_name  in collections:
        open(f"{output_dir}/collections/{coll_name}.md", "a+").write(f"- [[{title}]]\n")
    collections = [f"[[{coll_name}]]" for coll_name in collections]
    md.append(f"**Collections:** {', '.join(collections)}")

    line = []
    if year:
        line.append(f"**Year:** {year}")
    if volume:
        line.append(f"**Volume:** {volume}")
    if pages:
        line.append(f"**Pages:** {pages}")
    if line:
        md.append(' | '.join(line))
    if doi:
        md.append(f"**DOI:** [{doi}](https://doi.org/{doi})")
    if url:
        md.append(f"**URL:** {url}")
    if tags:
        md.append(f"**Tags:** {tags}")
    if language:
        md.append(f"**Language:** {language}")
    if extra:
        md.append(f"**Extra Info:** {unescape(extra)}")
    if abstract:
        md.append("\n**Abstract:**\n")
        md.append(unescape(abstract))
    res = '\n\n'.join(md)
    open(f"{output_dir}/papers/{title}.md", "w").write(res)


def get_zotero_client():
    library_id = os.getenv("ZOTERO_LIBRARY_ID")
    library_type = os.getenv("ZOTERO_LIBRARY_TYPE", "user")
    api_key = os.getenv("ZOTERO_API_KEY") or None
    local = os.getenv("ZOTERO_LOCAL", "").lower() in ["true", "yes", "1"]
    if local:
        if not library_id:
            # Indicates "current user" for the local API
            library_id = "0"
    elif not all([library_id, api_key]):
        raise ValueError(
            "Missing required environment variables. Please set ZOTERO_LIBRARY_ID and ZOTERO_API_KEY"
        )

    return zotero.Zotero(
        library_id=library_id,
        library_type=library_type,
        api_key=api_key,
        local=local,
    )

if __name__ == "__main__":
    # import json
    zot = get_zotero_client()

    init_dirs()

    collections = zot.collections()
    # json.dump(collections, open(f"collections.json", "w", encoding="utf-8"), indent=4, ensure_ascii=False)

    coll_dict = {}

    for coll_detail in collections:
        coll_id = coll_detail["key"]
        coll_name = coll_detail["data"]["name"]
        coll_name = safe_filename(coll_name)
        coll_dict[coll_id] = coll_name

    for coll_detail in collections:
        coll_id = coll_detail["key"]
        coll_name = coll_detail["data"]["name"]
        coll_name = safe_filename(coll_name)
        open(f"{output_dir}/collections/{coll_name}.md", "w").write(f"# {coll_name}\n")
        parent_coll = coll_detail["data"]["parentCollection"]
        if parent_coll:
            parent_coll_name = coll_dict[parent_coll]
            open(f"{output_dir}/collections/{coll_name}.md", "a+").write(f"## From: [[{parent_coll_name}]]\n")

    all_papers = zot.everything(zot.top())
    # json.dump(all_papers, open(f"all_papers.json", "w", encoding="utf-8"), indent=4, ensure_ascii=False)
    paper_num = len(all_papers)
    for i, paper in enumerate(all_papers):
        print(f'[{i}/{paper_num}]', end='\r')
        if 'title' in paper["data"]:
            dict_to_markdown(paper, coll_dict)
    print(f'all {paper_num} papers processed')
