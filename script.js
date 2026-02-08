// ===================================
// Mobile Navigation Toggle
// ===================================
const navToggle = document.getElementById('nav-toggle');
const navMenu = document.getElementById('nav-menu');

if (navToggle) {
    navToggle.addEventListener('click', () => {
        navMenu.classList.toggle('active');

        // Animate hamburger icon
        const spans = navToggle.querySelectorAll('span');
        if (navMenu.classList.contains('active')) {
            spans[0].style.transform = 'rotate(45deg) translate(5px, 5px)';
            spans[1].style.opacity = '0';
            spans[2].style.transform = 'rotate(-45deg) translate(7px, -6px)';
        } else {
            spans[0].style.transform = 'none';
            spans[1].style.opacity = '1';
            spans[2].style.transform = 'none';
        }
    });
}

// Close mobile menu when clicking on a link
const navLinks = document.querySelectorAll('.nav-link');
navLinks.forEach(link => {
    link.addEventListener('click', () => {
        if (navMenu.classList.contains('active')) {
            navMenu.classList.remove('active');
            const spans = navToggle.querySelectorAll('span');
            spans[0].style.transform = 'none';
            spans[1].style.opacity = '1';
            spans[2].style.transform = 'none';
        }
    });
});

// ===================================
// Smooth Scrolling (backup for older browsers)
// ===================================
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        const href = this.getAttribute('href');

        // Skip if href is just "#"
        if (href === '#') return;

        e.preventDefault();
        const target = document.querySelector(href);

        if (target) {
            const headerOffset = 80;
            const elementPosition = target.getBoundingClientRect().top;
            const offsetPosition = elementPosition + window.pageYOffset - headerOffset;

            window.scrollTo({
                top: offsetPosition,
                behavior: 'smooth'
            });
        }
    });
});

// ===================================
// Header Scroll Effect
// ===================================
const header = document.getElementById('header');
let lastScroll = 0;

window.addEventListener('scroll', () => {
    const currentScroll = window.pageYOffset;

    // Add shadow when scrolled
    if (currentScroll > 50) {
        header.style.boxShadow = '0 4px 12px rgba(0, 0, 0, 0.1)';
    } else {
        header.style.boxShadow = '0 2px 4px rgba(0, 0, 0, 0.1)';
    }

    lastScroll = currentScroll;
});

// ===================================
// Intersection Observer for Scroll Animations
// ===================================
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -100px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
        }
    });
}, observerOptions);

// Observe all cards and sections
const animatedElements = document.querySelectorAll(`
    .problem-card,
    .philosophy-card,
    .limit-card,
    .example-card,
    .vision-feature,
    .role-card
`);

animatedElements.forEach(el => {
    el.style.opacity = '0';
    el.style.transform = 'translateY(30px)';
    el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
    observer.observe(el);
});

// ===================================
// Active Navigation Link Highlighting
// ===================================
const sections = document.querySelectorAll('section[id]');

function highlightNavigation() {
    const scrollY = window.pageYOffset;

    sections.forEach(section => {
        const sectionHeight = section.offsetHeight;
        const sectionTop = section.offsetTop - 150; // Increased offset for better triggering
        const sectionId = section.getAttribute('id');
        
        // Target both desktop nav links and bottom nav items
        const targetLinks = document.querySelectorAll(`.nav-link[href="#${sectionId}"], .bottom-nav-item[href="#${sectionId}"]`);

        if (scrollY > sectionTop && scrollY <= sectionTop + sectionHeight) {
            targetLinks.forEach(link => {
                link.classList.add('active');
                // Maintain legacy inline style behavior for desktop nav if valid, but class is better
                if (link.classList.contains('nav-link')) {
                    link.style.color = 'var(--primary)';
                }
            });
        } else {
            targetLinks.forEach(link => {
                link.classList.remove('active');
                if (link.classList.contains('nav-link')) {
                    link.style.color = '';
                }
            });
        }
    });
}

window.addEventListener('scroll', highlightNavigation);

// ===================================
// Balance Meter Animation
// ===================================
const meterIndicator = document.querySelector('.meter-indicator');

if (meterIndicator) {
    let position = 50; // Start at center (0 points)
    let direction = 1;

    setInterval(() => {
        position += direction * 0.5;

        // Bounce back when reaching limits
        if (position >= 60 || position <= 40) {
            direction *= -1;
        }

        meterIndicator.style.left = position + '%';
    }, 50);
}

// ===================================
// Compact Balance Hero - Interactive Functions
// ===================================

let balanceCompact = 0; // -30000 to +30000

// Update balance with smooth animation
function updateBalanceCompact(newBalance) {
    balanceCompact = Math.max(-30000, Math.min(30000, newBalance));

    const indicator = document.getElementById('indicatorCompact');
    const statusElement = document.getElementById('statusCompact');
    const centerHighlight = document.getElementById('centerHighlight');
    const centerLabel = document.getElementById('centerLabel');

    if (!indicator || !statusElement) return;

    // Calculate position (0% = left/benefit, 50% = center, 100% = right/contribution)
    const percentage = ((balanceCompact + 30000) / 60000) * 100;
    indicator.style.left = percentage + '%';

    // Center glow when balanced
    const isBalanced = Math.abs(balanceCompact) <= 3000;
    if (centerHighlight) {
        centerHighlight.classList.toggle('active', isBalanced);
    }
    if (centerLabel) {
        centerLabel.style.transform = isBalanced ? 'scale(1.1)' : 'scale(1)';
    }

    // Update status message
    let message = '中庸：最も巡りが良い状態です';
    statusElement.className = 'bar-status-compact';

    if (isBalanced) {
        statusElement.classList.add('blessed');
    } else if (balanceCompact < -5000) {
        message = '御恩を多く受けています。次は奉公してみませんか？';
    } else if (balanceCompact > 5000) {
        message = '多くの徳を回しています。御恩を受け取ってみませんか？';
    }

    const statusText = statusElement.querySelector('.status-text');
    if (statusText) {
        statusText.style.opacity = '0';
        setTimeout(() => {
            statusText.textContent = message;
            statusText.style.opacity = '1';
        }, 200);
    }
}

// Show toast notification
function showToast(message, type = 'neutral') {
    const container = document.getElementById('toastContainer');
    if (!container) return;

    const toast = document.createElement('div');
    toast.className = `toast ${type}`;
    toast.textContent = message;

    container.appendChild(toast);

    // Remove after animation
    setTimeout(() => {
        toast.remove();
    }, 2000);
}

// Action: Benefit (receive help)
function actionBenefit() {
    const amount = Math.floor(Math.random() * 3000) + 2000; // 2000-5000
    updateBalanceCompact(balanceCompact - amount);
    showToast(`感謝を受け取りました`, 'benefit');
}

// Action: Contribution (give help)
function actionContribution() {
    const amount = Math.floor(Math.random() * 3000) + 2000; // 2000-5000
    updateBalanceCompact(balanceCompact + amount);
    showToast(`徳が回りました`, 'contribution');
}

// Action: Equilibrium (show suggestions)
function actionEquilibrium() {
    const modal = document.getElementById('modalCompact');
    const suggestions = document.getElementById('suggestionsCompact');

    if (!modal || !suggestions) return;

    let content = '';

    if (Math.abs(balanceCompact) <= 3000) {
        content = `
            <div class="suggestion-card">
                <strong>✨ 素晴らしいバランスです</strong><br>
                この調和を保ちながら、新しいご縁を探してみましょう。
            </div>
        `;
    } else if (balanceCompact < -5000) {
        content = `
            <div class="suggestion-card">
                <strong>🎁 次は奉公してみませんか？</strong><br>
                あなたの得意なことで、誰かを助けてみましょう。
            </div>
            <div class="suggestion-card">
                例：野菜を分ける、スキルを教える、手作り品を贈る
            </div>
        `;
    } else if (balanceCompact > 5000) {
        content = `
            <div class="suggestion-card">
                <strong>🙏 次は御恩を受けてみませんか？</strong><br>
                誰かの助けを素直に受け取ってみましょう。
            </div>
            <div class="suggestion-card">
                例：必要なものをリクエストする、教えてもらう、サービスを利用する
            </div>
        `;
    }

    suggestions.innerHTML = content;
    modal.classList.add('active');
    document.body.style.overflow = 'hidden';
}

// Close modal
function closeModalCompact() {
    const modal = document.getElementById('modalCompact');
    if (modal) {
        modal.classList.remove('active');
        document.body.style.overflow = '';
    }
}

// Initialize
document.addEventListener('DOMContentLoaded', () => {
    updateBalanceCompact(0);

    // ESC key to close modal
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') {
            closeModalCompact();
        }
    });
});

// ===================================
// Console Welcome Message
// ===================================
console.log('%c楽市 - Rakuichi', 'font-size: 24px; font-weight: bold; color: #E67E22;');
console.log('%c利益の最大化ではなく、循環の最大化を。', 'font-size: 14px; color: #27AE60;');
console.log('Welcome to the new circulating economy! 🔄');
