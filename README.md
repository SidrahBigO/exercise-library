# Exercise Library

A standalone exercise library and browser-based review tool.

## Structure

```
exercise-library/
  data/
    exercises.json       — filtered exercise dataset
    brand-tokens.json    — brand audit output (colors, typography, tokens)
  review-tool/
    index.html           — swipe-style review app for browsing exercises
```

## Usage

### Data

Drop your filtered dataset into `data/exercises.json` and your brand audit output into `data/brand-tokens.json`. Both files are consumed directly by the review tool — no build step required.

### Review Tool

Open `review-tool/index.html` in any modern browser. The app loads exercise data from `../data/exercises.json` and applies brand tokens from `../data/brand-tokens.json`, letting you swipe through exercises, approve or reject them, and export your selections.
