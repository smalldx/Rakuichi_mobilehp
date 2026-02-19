const BOTTOM_NAV_SELECTOR = '.bottom-nav-item[href^="#"]';

function getTargetFromHash(hash) {
    if (!hash || hash === '#') return null;
    try {
        return document.querySelector(hash);
    } catch {
        return null;
    }
}

function smoothScrollToTarget(target) {
    if (!target) return;
    target.scrollIntoView({
        behavior: 'smooth',
        block: 'start'
    });
}

function setupAnchorScrolling() {
    const anchors = document.querySelectorAll('a[href^="#"]');
    anchors.forEach((anchor) => {
        anchor.addEventListener('click', (event) => {
            const href = anchor.getAttribute('href');
            const target = getTargetFromHash(href);
            if (!target) return;

            event.preventDefault();
            smoothScrollToTarget(target);
            history.replaceState(null, '', href);
        });
    });
}

function setupBottomNavHighlight() {
    const navItems = Array.from(document.querySelectorAll(BOTTOM_NAV_SELECTOR));
    const pairs = navItems
        .map((item) => ({
            item,
            target: getTargetFromHash(item.getAttribute('href'))
        }))
        .filter((pair) => pair.target);

    if (pairs.length === 0) return;

    const setActive = (activeItem) => {
        navItems.forEach((item) => {
            const isActive = item === activeItem;
            item.classList.toggle('active', isActive);
            if (isActive) {
                item.setAttribute('aria-current', 'page');
            } else {
                item.removeAttribute('aria-current');
            }
        });
    };

    const pickActiveItem = () => {
        const marker = window.scrollY + 140;
        let active = pairs[0].item;

        pairs.forEach((pair) => {
            if (pair.target.offsetTop <= marker) {
                active = pair.item;
            }
        });

        setActive(active);
    };

    let ticking = false;
    window.addEventListener('scroll', () => {
        if (ticking) return;
        ticking = true;
        requestAnimationFrame(() => {
            pickActiveItem();
            ticking = false;
        });
    }, { passive: true });

    window.addEventListener('resize', pickActiveItem);
    pickActiveItem();
}

function setupExampleTabs() {
    const tabs = document.querySelectorAll('.tab-btn');
    const cards = document.querySelectorAll('.category-card');

    if (!tabs.length || !cards.length) return;

    const filterCards = (filter) => {
        cards.forEach(card => {
            const category = card.getAttribute('data-category');
            if (filter === 'all' || filter === category) {
                card.style.display = 'flex';
                card.style.animation = 'none';
                card.offsetHeight; /* trigger reflow */
                card.style.animation = 'fadeIn 0.5s ease forwards';
            } else {
                card.style.display = 'none';
            }
        });
    };

    tabs.forEach(tab => {
        tab.addEventListener('click', () => {
            tabs.forEach(t => t.classList.remove('active'));
            tab.classList.add('active');
            const filter = tab.getAttribute('data-filter');
            filterCards(filter);
        });
    });

    // Initial filter execution based on active tab
    const activeTab = document.querySelector('.tab-btn.active');
    if (activeTab) {
        filterCards(activeTab.getAttribute('data-filter'));
    }
}



document.addEventListener('DOMContentLoaded', () => {
    setupAnchorScrolling();
    setupBottomNavHighlight();
    setupExampleTabs();
});
