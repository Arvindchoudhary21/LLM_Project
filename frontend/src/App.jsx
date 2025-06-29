import { useState, useEffect } from "react";
import axios from "axios";
import ChapterCard from "./components/chapterCard";
import ScrollToTopButton from "./components/ScrollToTopButton";
import chapters from "./data/chapters"; // ← local chapters

function App() {
  const [searchText, setSearchText] = useState("");
  const [darkMode, setDarkMode] = useState(false);
  const [searchResult, setSearchResult] = useState(null); // backend result

  // Load dark mode preference
  useEffect(() => {
    const stored = localStorage.getItem("darkMode");
    if (stored) setDarkMode(JSON.parse(stored));
  }, []);

  useEffect(() => {
    localStorage.setItem("darkMode", JSON.stringify(darkMode));
  }, [darkMode]);

  // Call backend only when searchText is non-empty
  useEffect(() => {
    const fetchResult = async () => {
      if (searchText.trim() === "") {
        setSearchResult(null);
        return;
      }

      try {
        const res = await axios.get(
          `http://localhost:8000/search?query=${encodeURIComponent(searchText)}`
        );

        if (res.data.results && res.data.results.length > 0) {
          setSearchResult({
            ...res.data.results[0],
            expanded: false,
          });
        } else {
          setSearchResult(null);
        }
      } catch (error) {
        console.error("Search API failed:", error);
        setSearchResult(null);
      }
    };

    fetchResult();
  }, [searchText]);

  return (
    <div className={`app ${darkMode ? "dark" : "light"}`}>
      {/* Sticky search bar */}
      <div className="search-wrapper">
        <input
          className="search-box"
          type="text"
          placeholder="Search any topic..."
          value={searchText}
          onChange={(e) => setSearchText(e.target.value)}
        />
      </div>

      <div className="container">
        <div className="top-bar">
          <h1>📘 Class 11 Biology Chapters</h1>
          <button
            className="theme-toggle"
            onClick={() => setDarkMode(!darkMode)}
          >
            {darkMode ? "🌞 Light Mode" : "🌙 Dark Mode"}
          </button>
        </div>

        {/* Conditional rendering */}
        {searchText.trim() && searchResult ? (
          <ChapterCard key={searchResult.title} chapter={searchResult} />
        ) : searchText.trim() && !searchResult ? (
          <p className="empty-message">No matching topics found.</p>
        ) : (
          // When search is empty → show all chapters from frontend
          chapters.map((chapter) => (
            <ChapterCard key={chapter.id} chapter={chapter} />
          ))
        )}
      </div>

      <ScrollToTopButton />
    </div>
  );
}

export default App;
