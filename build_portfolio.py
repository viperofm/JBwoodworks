import os
import re

base_dir = r"C:\Users\Zonia\Desktop\JB Woodworks\Jah Images"
directories = [d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d))]

# Reusable header derived directly from index.html (Sync)
nav_html = """
    <!-- NAV -->
    <nav id="navbar" class="scrolled">
        <div class="nav-inner">
            <a href="index.html" class="nav-logo">
                <span class="nav-logo-text">JB <span class="nav-logo-sub">WOODWORKS</span></span>
            </a>
            <ul class="nav-links">
                <li><a href="index.html#services">Services</a></li>
                <li><a href="portfolio.html">Portfolio</a></li>
                <li><a href="index.html#faq">FAQ</a></li>
                <li><a href="index.html#contact">Contact Us</a></li>
            </ul>
            <div class="nav-socials" style="display: flex; gap: 12px; align-items: center;">
                <a href="https://www.instagram.com/jb.woodworkss" target="_blank" rel="noopener" class="nav-instagram" title="Instagram">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect>
                        <path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path>
                        <line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line>
                    </svg>
                    <span>Follow Us</span>
                </a>
            </div>
            <a href="index.html#contact" class="btn btn-nav">Get a Quote</a>
            <button class="nav-hamburger" id="hamburger" aria-label="Toggle menu">
                <span></span><span></span><span></span>
            </button>
        </div>
    </nav>

    <!-- MOBILE MENU -->
    <div class="mobile-menu" id="mobileMenu">
        <ul>
            <li><a href="index.html#services" class="mob-link">Services</a></li>
            <li><a href="portfolio.html" class="mob-link">Portfolio</a></li>
            <li><a href="index.html#faq" class="mob-link">FAQ</a></li>
            <li><a href="https://www.instagram.com/jb.woodworkss" target="_blank" rel="noopener" class="mob-link">Instagram</a></li>
            <li><a href="https://www.facebook.com/people/JB-Woodworks/61581118061434" target="_blank" rel="noopener" class="mob-link">Facebook</a></li>
            <li><a href="https://www.tiktok.com/@jbwoodworks_" target="_blank" rel="noopener" class="mob-link">TikTok</a></li>
            <li><a href="https://x.com/jbwoodworks8" target="_blank" rel="noopener" class="mob-link">Twitter</a></li>
            <li><a href="index.html#contact" class="btn btn-primary mob-link">Get a Quote</a></li>
        </ul>
    </div>
"""

def generate_header(title, is_project=False):
    back_btn = ""
    if is_project:
        back_btn = '<a href="portfolio.html" class="btn btn-ghost" style="margin-top: 20px; display:inline-block;">&larr; Back to Portfolio</a>'
        header_text = f'<h1 class="hero-headline" style="font-size: 3.5rem; margin-top:20px;">Project: <em>{title}</em></h1>'
    else:
        back_btn = '<a href="index.html" class="btn btn-ghost" style="margin-top: 20px; display:inline-block;">&larr; Back to Main Page</a>'
        header_text = '<h1 class="hero-headline" style="font-size: 3.5rem; margin-top:20px;">Full <em>Portfolio</em></h1>'

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>{title} | JB Woodworks</title>
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=DM+Serif+Display:ital@0;1&display=swap" rel="stylesheet" />
    <link rel="stylesheet" href="style.css" />
    <style>
        .portfolio-header {{ padding-top: 150px; padding-bottom: 40px; text-align: center; background: var(--black-2); }}
        .portfolio-tabs {{ display: flex; flex-wrap: wrap; justify-content: center; gap: 15px; padding: 20px; background: var(--black-1); border-bottom: 1px solid var(--border); }}
        .tab-btn {{ background: transparent; color: var(--white-50); border: 1px solid var(--border); padding: 10px 20px; border-radius: 30px; cursor: pointer; font-family: 'Inter', sans-serif; font-size: 0.9rem; transition: all 0.3s ease; }}
        .tab-btn:hover {{ color: var(--white); border-color: var(--gold); }}
        .tab-btn.active {{ background: var(--gold); color: var(--black); border-color: var(--gold); font-weight: 600; }}
        .portfolio-grid-container {{ padding: 60px 0; background: var(--black-2); }}
        .portfolio-item {{ display: none; }}
        .portfolio-item.show {{ display: block; animation: fadeIn 0.5s ease; }}
        
        .gallery-grid-container {{ padding: 60px 0; background: var(--black-2); }}
        .gallery-item {{ width: 100%; border-radius: var(--radius-lg); overflow: hidden; border: 1px solid var(--border); background: var(--black-3); display: flex; align-items: center; justify-content: center; margin-bottom: 30px; }}
        .gallery-item img, .gallery-item video {{ width: 100%; height: auto; max-height: 80vh; object-fit: contain; }}
        
        @keyframes fadeIn {{ from {{ opacity: 0; transform: translateY(10px); }} to {{ opacity: 1; transform: translateY(0); }} }}
    </style>
</head>
<body>
{nav_html}
    <!-- HEADER -->
    <section class="portfolio-header">
        <div class="container">
            <span class="section-tag">Our Masterpieces</span>
            {header_text}
            {back_btn}
        </div>
    </section>
"""

footer_html = """
    <div style="text-align: center; padding: 60px; background: var(--black-1);">
        <a href="index.html#contact" class="btn btn-primary btn-large">Start Your Custom Project</a>
    </div>
    <!-- FOOTER -->
    <footer class="site-footer">
        <div class="container">
            <div class="footer-inner">
                <div class="footer-brand">
                    <div class="footer-logo-wrap">
                        <div>
                            <a href="index.html" class="footer-logo">JB</a>
                            <p class="footer-tagline">WOODWORKS</p>
                        </div>
                    </div>
                    <p>Premium custom woodworking and construction.</p>
                </div>
                <div class="footer-links-col">
                    <h4>Company</h4>
                    <ul>
                        <li><a href="index.html#services">Services</a></li>
                        <li><a href="portfolio.html">Portfolio</a></li>
                        <li><a href="index.html#faq">FAQ</a></li>
                    </ul>
                </div>
                <div class="footer-links-col">
                    <h4>Contact</h4>
                    <ul>
                        <li><a href="index.html#contact">Get a Quote</a></li>
                        <li><a href="mailto:jbwoodworks8@gmail.com">jbwoodworks8@gmail.com</a></li>
                        <li style="margin-top: 15px;"><a href="https://www.instagram.com/jb.woodworkss" target="_blank" rel="noopener">Instagram</a></li>
                        <li><a href="https://www.facebook.com/people/JB-Woodworks/61581118061434" target="_blank" rel="noopener">Facebook</a></li>
                        <li><a href="https://www.tiktok.com/@jbwoodworks_" target="_blank" rel="noopener">TikTok</a></li>
                        <li><a href="https://x.com/jbwoodworks8" target="_blank" rel="noopener">Twitter</a></li>
                    </ul>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2026 JB Woodworks. All rights reserved.</p>
                <div class="footer-legal-links">
                    <a href="privacy.html">Privacy Policy</a>
                    <a href="terms.html">Terms of Service</a>
                </div>
            </div>
        </div>
    </footer>
    <script src="script.js"></script>
    <script>
        document.getElementById('navbar').classList.add('scrolled');
    </script>
</body>
</html>
"""

# Categorize images by logic into structured projects
projects = {}

for d in directories:
    dir_path = os.path.join(base_dir, d)
    files_raw = [f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f))]
    # Filter out HEIC immediately to prevent any broken images throughout the site
    files = [f for f in files_raw if not f.lower().endswith('.heic')]
    
    if not files:
        continue
        
    if d == "Custom Pool Table":
        # Group by prefix 732 vs 733 into two separate projects
        p1 = []
        p2 = []
        for f in files:
            if "732" in f: p1.append((d, f))
            else: p2.append((d, f))
        if p1: projects["Custom Pool Table (A)"] = {"files": p1, "cat": "Custom Pool Table"}
        if p2: projects["Custom Pool Table (B)"] = {"files": p2, "cat": "Custom Pool Table"}
            
    elif d == "Custom Furniture":
        # Group by prefix IMG_11 vs IMG_12/UUID
        p1 = []
        p2 = []
        for f in files:
            if "IMG_11" in f: p1.append((d, f))
            else: p2.append((d, f))
        if p1: projects["Custom Furniture (A)"] = {"files": p1, "cat": "Custom Furniture"}
        if p2: projects["Custom Furniture (B)"] = {"files": p2, "cat": "Custom Furniture"}
        
    elif d == "Pergola":
        # Group by prefix IMG_00 vs IMG_18/19
        p1 = []
        p2 = []
        for f in files:
            if "IMG_00" in f: p1.append((d, f))
            else: p2.append((d, f))
        if p1: projects["Pergola (A)"] = {"files": p1, "cat": "Pergola"}
        if p2: projects["Pergola (B)"] = {"files": p2, "cat": "Pergola"}
        
    else:
        if d not in projects:
            projects[d] = {"files": [], "cat": d}
        projects[d]["files"].extend([(d, f) for f in files])

# Handcrafted family-oriented descriptions for each individual project
project_descriptions = {
    "Custom Pool Table (A)": "The client was absolutely thrilled with this custom handcrafted pool table. Built with precision and a loving attention to detail, it serves as the perfect centerpiece for their family's game night gatherings.",
    "Custom Pool Table (B)": "We designed this stunning pool table from scratch to fit perfectly within the home's aesthetics. The family was overjoyed with the final result, providing a robust and elegant space for evening entertainment.",
    "Custom Furniture (A)": "This custom furniture piece was built entirely out of premium lumber to exceed the client's expectations. Knowing it will be part of the family's daily life, we focused on making it both gorgeous and highly durable.",
    "Custom Furniture (B)": "Hand-crafted to match the specific vision of the homeowners, this unique piece effortlessly blending style with everyday functionality. The clients loved the seamless finish and sturdy construction.",
    "Boat Dock": "A massive masterclass in waterfront construction. The client's family can now safely enjoy their lakefront property year-round. This heavily reinforced boat dock provides easy access while perfectly complementing the beautiful outdoor views.",
    "Deck": "Creating a beautiful transition from the indoors to the outdoors! We built this gorgeous deck to give the family an incredible outdoor living space for weekend barbecues and relaxing evenings under the stars. The clients were incredibly happy with the structural quality.",
    "Pergola (A)": "The perfect balance of shade and outdoor comfort. The family wanted a dedicated space to host friends and relax safely out of the intense sun. We custom-built this stunning pergola (Part 1), ensuring the clients had a beautiful and sturdy structure.",
    "Pergola (B)": "Continuing our work on custom outdoor shade structures, this beautiful pergola offers an elegant retreat in the backyard. Perfect for relaxing and enjoying the fresh breeze year-round.",
    "Trex Deck": "Using top-of-the-line Trex decking materials, we created an absolutely massive, maintenance-free outdoor living expansion. The clients were stunned at the transformation. It is the perfect, safe environment for kids to play and parents to entertain without worry of splinters or rotting."
}

# ----- BUILD INDIVIDUAL PROJECT SUBPAGES -----
for proj_name, data in projects.items():
    safe_name = proj_name.replace(" ", "_").replace("(", "").replace(")", "").lower()
    html_content = generate_header(proj_name, is_project=True)
    
    desc_text = project_descriptions.get(proj_name, "Our clients were absolutely thrilled with the results of this custom project. Built with precision and care, it provides a beautiful and functional addition to their family home.")
    
    html_content += f'''<div class="gallery-grid-container"><div class="container">\n'''
    html_content += f'''    <div style="background: var(--black-1); padding: 30px; border-radius: var(--radius-md); border-left: 4px solid var(--gold); margin-bottom: 40px;">\n'''
    html_content += f'''        <p style="font-size: 1.1rem; line-height: 1.7; color: var(--white-80); margin: 0;">{desc_text}</p>\n'''
    html_content += f'''    </div>\n'''
    html_content += '''    <div class="gallery-grid" style="column-count: 1; gap: 30px;">\n'''
    
    for folder, f in data["files"]:
        clean_ext = f.lower()
        if clean_ext.endswith('.mov') or clean_ext.endswith('.mp4'):
            html_content += f'''
            <div class="gallery-item fade-in-up">
                <video autoplay loop muted playsinline controls>
                    <source src="Jah Images/{folder}/{f}" type="video/mp4">
                </video>
            </div>
            '''
        else:
            html_content += f'''
            <div class="gallery-item fade-in-up">
                <img src="Jah Images/{folder}/{f}" alt="{proj_name} Picture">
            </div>
            '''
            
    html_content += '''</div></div></div>\n'''
    html_content += footer_html
    
    with open(rf"C:\Users\Zonia\Desktop\JB Woodworks\project_{safe_name}.html", "w", encoding="utf-8") as f:
        f.write(html_content)

# ----- BUILD MASTER PORTFOLIO PORTAL -----
portfolio_html = generate_header("Portfolio")
portfolio_html += '''
    <div class="portfolio-tabs">
        <button class="tab-btn active" onclick="filterSelection('all')">All Projects</button>
'''
# Add tabs based on unique categories
unique_cats = sorted(list(set([p["cat"] for p in projects.values()])))
for c in unique_cats:
    portfolio_html += f'''        <button class="tab-btn" onclick="filterSelection('{c.replace(" ", "")}')">{c}</button>\n'''

# Add requested empty static tabs
portfolio_html += f'''        <button class="tab-btn" onclick="filterSelection('Staining')">Staining</button>\n'''
portfolio_html += f'''        <button class="tab-btn" onclick="filterSelection('Paving')">Paving</button>\n'''

portfolio_html += '''    </div>\n    <div class="portfolio-grid-container">\n        <div class="container">\n            <div class="portfolio-grid">\n'''

# Generate EXACTLY ONE card per dictionary item (8 total)
for proj_name, data in projects.items():
    safe_name = proj_name.replace(" ", "_").replace("(", "").replace(")", "").lower()
    cat_class = data["cat"].replace(" ", "")
    
    # Pick the first file to act as the cover thumbnail
    cover = ""
    cover_dir = ""
    for folder, f in data["files"]:
        cover = f
        cover_dir = folder
        break
        
    cover_ext = cover.lower()
    
    # Wrap entire card in an Anchor tag, REMOVE display: block inline to let .show class handle filtering!
    portfolio_html += f'''<a href="project_{safe_name}.html" style="text-decoration: none; color: inherit;" class="portfolio-item {cat_class}">'''
    
    if cover_ext.endswith('.mov') or cover_ext.endswith('.mp4'):
        portfolio_html += f'''
            <div class="portfolio-card">
                <video class="portfolio-image" style="width: 100%; height: 280px; object-fit: cover; background: #000;" autoplay loop muted playsinline>
                    <source src="Jah Images/{cover_dir}/{cover}" type="video/mp4">
                </video>
                <div class="portfolio-content">
                    <h3>{proj_name}</h3>
                    <p class="portfolio-desc">View all {len(data["files"])} photos/videos &rarr;</p>
                </div>
            </div>
        </a>
        '''
    else:
        portfolio_html += f'''
            <div class="portfolio-card">
                <div class="portfolio-image" style="background-image: url('Jah Images/{cover_dir}/{cover}');"></div>
                <div class="portfolio-content">
                    <h3>{proj_name}</h3>
                    <p class="portfolio-desc">View all {len(data["files"])} photos/videos &rarr;</p>
                </div>
            </div>
        </a>
        '''

portfolio_html += '''            </div>\n        </div>\n    </div>'''

# Inject the filter logic script before footer closing
footer_with_filter = footer_html.replace('</body>', '''
    <script>
        function filterSelection(c) {
            var x, i;
            x = document.getElementsByClassName("portfolio-item");
            if (c == "all") c = "";
            for (i = 0; i < x.length; i++) {
                w3RemoveClass(x[i], "show");
                if (x[i].className.indexOf(c) > -1) w3AddClass(x[i], "show");
            }
            var btns = document.getElementsByClassName("tab-btn");
            for (var i = 0; i < btns.length; i++) {
                btns[i].className = btns[i].className.replace(" active", "");
                if(c == "" && btns[i].innerHTML == "All Projects") {
                    btns[i].className += " active";
                } else if(btns[i].innerHTML.replace(/ /g, "") == c) {
                    btns[i].className += " active";
                }
            }
        }
        function w3AddClass(element, name) {
            var i, arr1, arr2;
            arr1 = element.className.split(" ");
            arr2 = name.split(" ");
            for (i = 0; i < arr2.length; i++) {
                if (arr1.indexOf(arr2[i]) == -1) {element.className += " " + arr2[i];}
            }
        }
        function w3RemoveClass(element, name) {
            var i, arr1, arr2;
            arr1 = element.className.split(" ");
            arr2 = name.split(" ");
            for (i = 0; i < arr2.length; i++) {
                while (arr1.indexOf(arr2[i]) > -1) { arr1.splice(arr1.indexOf(arr2[i]), 1); }
            }
            element.className = arr1.join(" ");
        }
        filterSelection("all");
    </script>
</body>''')

portfolio_html += footer_with_filter

with open(r"C:\Users\Zonia\Desktop\JB Woodworks\portfolio.html", "w", encoding="utf-8") as f:
    f.write(portfolio_html)

print("Generated portfolio.html and Individual Project Pages seamlessly.")
