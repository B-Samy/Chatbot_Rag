# 🎬 Movie Recommendation System

A content-based **Movie Recommendation System** that recommends movies similar to a user's selected movie.

The project combines **Data Science, Natural Language Processing, Machine Learning, similarity algorithms, and the TMDB API** to create an interactive movie discovery application.

---

## 🚀 What the Project Does

The user selects or searches for a movie, and the system finds movies with similar characteristics.

```text
User selects movie
        ↓
Movie information
        ↓
Feature processing
        ↓
Text/vector representation
        ↓
Similarity calculation
        ↓
Top similar movies
        ↓
TMDB API
        ↓
Posters + movie information
        ↓
🎬 Recommendations
```

---

# 🎯 Objective

The goal is to build a recommendation system that answers:

> **"If I liked this movie, what other movies might I like?"**

For example:

```text
Selected Movie:
Interstellar

        ↓

Recommendations:
• Inception
• The Martian
• Gravity
• Arrival
```

The recommendations are based on movie characteristics rather than simply popularity.

---

# 📊 Dataset

Movie information is collected from movie datasets and/or the **TMDB API**.

Relevant information can include:

* Movie title
* Genres
* Overview
* Keywords
* Cast
* Director
* Movie ID
* Poster information
* Release information
* Ratings

These features provide information that can be used to determine movie similarity.

---

# 🧹 Data Preprocessing

Movie information is prepared before calculating similarity.

Typical processing includes:

```text
Raw Movie Data
      ↓
Select useful features
      ↓
Handle missing values
      ↓
Clean text
      ↓
Combine important movie features
      ↓
Create movie representation
```

For example, important textual features can be combined:

```text
Genres + Keywords + Cast + Director + Overview
```

into a single representation.

---

# 🧠 Recommendation Approach

The system uses a **content-based recommendation approach**.

Instead of depending on what other users watched, the system compares the characteristics of movies.

```text
Movie A
   ↓
Movie Features
   ↓
Vector Representation
   ↓
Similarity
   ↑
Vector Representation
   ↑
Movie B
```

Movies with similar feature representations receive higher similarity scores.

---

# 🔢 Vectorization

Textual movie information is converted into numerical representations so that similarity can be calculated.

Depending on the implementation, techniques such as:

* Bag of Words
* TF-IDF
* Text vectorization

can be used.

Example:

```text
Movie features
      ↓
Text vectorization
      ↓
Numerical vectors
      ↓
Similarity calculation
```

---

# 📐 Similarity Calculation

The system calculates how similar movies are to each other.

A common approach is **Cosine Similarity**.

Conceptually:

```text
Similarity(Movie A, Movie B)
          ↓
Higher score → More similar
Lower score  → Less similar
```

The movies with the highest similarity scores are selected as recommendations.

---

# 🌐 TMDB API

The **TMDB API** is used to retrieve additional movie information and visual content.

The recommendation algorithm determines **which movies to recommend**, while TMDB provides information such as:

* Movie posters
* Movie details
* Release information
* Ratings
* Descriptions
* Other movie metadata

```text
Recommendation Model
        ↓
Recommended Movie IDs
        ↓
TMDB API
        ↓
Movie Details
        ↓
Poster + Information
```

This separates the **recommendation logic** from the **movie information service**.

---

# 🏗️ Project Architecture

```text
                    🎬 Movie Dataset
                           │
                           ▼
                         EDA
                           │
                           ▼
                  Data Preprocessing
                           │
                           ▼
                  Feature Engineering
                           │
                           ▼
                   Text Vectorization
                           │
                           ▼
                 Similarity Calculation
                           │
                           ▼
                  Recommendation Engine
                           │
                    User selects movie
                           │
                           ▼
                    Similar Movies
                           │
                           ▼
                       TMDB API
                           │
                           ▼
                Posters + Movie Details
                           │
                           ▼
                    🎬 Final Results
```

---

# 🔄 Complete Workflow

```text
1. Collect movie data
        ↓
2. Explore the dataset
        ↓
3. Clean movie information
        ↓
4. Select important features
        ↓
5. Combine movie features
        ↓
6. Convert text into vectors
        ↓
7. Calculate movie similarity
        ↓
8. Build recommendation function
        ↓
9. Select a movie
        ↓
10. Find similar movies
        ↓
11. Request movie details from TMDB API
        ↓
12. Display recommendations
```

---

# 🛠️ Technologies Used

| Technology   | Purpose                     |
| ------------ | --------------------------- |
| Python       | Core development            |
| Pandas       | Data manipulation           |
| NumPy        | Numerical operations        |
| Scikit-learn | Vectorization & similarity  |
| NLP          | Movie text processing       |
| TMDB API     | Movie information & posters |
| Requests     | API communication           |
| Streamlit    | User interface              |

---

# 📁 Suggested Project Structure

```text
Movie-Recommendation/
│
├── app.py
├── README.md
├── requirements.txt
│
├── data/
│   └── movies.csv
│
├── models/
│   └── similarity.pkl
│
├── notebooks/
│   └── movie_recommendation.ipynb
│
└── src/
    ├── preprocessing.py
    ├── recommendation.py
    └── tmdb_api.py
```

---

# 🌐 Streamlit Application

The final application provides an interactive movie recommendation interface.

```text
┌─────────────────────────────────────┐
│ 🎬 Movie Recommendation System      │
│                                     │
│ Select a movie                     │
│ [ Interstellar          ▼ ]         │
│                                     │
│        [ Recommend ]                │
│                                     │
│ Recommended Movies                  │
│                                     │
│ 🎬 Movie 1   🎬 Movie 2             │
│ 🎬 Movie 3   🎬 Movie 4             │
└─────────────────────────────────────┘
```

Movie posters and additional information are retrieved through the TMDB API.

---

# 🎓 Learning Outcomes

This project demonstrates practical experience with:

* Data preprocessing
* Exploratory Data Analysis
* Feature engineering
* NLP text processing
* Text vectorization
* Content-based recommendation
* Cosine similarity
* API integration
* Data retrieval
* Streamlit application development

---

# 🔮 Future Improvements

Possible improvements include:

* Hybrid recommendation system
* User-based recommendations
* Personalized watch history
* Rating-based recommendations
* Genre filtering
* Mood-based recommendations
* Multi-language movie search
* Recommendation explanations
* User authentication
* Movie watchlists

---

## ⭐ Project Summary

**Movie Recommendation System** is a content-based recommendation application that analyzes movie characteristics, calculates similarity between movies, and uses the **TMDB API** to present rich movie information and posters.

The project combines:

**Data Science → NLP → Machine Learning → Similarity Search → API Integration → Streamlit**

to create an end-to-end movie discovery application.
