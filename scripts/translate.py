import os
import sys
import yaml
import re
import google.generativeai as genai

# Konfigurace Gemini (vyžaduje GEMINI_API_KEY v prostředí)
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-3-flash-preview')

def translate_text(text, target_lang="English"):
    if not text or not text.strip():
        return ""
    
    prompt = f"""You are a professional translator. Translate the following Markdown content to {target_lang}. 
    Preserve all Markdown formatting, links, and code blocks. 
    Do not translate the front matter keys, only the values if appropriate. 
    Keep the tone consistent with the original.
    
    CONTENT TO TRANSLATE:
    {text}"""

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"Error during translation: {e}")
        return None

def process_file(file_path):
    if not os.path.exists(file_path):
        print(f"File {file_path} does not exist. Skipping.")
        return

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Rozdělení Front Matter a obsahu
    parts = re.split(r'---', content, maxsplit=2)
    if len(parts) < 3:
        if content.startswith('---'):
            parts = re.split(r'---', content[3:], maxsplit=1)
            if len(parts) >= 2:
                front_matter_raw = parts[0]
                body = parts[1]
            else:
                print(f"Skipping {file_path}: Invalid format.")
                return
        else:
            print(f"Skipping {file_path}: No front matter found.")
            return
    else:
        front_matter_raw = parts[1]
        body = parts[2]

    try:
        front_matter = yaml.safe_load(front_matter_raw)
    except yaml.YAMLError as e:
        print(f"Error parsing YAML in {file_path}: {e}")
        return

    print(f"Translating: {front_matter.get('title', file_path)}...")

    # Překlad názvu
    if 'title' in front_matter:
        translated_title = translate_text(front_matter['title'])
        if translated_title:
            front_matter['title'] = translated_title.strip('" \n')
    
    # Překlad těla
    translated_body = translate_text(body)
    if translated_body is None:
        print(f"Failed to translate body of {file_path}")
        return

    # Sestavení obsahu
    new_content = "---\n"
    new_content += yaml.dump(front_matter, allow_unicode=True, sort_keys=False)
    new_content += "---\n"
    new_content += translated_body

    filename = os.path.basename(file_path)
    output_path = os.path.join("content/en/posts", filename)
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"Successfully saved to: {output_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python scripts/translate.py content/posts/your-article.md")
    else:
        for arg in sys.argv[1:]:
            process_file(arg)
