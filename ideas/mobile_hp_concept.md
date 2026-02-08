# Mobile HP Conversion Concept

## Overview
Transform the current "Rakuich" homepage into a fully optimized smartphone experience ("App-like" Web). The goal is not just responsiveness, but a "Mobile Native" feel.

## 1. Design Philosophy: "Thumb-Driven Design"
*   **Bottom Navigation**: Move primary navigation to the bottom of the screen (easiest to reach with thumb).
*   **Card-Based Layout**: Content should be chunked into cards that fit within a single screen view or are swipeable.
*   **Bigger Touch Targets**: Buttons and interactive elements must be at least 44x44px.

## 2. Key Section Redesigns

### Header & Navigation
*   **Current**: Top bar with text links.
*   **Proposal**: 
    *   **Hide Top Bar on Scroll**: Maximize screen real estate.
    *   **Hamburger Menu (Right)**: For full menu access.
    *   **Sticky Bottom Action Bar**: Always visible "Join / Inquiry" button.

### Hero Section (First View)
*   **Current**: Large image with centered text.
*   **Proposal**:
    *   **Full Screen Height (100dvh)**: Guarantee the hero fills the exact mobile screen height.
    *   **Vertical Centering**: Text and main CTA in the optical center.
    *   **Background Video/Animation**: Subtle movement to signal "aliveness".

### Philosophy & Comparison (Section: `#intro`)
*   **Current**: Side-by-side or stacked text blocks.
*   **Proposal**:
    *   **Swipeable Cards**: Instead of long vertical scrolling, place "Original vs Modern" comparisons in a horizontal swipe container.
    *   **Interactive Toggle**: "Tap to flip" cards to see the contrast between current economy and Rakuich economy.

### Use Scenes (Section: `#scenes`)
*   **Current**: Vertical list of 3 scenes (Give, Exchange, Receive).
*   **Proposal**:
    *   **Horizontal Carousel**: Users swipe left/right to view different use cases.
    *   **Pagination Dots**: Briefly show how many scenes there are.

### System Diagram (Section: `#system`)
*   **Current**: Large complex diagram images.
*   **Proposal**:
    *   **Simplified SVG/CSS Animation**: Break down the diagram into steps that build up as the user scrolls (Scrollytelling).
    *   **Zoomable Image**: Allow users to tap and zoom into complex diagrams.

## 3. Interaction & "App-Like" Feel
*   **Page Transitions**: Smooth fade or slide effects between "pages" (even if just scrolling anchors).
*   **Haptic Feedback (Visual)**: Ripple effects on buttons.
*   **Skeleton Loading**: Show placeholders while images load to prevent layout shift.

## 4. Technical Roadmap (Ideas)
*   **PWA (Progressive Web App)**: Add `manifest.json` and Service Worker so users can "Add to Home Screen" and use it offline.
*   **CSS Scroll Snap**: For the "Swipeable Sections" to make them snap cleanly into place.
*   **Font Optimization**: Ensure text is readable (16px+ body) without zooming.

## 5. Next Layout Sketch (Textual)

```
[ Navbar: Logo (Left) | Menu (Right) ]
--------------------------------------
[ Hero Section (100dvh)              ]
[   "Maximize Circulation"           ]
[   [ CTA Button ]                   ]
[   v Scroll Indicator v             ]
--------------------------------------
[ Concept Cards (Horizontal Scroll)  ]
[  [Card 1]  [Card 2]  [Card 3]      ]
--------------------------------------
[ Interactive System Diagram         ]
[ (User Taps to advance step)        ]
--------------------------------------
[ Footer                             ]
--------------------------------------
[ Sticky Bottom Bar                  ]
[  [ About ] [ System ] [ JOIN ]     ]
```
