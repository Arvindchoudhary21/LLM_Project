import { useState } from "react";

function ChapterCard({ chapter }) {
  const [expanded, setExpanded] = useState(false);

  const summary = chapter.content.slice(0, 180);
  const rest = chapter.content.slice(180);

  return (
    <div className="chapter-card">
      <h2 className="chapter-title">{chapter.title}</h2>

      <p className="chapter-content">
        {summary}
        {expanded && <span className="extra-content">{rest}</span>}
      </p>

      <button
        onClick={() => setExpanded(!expanded)}
        className="toggle-button"
      >
        {expanded ? "🔼 Show Less" : "🔽 Read More"}
      </button>
    </div>
  );
}

export default ChapterCard;
