import os
import shutil
import re

base_dir = r"C:\Users\Zonia\Desktop\JB Woodworks"

# 1. Deduplicate pool table b
pool_b_path = os.path.join(base_dir, "project_custom_pool_table_b.html")
with open(pool_b_path, "r", encoding="utf-8") as f:
    content = f.read()

# remove elements with (1).jpg
content = re.sub(r'<div class="gallery-item fade-in-up">\s*<img src="[^"]*\(1\)\.jpg"\s*alt="[^"]*">\s*</div>', '', content)
with open(pool_b_path, "w", encoding="utf-8") as f:
    f.write(content)
print("Removed duplicates from Pool Table B")

# 2. Merge Custom Furniture
# We will use project_custom_furniture_a.html as base and rename it to project_custom_furniture.html
furn_a_path = os.path.join(base_dir, "project_custom_furniture_a.html")
furn_b_path = os.path.join(base_dir, "project_custom_furniture_b.html")
furn_merged_path = os.path.join(base_dir, "project_custom_furniture.html")

with open(furn_a_path, "r", encoding="utf-8") as f:
    furn_a = f.read()
with open(furn_b_path, "r", encoding="utf-8") as f:
    furn_b = f.read()

# extract gallery items from B
match_b = re.search(r'<div class="gallery-grid" style="column-count: 1; gap: 30px;">(.*?)</div></div></div>', furn_b, re.DOTALL)
if match_b:
    items_b = match_b.group(1).strip()
    # insert items into A
    furn_merged = re.sub(r'(<div class="gallery-grid" style="column-count: 1; gap: 30px;">.*?)(</div>\s*</div>\s*</div>)', r'\1\n' + items_b + r'\n\2', furn_a, flags=re.DOTALL)
    # Fix the title
    furn_merged = furn_merged.replace("Custom Furniture (A)", "Custom Furniture")
    with open(furn_merged_path, "w", encoding="utf-8") as f:
        f.write(furn_merged)
    print("Merged Custom Furniture into project_custom_furniture.html")
    
    # Clean up old files safely
    try:
        os.remove(furn_a_path)
        os.remove(furn_b_path)
    except:
        pass


# 3. Split Pergola
pergola_path = os.path.join(base_dir, "project_pergola.html")
pergola_a_path = os.path.join(base_dir, "project_pergola_a.html")
pergola_b_path = os.path.join(base_dir, "project_pergola_b.html")

with open(pergola_path, "r", encoding="utf-8") as f:
    pergola = f.read()

# The first two videos are IMG_0047 and IMG_0050. The other two are IMG_1866 and IMG_1943.
items = re.findall(r'<div class="gallery-item fade-in-up">.*?</div>', pergola, re.DOTALL)

if len(items) >= 4:
    pergola_a_items = "\n".join(items[:2])
    pergola_b_items = "\n".join(items[2:])
    
    pergola_a = re.sub(r'<div class="gallery-grid" style="column-count: 1; gap: 30px;">(.*?)</div></div></div>', r'<div class="gallery-grid" style="column-count: 1; gap: 30px;">\n' + pergola_a_items + r'\n</div></div></div>', pergola, flags=re.DOTALL)
    pergola_a = pergola_a.replace("Project: <em>Pergola</em>", "Project: <em>Pergola 1</em>")
    pergola_a = pergola_a.replace("<title>Pergola | JB Woodworks</title>", "<title>Pergola 1 | JB Woodworks</title>")
    with open(pergola_a_path, "w", encoding="utf-8") as f:
        f.write(pergola_a)
        
    pergola_b = re.sub(r'<div class="gallery-grid" style="column-count: 1; gap: 30px;">(.*?)</div></div></div>', r'<div class="gallery-grid" style="column-count: 1; gap: 30px;">\n' + pergola_b_items + r'\n</div></div></div>', pergola, flags=re.DOTALL)
    pergola_b = pergola_b.replace("Project: <em>Pergola</em>", "Project: <em>Pergola 2</em>")
    pergola_b = pergola_b.replace("<title>Pergola | JB Woodworks</title>", "<title>Pergola 2 | JB Woodworks</title>")
    with open(pergola_b_path, "w", encoding="utf-8") as f:
        f.write(pergola_b)
        
    print("Split Pergola into A and B")
    try:
        os.remove(pergola_path)
    except:
        pass

# Now update portfolio.html references!
portfolio_path = os.path.join(base_dir, "portfolio.html")
with open(portfolio_path, "r", encoding="utf-8") as f:
    port = f.read()

# 1. Furniture
port = port.replace("project_custom_furniture_a.html", "project_custom_furniture.html")
port = port.replace("Custom Furniture (A)", "Custom Furniture")
# Remove furniture B
port = re.sub(r'<a href="project_custom_furniture_b\.html".*?</a>', '', port, flags=re.DOTALL)

# 2. Pergola 
# Duplicate the pergola block and rename
pergola_match = re.search(r'<a href="project_pergola\.html" class="portfolio-card filter-item pergola".*?</a>', port, re.DOTALL)
if pergola_match:
    perg_block = pergola_match.group(0)
    perg_1 = perg_block.replace("project_pergola.html", "project_pergola_a.html")
    perg_1 = perg_1.replace("Pergola</h3>", "Pergola 1</h3>")
    
    perg_2 = perg_block.replace("project_pergola.html", "project_pergola_b.html")
    perg_2 = perg_2.replace("Pergola</h3>", "Pergola 2</h3>")
    perg_2 = perg_2.replace("IMG_1943.jpg", "IMG_1866.mp4") # Maybe adjust cover image if possible, but fine as is or change later
    
    port = port.replace(perg_block, perg_1 + "\n" + perg_2)

with open(portfolio_path, "w", encoding="utf-8") as f:
    f.write(port)
print("Updated portfolio.html")
