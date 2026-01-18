#!/usr/bin/env python3
"""
Rakuichi HP Generator
Generates index.html from content.json and template files
"""

import json
import os
from pathlib import Path


def load_json(filepath):
    """Load JSON file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)


def load_template(filepath):
    """Load template file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()


def render_intro_philosophy_items(blocks):
    """Render intro philosophy items (origin_tool, value_illusion) - vertical layout"""
    philosophy_blocks = [b for b in blocks if b.get('group') == 'philosophy']
    html = ""
    
    for i, block in enumerate(philosophy_blocks):
        title = block.get('title', '')
        image = block.get('image', '')
        text_items = block.get('text', [])
        
        # Create text paragraphs
        text_html = "\n".join([f"                        <p>{t}</p>" for t in text_items])
        
        # Horizontal layout: title on top, then image (left) + text (right)
        html += f"""                    <!-- Block {i+1}: {block.get('id', '')} -->
                    <div class="philosophy-block">
                        <h3>{title}</h3>
                        <div class="philosophy-content-wrapper">
                            <div class="philosophy-image">
                                <img src="{image}" alt="{title}">
                            </div>
                            <div class="philosophy-text">
{text_html}
                            </div>
                        </div>
                    </div>
"""
    
    return html


def render_intro_dilemma_items(blocks):
    """Render intro dilemma items (subcopy, business_pressure, volunteer_limit)"""
    dilemma_blocks = [b for b in blocks if b.get('group') == 'dilemma']
    html = ""
    
    for i, block in enumerate(dilemma_blocks):
        block_type = block.get('type', '')
        block_id = block.get('id', '')
        
        if block_type == 'subcopy':
            # Render intro/lead text
            text_items = block.get('text', [])
            text_html = "\n".join([f"                        <p>{t}</p>" for t in text_items])
            
            html += f"""                    <!-- Dilemma Intro -->
                    <div class="dilemma-intro">
{text_html}
                    </div>
"""
        
        elif block_type == 'issue':
            # Render issue blocks with Top Row (Text+Image) and Bottom Row (Conclusion)
            number = block.get('number', '')
            title = block.get('title', '')
            image = block.get('image', '')
            image_position = block.get('imagePosition', 'right')  # 'left' or 'right'
            
            # Handle text content
            intro_text = block.get('text', [])
            conclusion_text = block.get('text_conclusion', [])
            tasks = block.get('tasks', [])
            
            # Create intro text paragraphs
            intro_html = "\n".join([f"                                    <p>{t}</p>" for t in intro_text if t])
            
            # Start issue container
            position_class = f"image-{image_position}"
            html += f"""                    <!-- Issue {number}: {block_id} -->
                    <div class="dilemma-issue {position_class}">
"""
            
            # --- TOP ROW: Text and Image ---
            html += """                        <div class="issue-top-row">
"""
            
            # 1. Text Component (Always first in DOM for Mobile Text->Image order)
            text_content = f"""                            <div class="issue-text">
                                <h3><span class="issue-number">{number}.</span> {title}</h3>
                                <div class="issue-content">
"""
            if intro_html:
                text_content += intro_html + "\n"
                
            # Add tasks list or task image if present
            tasks_html = ""
            if 'task_image' in block:
                 tasks_html = f'''
                                    <div class="issue-task-image">
                                        <img src="{block['task_image']}" alt="ビジネスの課題" style="width: 100%; height: auto; margin: var(--spacing-lg) 0; border-radius: var(--radius-sm);">
                                    </div>
'''
            elif tasks: 
                tasks_html = """                                    <ul class="issue-tasks">
"""
                for task in tasks:
                    label = task.get('label', '')
                    description = task.get('description', '')
                    tasks_html += f"""                                        <li>
                                            <strong>{label}：</strong><span>{description}</span>
                                        </li>
"""
                tasks_html += """                                    </ul>
"""
            if tasks_html:
                text_content += tasks_html + "\n"
            
            text_content += """                                </div>
                            </div>
"""
            html += text_content
            
            # 2. Image Component
            html += f"""                            <div class="issue-image">
                                <img src="{image}" alt="{title}">
                            </div>
"""
            
            html += """                        </div>
"""
            # --- END TOP ROW ---

            # --- BOTTOM ROW: Conclusion (Full Width) ---
            if conclusion_text:
                conclusion_html = "\n".join([f"                            <p>{t}</p>" for t in conclusion_text if t])
                html += f"""                        <div class="issue-bottom-row">
                            <div class="issue-conclusion">
{conclusion_html}
                            </div>
                        </div>
"""
            
            html += """                    </div>
"""
        
        elif block_type == 'conclusion':
            # Render conclusion text
            text_items = block.get('text', [])
            text_html = "\n".join([f"                        <p>{t}</p>" for t in text_items])
            
            html += f"""                    <!-- Dilemma Conclusion -->
                    <div class="dilemma-conclusion">
{text_html}
                    </div>
"""
    
    return html


def render_text_paragraphs(text_array):
    """Render text array as paragraphs"""
    return "\n".join([f"                <p>{t}</p>" for t in text_array])


def generate_html(content_data):
    """Generate complete HTML from content.json"""
    base_dir = Path(__file__).parent
    src_dir = base_dir / 'src'
    sections_dir = src_dir / 'sections'
    
    # Load base template
    base_template = load_template(src_dir / 'base.html')
    
    # Load section templates
    hero_template = load_template(sections_dir / 'hero.html')
    intro_template = load_template(sections_dir / 'intro.html')
    dilemma_template = load_template(sections_dir / 'dilemma.html')
    crevasse_template = load_template(sections_dir / 'crevasse.html')
    problem_template = load_template(sections_dir / 'problem.html')
    explanation_template = load_template(sections_dir / 'explanation.html')
    value_illusion_template = load_template(sections_dir / 'value_illusion.html')
    circulation_template = load_template(sections_dir / 'circulation.html')
    philosophy_template = load_template(sections_dir / 'philosophy.html')
    system_template = load_template(sections_dir / 'system.html')
    scenes_template = load_template(sections_dir / 'scenes.html')
    examples_template = load_template(sections_dir / 'examples.html')
    media_template = load_template(sections_dir / 'media.html')
    vision_template = load_template(sections_dir / 'vision.html')
    join_template = load_template(sections_dir / 'join.html')
    footer_template = load_template(sections_dir / 'footer.html')
    
    # Prepare template variables
    template_vars = {
        'meta_title': content_data['meta']['title'],
        'meta_description': content_data['meta']['description'],
        'meta_keywords': content_data['meta']['keywords'],
    }
    
    # Render sections
    sections_html = ""
    
    # Hero section
    hero_html = hero_template.replace('{{hero_title}}', content_data['hero']['title'])
    hero_html = hero_html.replace('{{hero_subtitle}}', content_data['hero']['subtitle'])
    hero_html = hero_html.replace('{{hero_image}}', content_data['hero']['image'])
    hero_html = hero_html.replace('{{hero_cta_text}}', content_data['hero']['cta_text'])
    sections_html += "\n" + hero_html
    
    # Intro philosophy section (vertical layout)
    intro_philosophy_items = render_intro_philosophy_items(content_data['intro']['blocks'])
    intro_html = intro_template.replace('{{intro_philosophy_items}}', intro_philosophy_items)
    # Update the class from contrast-grid to philosophy-vertical for vertical layout
    intro_html = intro_html.replace('class="contrast-grid"', 'class="philosophy-vertical"')
    sections_html += "\n" + intro_html
    
    # Dilemma section
    intro_dilemma_items = render_intro_dilemma_items(content_data['intro']['blocks'])
    # Extract dilemma title from the first dilemma block (subcopy)
    dilemma_title = ""
    for block in content_data['intro']['blocks']:
        if block.get('group') == 'dilemma' and block.get('type') == 'subcopy':
            dilemma_title = block.get('title', '進むも退くも、茨の道。')
            break
    dilemma_html = dilemma_template.replace('{{intro_dilemma_items}}', intro_dilemma_items)
    dilemma_html = dilemma_html.replace('{{dilemma_title}}', dilemma_title)
    sections_html += "\n" + dilemma_html
    
    # Crevasse section
    crevasse = content_data['intro']['solution']
    crevasse_text = render_text_paragraphs(crevasse['text'])
    crevasse_html = crevasse_template.replace('{{intro_crevasse_title}}', crevasse['title'])
    crevasse_html = crevasse_html.replace('{{intro_crevasse_image}}', crevasse['image'])
    crevasse_html = crevasse_html.replace('{{intro_crevasse_text}}', crevasse_text)
    sections_html += "\n" + crevasse_html

    # Explanation section
    explanation = content_data.get('explanation', {})
    if explanation:
        cards_html = ""
        for card in explanation.get('cards', []):
            card_type = card.get('type', '')
            image = card.get('image', '')
            title = card.get('title', '')
            subtitle = card.get('subtitle', '')
            text = card.get('text', '')
            
            cards_html += f"""                    <div class="comparison-card {card_type}">
                        <div class="comparison-image">
                            <img src="{image}" alt="{title}">
                        </div>
                        <div class="comparison-content">
                            <h3 class="comparison-title">{title}</h3>
                            <p class="comparison-subtitle">{subtitle}</p>
                            <div class="comparison-features">
                                <p class="comparison-text">{text}</p>
                            </div>
                        </div>
                    </div>
"""
        
        explanation_html = explanation_template.replace('{{explanation_title}}', explanation.get('title', ''))
        explanation_html = explanation_html.replace('{{explanation_cards}}', cards_html)
        sections_html += "\n" + explanation_html

    # Circulation section
    circulation = content_data.get('circulation', {})
    if circulation:
        circulation_html = circulation_template.replace('{{circulation_image}}', circulation.get('image', ''))
        circulation_html = circulation_html.replace('{{circulation_caption}}', circulation.get('caption', ''))
        sections_html += "\n" + circulation_html
    

    
    # Philosophy section
    philosophy_cols_html = ""
    for col in content_data['philosophy']['cols']:
        philosophy_cols_html += f"""                <div class="philosophy-col">
                    <h3>{col['title']}</h3>
                    <p>{col['text']}</p>
                </div>
"""
    
    philosophy_html = f"""
    <section class="philosophy section bg-white" id="philosophy">
        <div class="container">
            <h2 class="section-title">{content_data['philosophy']['title']}</h2>
            <div class="philosophy-quote">
                <p>{content_data['philosophy']['quote']}</p>
            </div>
            <div class="philosophy-content">
{philosophy_cols_html}            </div>
        </div>
    </section>
"""
    sections_html += philosophy_html
    
    # System section (楽ポイントシステム)
    system = content_data.get('system', {})
    if system:
        limits = system.get('limits', {})
        plus_limit = limits.get('plus', {})
        minus_limit = limits.get('minus', {})
        
        system_html = f"""
    <section class="system section bg-cream" id="system">
        <div class="container">
            <h2 class="section-title">{system.get('title', '')}</h2>
            <p class="system-intro">{system.get('intro', '')}</p>
            
            <div class="limit-visual-container">
                <div class="limit-bar-line"></div>
                
                <!-- Plus Limit -->
                <div class="limit-item">
                    <div class="limit-marker-line"></div>
                    <div class="limit-value-label">{plus_limit.get('value', '')}</div>
                    <div class="limit-content">
                        <h4>{plus_limit.get('purpose', '')}</h4>
                        <p>{plus_limit.get('text', '')}</p>
                    </div>
                </div>
                
                <!-- Minus Limit -->
                <div class="limit-item">
                    <div class="limit-marker-line"></div>
                    <div class="limit-value-label">{minus_limit.get('value', '')}</div>
                    <div class="limit-content">
                        <h4>{minus_limit.get('purpose', '')}</h4>
                        <p>{minus_limit.get('text', '')}</p>
                    </div>
                </div>
                
                <!-- Ideal State -->
                <div class="limit-item is-ideal">
                    <div class="limit-content">
                        <div class="ideal-scale">
                            <span>-30,000</span>
                            <span>0</span>
                            <span>+30,000</span>
                        </div>
                        <p>{system.get('ideal', '')}</p>
                    </div>
                </div>
            </div>
            
            <!-- Balance Meter Animation -->
            <div class="balance-meter">
                <div class="meter-track">
                    <div class="meter-indicator"></div>
                    <div class="meter-label left">-30,000</div>
                    <div class="meter-label center">0</div>
                    <div class="meter-label right">+30,000</div>
                </div>
            </div>

        </div>
    </section>
"""
        sections_html += system_html
    
    # Scenes section (楽市の3つのシーン)
    scenes = content_data.get('scenes', {})
    if scenes:
        scenes_items_html = ""
        for item in scenes.get('items', []):
            scenes_items_html += f"""            <div class="scene-card">
                <div class="scene-image">
                    <img src="{item.get('image', '')}" alt="{item.get('title', '')}">
                </div>
                <div class="scene-content">
                    <h3>{item.get('title', '')}</h3>
                    <p class="scene-concept">{item.get('concept', '')}</p>
                    <p class="scene-story">{item.get('story', '')}</p>
                </div>
            </div>
"""
        
        scenes_html = f"""
    <section class="scenes section bg-white" id="scenes">
        <div class="container">
            <h2 class="section-title">{scenes.get('title', '')}</h2>
{scenes_items_html}        </div>
    </section>
"""
        sections_html += scenes_html
    
    # Examples section
    examples = content_data.get('examples', {})
    if examples:
        examples_items_html = ""
        for item in examples.get('items', []):
            examples_items_html += f"""            <div class="example-card">
                <div class="example-image">
                    <img src="{item.get('image', '')}" alt="{item.get('title', '')}">
                </div>
                <h3>{item.get('title', '')}</h3>
                <p>{item.get('text', '')}</p>
            </div>
"""
        
        examples_html = f"""
    <section class="examples section bg-cream" id="examples">
        <div class="container">
            <h2 class="section-title">{examples.get('title', '')}</h2>
            <div class="examples-grid">
{examples_items_html}            </div>
            <p class="examples-note">{examples.get('note', '')}</p>
        </div>
    </section>
"""
        sections_html += examples_html
    
    # Media section
    media = content_data.get('media', {})
    if media:
        media_html = f"""
    <section class="media section bg-white" id="media">
        <div class="container">
            <h2 class="section-title">{media.get('title', '')}</h2>
            <p class="media-intro">{media.get('intro', '')}</p>
            
            <div class="media-grid">
                <div class="media-item">
                    <div class="media-placeholder video">
                        <p>📹</p>
                    </div>
                    <h3>{media.get('video', {}).get('title', '')}</h3>
                    <p>{media.get('video', {}).get('text', '')}</p>
                </div>
                
                <div class="media-item">
                    <div class="media-placeholder pdf">
                        <p>📄</p>
                    </div>
                    <h3>{media.get('pdf', {}).get('title', '')}</h3>
                    <p>{media.get('pdf', {}).get('text', '')}</p>
                </div>
            </div>
        </div>
    </section>
"""
        sections_html += media_html
    
    # Vision section
    vision = content_data.get('vision', {})
    if vision:
        vision_features_html = ""
        for feature in vision.get('features', []):
            vision_features_html += f"""            <div class="vision-feature">
                <p>✓ {feature}</p>
            </div>
"""
        
        vision_html = f"""
    <section class="vision section bg-cream" id="vision">
        <div class="container">
            <h2 class="section-title">{vision.get('title', '')}</h2>
            <div class="vision-features">
{vision_features_html}            </div>
            <div class="vision-quote">
                <p>{vision.get('quote', '')}</p>
            </div>
        </div>
    </section>
"""
        sections_html += vision_html
    
    # Join section
    join = content_data.get('join', {})
    if join:
        join_roles_html = ""
        for role in join.get('roles', []):
            join_roles_html += f"""            <div class="role-card">
                <h3>{role.get('title', '')}</h3>
                <p>{role.get('text', '')}</p>
            </div>
"""
        
        join_html = f"""
    <section class="join section bg-white" id="join">
        <div class="container">
            <h2 class="section-title">{join.get('title', '')}</h2>
            <p class="join-intro">{join.get('intro', '')}</p>
            
            <div class="roles-grid">
{join_roles_html}            </div>
            
            <div class="join-cta">
                <p class="cta-message">{join.get('cta_message', '')}</p>
                <a href="mailto:{join.get('email', '')}" class="btn btn-primary btn-large">お問い合わせ</a>
            </div>
        </div>
    </section>
"""
        sections_html += join_html
    
    # Footer
    footer = content_data.get('footer', {})
    footer_html = f"""
    <footer class="footer bg-dark section">
        <div class="container">
            <div class="footer-brand">楽市</div>
            <p class="footer-tagline">{footer.get('tagline', '')}</p>
            <div class="footer-bottom">
                <p class="copyright">{footer.get('copyright', '')}</p>
            </div>
        </div>
    </footer>
"""
    sections_html += footer_html
    
    # Insert sections into main tag
    main_html = f"""
    <main>
{sections_html}
    </main>
"""
    
    # Replace in base template
    html = base_template.replace('{{meta_title}}', template_vars['meta_title'])
    html = html.replace('{{meta_description}}', template_vars['meta_description'])
    html = html.replace('{{meta_keywords}}', template_vars['meta_keywords'])
    html = html.replace('{{content}}', main_html)
    
    return html


def main():
    """Main function"""
    base_dir = Path(__file__).parent
    
    # Load content.json
    content_path = base_dir / 'config' / 'content.json'
    print(f"Loading content from: {content_path}")
    content_data = load_json(content_path)
    
    # Generate HTML
    print("Generating HTML...")
    html = generate_html(content_data)
    
    # Write to index.html
    output_path = base_dir / 'index.html'
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"✓ Generated: {output_path}")
    print("完了！HPに変更が反映されました。")


if __name__ == '__main__':
    main()
