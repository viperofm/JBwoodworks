import re

file_path = r"C:\Users\Zonia\Desktop\JB Woodworks\style.css"
with open(file_path, "r", encoding="utf-8") as f:
    css = f.read()

# Replace Hero BG
hero_new = """
.hero-slider {
  position: absolute;
  inset: 0;
  overflow: hidden;
  z-index: 0;
}

.hero-slide {
  position: absolute;
  inset: 0;
  background-size: cover;
  background-position: center;
  opacity: 0;
  transition: opacity 1.5s ease-in-out, transform 8s ease-out;
  transform: scale(1.05);
}

.hero-slide.active {
  opacity: 1;
  transform: scale(1);
}

.hero-overlay {
  position: absolute;
  inset: 0;
  background: linear-gradient(to right, rgba(8,8,8,0.95) 0%, rgba(8,8,8,0.7) 40%, rgba(8,8,8,0.3) 100%);
  z-index: 1;
}
"""
css = re.sub(r"\.hero-bg\s*\{[\s\S]*?\.hero-overlay\s*\{[\w\s\(\),%;:\-]*\}", hero_new, css)

# Replace from Marquette down to FAQ
portfolio_css = """
/* =============================================
   PORTFOLIO SECTION
   ============================================= */
.section-portfolio {
  background: var(--black-2);
}

.portfolio-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
  gap: 32px;
  margin-top: 60px;
}

.portfolio-card {
  background: var(--black-3);
  border: 1px solid var(--border);
  border-radius: var(--radius-lg);
  overflow: hidden;
  position: relative;
  transition: all var(--transition);
}

.portfolio-card:hover {
  transform: translateY(-8px);
  border-color: rgba(201, 168, 76, 0.4);
  box-shadow: 0 16px 40px rgba(0, 0, 0, 0.6);
}

.portfolio-image {
  height: 280px;
  background-size: cover;
  background-position: center;
  transition: transform 0.6s ease;
}

.portfolio-card:hover .portfolio-image {
  transform: scale(1.05);
}

.portfolio-content {
  padding: 32px;
  position: relative;
  z-index: 2;
  background: var(--black-3);
  border-top: 1px solid var(--border);
}

.portfolio-content h3 {
  font-family: 'DM Serif Display', serif;
  font-size: 1.6rem;
  color: var(--white);
  margin-bottom: 12px;
}

.portfolio-desc {
  font-size: 0.95rem;
  color: var(--white-50);
  line-height: 1.6;
  margin: 0;
}

/* =============================================
   FAQ
   ============================================= */"""

css = re.sub(r"/\*\s*=============================================\s*MARQUEE[\s\S]*?/\*\s*FAQ\s*\*/", portfolio_css, css)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(css)

print("CSS replacement completed successfully.")
