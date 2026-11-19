# Ranveer Singh: Hair Length vs. Film Quality

**Question:** Do Ranveer Singh's best films line up with his longest hair?

## Files
- `ranveer_hair_vs_imdb.csv`: 16 lead-role films, IMDb rating, hair length (1 to 5), confidence, note
- `ranveer_hair_scatter.png`: scatter plot with trend line
- `build.py`: reproduces the stats and chart

## Method
- Film quality: IMDb rating (a "good film" flag at 7.0+)
- Hair length: hand-coded ordinal scale, 1 = crop, 3 = mid-length/tousled, 5 = very long. Each row has a confidence flag.
- Stats: Pearson and Spearman correlation, plus a 20,000-shuffle permutation test (n is small)

## Results (v1)
- Spearman rho = 0.37, Pearson r = 0.34
- Permutation p = 0.16, so not statistically significant at n = 16
- Mean IMDb by hair length: level 2 = 5.7 (n=8), level 3 = 5.5 (n=5), level 4 = 7.5 (n=3)
- The three "long hair" films (Bajirao Mastani, Padmaavat, Dhurandhar) all rate 7.0+, but the effect rests on those three.
- Among only the high-confidence hair codes (n=4) the correlation is slightly negative, so the signal is fragile.

## Known limitations / to do
1. Hair codes come from recollection of each film's look, not frame-by-frame review. Verify with stills before publishing.
2. IMDb ratings drift and sources disagree (e.g. Dhurandhar shows 8.3 in some places, 6.9 in others). Re-pull from one source on one date.
3. Missing films: 83, Jayeshbhai Jordaar (ratings not verified yet); Dhurandhar: The Revenge (2026).
4. Confounds: director (Bhansali's period epics), genre, and role type drive both look and quality. Long hair is mostly a period-drama or gritty-role signal.
5. Ideas: add Rotten Tomatoes / box office, code beard separately, use a Letterboxd rating as a second quality measure.
