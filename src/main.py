"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv") 

    profiles = {
        "High-Energy Pop": {"genre": "pop",  "mood": "happy",   "energy": 0.9, "tempo_bpm": 120},
        "Chill Lofi":      {"genre": "lofi", "mood": "chill",   "energy": 0.3, "tempo_bpm": 75},
        "Deep Intense Rock":{"genre": "rock", "mood": "intense", "energy": 0.95,"tempo_bpm": 150},
    }

    for profile_name, user_prefs in profiles.items():
        recommendations = recommend_songs(user_prefs, songs, k=5)

        print("\n" + "=" * 50)
        print(f"  {profile_name.upper()}")
        print("=" * 50)
        for i, (song, score, explanation) in enumerate(recommendations, start=1):
            print(f"\n#{i}  {song['title']} by {song['artist']}")
            print(f"    Score : {score:.2f}")
            print(f"    Reasons:")
            for reason in explanation.split(", "):
                print(f"      - {reason}")
    print("\n" + "=" * 50)


if __name__ == "__main__":
    main()
