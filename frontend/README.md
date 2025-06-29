# Frontend

1. Project Setup with Vite  
•	Used Vite to create a fast and lightweight React project  

2. Installed Required Dependencies  
•	Installed axios for making HTTP requests to the backend:  
npm install axios  

3. Created Component: ChapterCard.jsx  
•	Displays each chapter's title and content preview.  
•	Accepts props like title, content, etc.  
•	Used in App.jsx to display all chapters.  

4. Created Component: ScrollToTopButton.jsx  
•	Displays a button that lets users scroll smoothly back to the top of the page.  
•	Button appears after scrolling down a certain distance.  

5. Created Chapter Data File: chapters.js  
To store chapter data and display in card.  

6. Main Logic in App.jsx  
•	Imported chapter data from chapters.js.  
•	Mapped over the chapters array to render ChapterCard for each.  
•	Handled search feature   
•	Used axios for API interaction.  
Your App.jsx file is the central hub of the frontend app. It:  
•	Manages theme (light/dark),  
•	Handles user search input,  
•	Connects with the backend,  
•	Displays search results or static chapters,  
•	And includes a scroll-to-top feature.  

7. Styling in styles.css  
•	Applied custom styles to:  
o	ChapterCard layout  
o	Scroll button appearance  
o	Typography, spacing, and layout across the app  

