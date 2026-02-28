import os
import glob
import re

base_dir = r"C:\Users\Zonia\Desktop\JB Woodworks"
html_files = glob.glob(os.path.join(base_dir, "*.html"))

for file in html_files:
    filename = os.path.basename(file)
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    is_index = (filename == "index.html")
    
    home_link = "" if is_index else "/"
    portfolio_link = "/portfolio" # In vercel, with clean urls, /portfolio points to portfolio.html
    logo_link = "#" if is_index else "/"

    nav_inner = f"""<div class="nav-inner">
            <a href="{logo_link}" class="nav-logo">
                <span class="nav-logo-text">JB <span class="nav-logo-sub">WOODWORKS</span></span>
            </a>
            <ul class="nav-links">
                <li><a href="{home_link}#services">Services</a></li>
                <li><a href="{portfolio_link}">Portfolio</a></li>
                <li><a href="{home_link}#faq">FAQ</a></li>
                <li><a href="{home_link}#contact">Contact Us</a></li>
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
            <a href="{home_link}#contact" class="btn btn-nav">Get a Quote</a>
            <button class="nav-hamburger" id="hamburger" aria-label="Toggle menu">
                <span></span><span></span><span></span>
            </button>
        </div>
    </nav>"""

    mobile_menu = f"""<!-- MOBILE MENU -->
    <div class="mobile-menu" id="mobileMenu">
        <ul>
            <li><a href="{home_link}#services" class="mob-link">Services</a></li>
            <li><a href="{portfolio_link}" class="mob-link">Portfolio</a></li>
            <li><a href="{home_link}#faq" class="mob-link">FAQ</a></li>
            <li><a href="https://www.instagram.com/jb.woodworkss" target="_blank" rel="noopener" class="mob-link">Instagram</a></li>
            <li><a href="https://www.facebook.com/people/JB-Woodworks/61581118061434" target="_blank" rel="noopener" class="mob-link">Facebook</a></li>
            <li><a href="https://www.tiktok.com/@jbwoodworks_" target="_blank" rel="noopener" class="mob-link">TikTok</a></li>
            <li><a href="https://x.com/jbwoodworks8" target="_blank" rel="noopener" class="mob-link">Twitter</a></li>
            <li><a href="{home_link}#contact" class="btn btn-primary mob-link">Get a Quote</a></li>
        </ul>
    </div>"""

    footer = f"""<!-- FOOTER -->
    <footer class="site-footer">
        <div class="container">
            <div class="footer-inner">
                <div class="footer-brand">
                    <div class="footer-logo-wrap">
                        <div>
                            <a href="{logo_link}" class="footer-logo">JB</a>
                            <p class="footer-tagline">WOODWORKS</p>
                        </div>
                    </div>
                    <p>Premium custom woodworking and construction.</p>
                </div>
                <div class="footer-links-col">
                    <h4>Company</h4>
                    <ul>
                        <li><a href="{home_link}#services">Services</a></li>
                        <li><a href="{portfolio_link}">Portfolio</a></li>
                        <li><a href="{home_link}#faq">FAQ</a></li>
                    </ul>
                </div>
                <div class="footer-links-col">
                    <h4>Contact</h4>
                    <ul>
                        <li><a href="{home_link}#contact">Get a Quote</a></li>
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
                    <a href="/privacy">Privacy Policy</a>
                    <a href="/terms">Terms of Service</a>
                </div>
            </div>
        </div>
    </footer>"""

    # Replacements
    content = re.sub(r'<div class="nav-inner">.*?</nav>', nav_inner, content, flags=re.DOTALL)
    content = re.sub(r'<!-- MOBILE MENU -->.*?</div>', mobile_menu, content, flags=re.DOTALL)
    content = re.sub(r'<!-- FOOTER -->.*?</footer>', footer, content, flags=re.DOTALL)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {filename}")
