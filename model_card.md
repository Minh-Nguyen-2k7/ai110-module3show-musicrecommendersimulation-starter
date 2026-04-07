# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

MoodConstructor v1.2.3.4
---

## 2. Intended Use  

- This recommender will create a list of suggested songs that should fit to the user's need based on their personal song interest.
- Specifically, the recommender is based on the user's preferred genre, mood, energy and tempo
- This is just a sample, classroom exploration of how a typical song recommender would work.
---

## 3. How the Model Works  

- The recommender looks at four features of each song: genre, mood, energy level, and tempo. The user tells the system what genre and mood they prefer, how energetic they want the music to feel (on a scale of 0 to 1), and optionally a target tempo. For each song in the catalog, the system checks how well it matches those preferences and produces a single score between 0 and 1. Genre and mood are treated as yes-or-no matches — either the song fits or it does not. Energy is compared as a distance — the closer the song's energy is to what the user wants, the higher it scores. Tempo is normalized across the catalog before comparing, so a slow song and a fast song are judged fairly. The four scores are then combined using weights — genre counts the most (40%), followed by mood (30%), energy (20%), and tempo (10%). Songs are ranked from highest to lowest score, and the top five are returned as recommendations.

---

## 4. Data  
  
- The catalog contains 18 songs loaded from a CSV file. Genres represented include pop, lofi, rock, classical, hip-hop, blues, acoustic, and synth.
- Moods include happy, chill, intense, sad, and romantic. No songs were added or removed from the original dataset. Musical styles that are missing or underrepresented include R&B, jazz, country, and Latin — meaning users who prefer those genres will rarely get a genre match and receive weaker recommendations overall.

---

## 5. Strengths  

- The system works best for users whose preferences clearly match a well-represented genre in the catalog — particularly pop, lofi, and rock. For those profiles, the top results scored above 0.95 and felt intuitive. The scoring also captures energy level well: a user who wants high-energy music consistently receives songs with energy values close to their target. The explanation output for each recommendation is a strength too — every result shows exactly which features matched and how much each contributed to the score, making the system fully transparent.
---

## 6. Limitations and Bias 

- The genre weight (0.4) creates a filter bubble. Because genre is the single heaviest factor in the score, the system almost always returns songs from the same genre the user already prefers — even when a song from a different genre matches their energy and mood far better. The system cannot reward a song for being "close" in genre (like indie-pop vs pop); it only sees a match or a complete miss. This design makes the users with cross-genre tastes have problems finding their best song recommendations, and this also force a user to stick to what they are used to rather than helping them discover new genre they never tried.

---

## 7. Evaluation  

- I tested five user profiles to evaluate how the recommender behaved across different situations. Three were realistic profiles — High-Energy Pop, Chill Lofi, and Deep Intense Rock — and two were edge cases designed to stress-test the scoring logic. 
- For the realistic profiles, the top results matched my expectations for the design: the correct genre and mood songs ranked highest, with scores above 0.95 in most cases. The most surprising result came from the "Conflicting: Lofi + High Energy" profile, where the system returned lofi songs in the top 3 even though none of them matched the requested energy level, which shows how genre dominates the score. 
- I also ran a weight experiment where I halved the genre weight (0.4 → 0.2) and doubled the energy level (0.2 → 0.4), which caused cross-genre songs with strong energy matches to surface higher in the rankings. 
- This makes me confirmed that the weights directly control how "open" or "narrow" the recommendations feel, and that no single weight setting is objectively correct — it depends on what the user values most.

---

## 8. Future Work  

- Allowing adjacent genres to receive a small score instead of zero.
- Use the unused `likes_acoustic` field in the scoring so acoustic preference actually influences results.
- Add a diversity rule so the same artist cannot appear more than once in the top 5.
- Expand the catalog, since 18 songs are too small for meaningful recommendations across many profiles.

---

## 9. Personal Reflection  

- Building this recommender makes me realize how hard it is for a recommender to truly capture the next recommender song for new user. The scoring systems are actually way harder than complex than I expected. Also users can have very weird preferences, such as a high-energy lofi song. Perhaps real apps like Spotify also have certain tradeoffs when they use many weighted scores, and they reflect the people's idea who built the system - not some objective truth about what music is good.
