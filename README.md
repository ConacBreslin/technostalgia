# **Technostalgia - a website where you can reminisce about obsolete technologies**
Technologies are developing at an unprecedented pace. It is easy to forget about older technologies that were once cutting edge but are now obsolete and risk being forgotten. This site gives people the opportuntity to reminisce about these technologies.

## Visit the deployed website
[![Technostalgia](static/images/banner.png "Visit the deployed site here")](https://conac-technostalgia.herokuapp.com/)

## User Experience (UX)

### Project Goals

The site was created to enagage visitors so that they will want to register and visit regularly. It was built to fulfill the requirements of Code Institutes's Diploma in Full Stack Development Milestone 3 project.

#### Visitor Goals

To enjoy visiting the site, to remind them of techologies they may have forgotten or never known and for them to motivated to interact with the site and to return often.

#### User Stories

##### All visitors to the site should be able to; 
1. Understand what the website is about and navigate it intuitively.
2. View technologies on the site, search by category, or search by keyword.
3. View all the comments about any technology on the site.
4. Register with the site.

##### In addition to the those aspects available to all users, all registered users should be able to log in to the website. When logged in they should be able to;
5. Add new technologies to the site.
6. Edit or delete the technolgies they have added.
7. Add comments to any technology.
8. Edit or delete the comments they have added to a technology.
9. View their profile page
10. Log out

##### Admin user should be able to
11. Add, edit or delete categories.
12. Edit or delete any technology.
13. Edit or delete any comment.

## Strategy
The site should provide a platform for people interested in obsolete technologies to come and be reminded of them and to share their experience of them.
- Objective Requirements;         To encourage visitors to visit the site, register with it and to return frequently.
- Functional requirements; 	    To provide a collection of technologies that users can view. To provide a facility for users to register, log in and log out of the site. To provide registered users with the facility to add, edit and delete their own technologies and comments.
- Non-functional requirements; 	The site should be attractive and intuitive.

## Structure
The site starts with a home page. From here there are four main areas to which visitors may  navigate depending on status (visitor, registered visitor, administrator).
1. The registration and login in pages are available to all users. The logout page is available to logged in users.
2. The page to browse technologies is available to all users and from this page users can navigate to the comments page where all users can view the comments that have been added about a selected technology selected. Registered, logged in users can add comments.
3. All registered, logged in users can access their profile page. This lists all the technologies and comments they have added to the site. From this page they can navigate to edit either their technologies or their comments.
4. Any user designated as an 'admin' user also has access to a page where the site can be managed. From this page categories can be added, and all the technologies and comments on the site can be editted or deleted.

## Skeleton

The wireframes for the site can be seen [here](static/images/wireframes1.jpg) and [here](static/images/wireframes2.jpg)

There are 12 pages on the site.
The **home** page  introduces the site. It has a carousel displaying images of all the technologies that are on the site. Other pages can be navigated to from the navbar at the top of this. 

The **registration** page has a form which a visitor can complete to register for the site. It contains a link to the login page for visitors who are already registered. 

The **login** page has a form for returning registered users to log back in to the site. It contains a link to the registration page for non-registered visitors.

The **technologies** page is where each technology and its information is displayed. The page can be searched by keyword or by category. Each technology is in a card from where the visitor can go to the **comments** page related to that technology. Here they can read all the comments that have been made about that technology and (if registered and logged in) they can add comments through a form.

The **add technology** page is accessed from the navbar (for registered, logged in users only) and has a form where the user can add all the necessary details of a new technology.

A  **profile** page is accessible to registered, logged in users from the navbar. It displays all the technologies that the current user has added and all the comments they have made. From this page the user can go to the **edit technologies** or **edit comments** pages. Technologies and comments can be deleted from the profile page. If a technology is deleted all comments about the technology are also deleted. 

The **manage the site** page is accessed from the navbar for admin users only. From here an admin user can link to the **add category** page to add a new categoy. Categories can be deleted from the page. When a category is deleted all associated technologies and comments are also deleted. Admin users can navigate to the **edit category** page. They can see all the technologies and comments that have been added to the site and can delete a technology or comment from that page or go to the pages for editting technologies or comments.  
 
## Surface/Design (Design Choices fonts, icons, colours, styling, backgroundss)

### Imagery
The overall feel of the site was to be bright, fun and simple.
### Colour scheme
According to Shane Barker in ["The Psychology of Color in Web Design"](https://www.vandelaydesign.com/the-psychology-of-color-in-web-design/), pink raises emotions of fun and romance and is "ideal for websites that hearken back to olden days". The backgound image was picked with this in mind and the colours from it were identified using [imagecolorpicker.com](https://imagecolorpicker.com/) and used throughout the site.
 A [minimum contrast ratio](https://developer.mozilla.org/en-US/docs/Web/Accessibility/Understanding_WCAG/Perceivable/Color_contrast) of 4.5:1 for small text and 3:1 for large text is recommended. There were a range of combinations of backgrounds and text across the site and their contrast ratios ranged from the best 10.45 (#f3e5f5 pink backgound of site and #000 - black text) to 4.81 (#ab47bc navbar backgound purple lighten-1 and #fff white text)

### Typography
The fonts were found on google font. The 'Press Start 2P' used for the title was picked because it looked like a 1980s arcade game font and the 'Ubuntu Mono' was recommended by google fonts as a popular pairing and it was clear and easily readable.
## Features
- Responsiveness on all device sizes.
- A nav bar that displays links dependent to the user type.
- A home page which dynamically displays images of all the categories that have been added to the site.
- A registration procedure which ensures each field meets the specified requiremnet, ensures every registered user has a unique username and a method of securing passwords. 
- A login page that ensures the users username and passwords match those with which they registered.
- A logout procedure that closes the session.
- A method of searching the technologies by keyword or category name.
- The ability to allow admin users to create, edit and delete categories.
- The ability for registered, logged in users to create, edit and delete technologies.
- The functionality so that when a technology is deleted all the comments associated iwth that technology are also deleted.
- A check that user wants to perform irreversible actions before they do so.
- The ability for registered, logged in users to create edit and delete comments

## Future features
To increase the interactivity of the site future features could include polls, ratings, favorites.

In the future users should be able to edit the technologies name (see known bugs).

It would be nice if the admin user could search/sort the technologies and comments on the manage the site page.

## Languages used
[HTML5](https://en.wikipedia.org/wiki/HTML5)

[CSS](https://en.wikipedia.org/wiki/CSS)

[Python](https://www.python.org/)

[JavaScript](https://en.wikipedia.org/wiki/JavaScript)


## Frameworks, Libraries and online resources used
- [jQuery](https://jquery.com/) javaScript 
- The [Flask](https://flask.palletsprojects.com/en/2.0.x/) mictroframework was used to build the app.
- The [Jinja](https://jinja.palletsprojects.com/en/3.0.x/) templating engine was used.
- [Balsamiq](https://balsamiq.com/wireframes/) was used to create the wireframes.
- Gits's [gitpod](https://www.gitpod.io/) was used for writing and editing code, and for submitting and pushing to GitHub.
- [Heroku](https://id.heroku.com/login) was used to deploy the app.
- [Mongodb](https://www.mongodb.com/) database was used to store data.
- [GitHub](https://github.com/) was used for storing the code after being pushed from Git.
- [RandomKeygen](https://randomkeygen.com/) was used to generate a secret key for the app.
- [Materilaize 1.0.0](https://materializecss.com/) was used for responsiveness and styling.
- [Google Fonts](https://fonts.google.com/) was used to choose and import the font.
- Foreground/Backgound contrast was checked using [contrast-ratio.com](https://contrast-ratio.com/). 
- The space invader image for the favicon was found in [iconfinder.com](https://www.iconfinder.com/).
- The favicon image was converted to an .ico file using [favicon.io](https://favicon.io/).
- Instructions for adding the favicon were found on [flask.palletsprojects.co](https://flask.palletsprojects.com/).
- The following websites were used for problem solving [stackoverflow.com](https://stackoverflow.com/), [w3schools.com](https://www.w3schools.com/), [geeksforgeeks.org](https://www.geeksforgeeks.org/), [pythonmorsels.com](https://www.pythonmorsels.com/), [teamtreehouse.com](https://teamtreehouse.com/) and [css-tricks.com](https://css-tricks.com/).
- The html code was formatted using [webformatter.com](https://webformatter.com/html).
- Information about automatically formatting  python with [black](https://pypi.org/project/black/) was found on [freecodecamp.org](https://www.freecodecamp.org/news/auto-format-your-python-code-with-black/)
- Help on datetime was found on [pythonexamples.org](https://pythonexamples.org/python-datetime-now/).
- Information on jinja filters was found on [exponea.com](https://docs.exponea.com/docs/filters).
- Information on date formatting was found on [jquery-az.com](https://www.jquery-az.com/python-datetime-to-string/) and [sendwithus.com](https://support.sendwithus.com/jinja/jinja_time/).
- I made use of tutorials from [www.freecodecamp.org](https://www.freecodecamp.org/), [codemy.com](https://codemy.com/) and [www.udemy.com](https://www.udemy.com/).
- Code from https://regexr.com/ was used to set pattern for email and url validation.
- Documents were converted to .jpg using [freeconvert.com](https://www.freeconvert.com/)
## Images
- The images were stored in [Imgur](https://i.imgur.com/).
- The images were formatted using [https://tinypng.com/](https://tinypng.com/).
- The homepage background image is by [Hello I'm Nik in unsplash.com](https://unsplash.com/photos/6nqbKX5UI9I).
- The Walkman image is by [Florian Schmetz on unsplash.com](https://unsplash.com/photos/Rks6FTfX5OU).
- The cassette tape image is in by [Volodymyr Hryshchenko on unsplash.com](https://unsplash.com/photos/D5_cfqMAY0Y).
- The motorola image is from [oneandroid.net/](https://oneandroid.net/).
- The floppy disk image is by [Fredy Jacob in unsplash.com](https://unsplash.com/photos/t0SlmanfFcg).
- The acoustic coupler imager was found on [arstechnica.com](https://arstechnica.com/).
- The credit card machine image was found on[singletrackworld.com](http://singletrackworld.com/).
- The punch card image was found on [www.palvenn.no/](http://www.palvenn.no/).
- The moog photo was foung on [(https://moogfoundation.org/)](https://moogfoundation.org/).
- The mellotron photo was found on [https://bluebuzzmusic.com](https://bluebuzzmusic.com/).

Other images on the site were added by users.

## Testing.
Bugs identified during development and testing and their solutions on 2 pages [page 1](static/images/bugsone.png), [page 2](static/images/bugstwo.png).
### Validation
- HTML code for each individual page was validited by direct input into [validator.w3.org](https://validator.w3.org/). The results of this can be seen  [here](static/images/htmlvalidation.jpg))
- CSS code was tested repeatedly by direct input into [jigsaw.w3.org](https://jigsaw.w3.org/css-validator/) until it got a 'Congratulations! No error found!' message.
- JavaScript was checked using [jshint](https://jshint.com/). There were no errors and the warnings were checked, corrected where appropriate and otherwise left.
- Python code was tested repeatedly with [pep8 online validator](http://pep8online.com/) until the vaildator deemed it 'All right'.
- Lighthouse Audits. The site’s Performance, Accessibility, Best Practices and SEO were assessed by [Chrome Lighthouse](https://chrome.google.com/webstore/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk) and the results of this are [here](static/images/lighthousereport.png).
- Manual Testing. At every step of development the errors highlighted in the code were addressed before proceeeding.
The app was tested on Google Chrome, Internet Explorer, Microsoft Edge and Safari browsers.
It was viewed on a variety of devices. Friends and family members reviewed the site to identify bugs and give feedback on user experience. The code was submitted for peer-review in Code Institute's peer-code-review channel in [slack.com](https://app.slack.com/). 
### Testing User Stories from User Experience (UX) Section.
 
1. All visitors should be able to understand what the website is about and navigate it intuitively.
- The home page has a title that explains what the site is about and can navigate to areas from the navbar
2. All visitors should be able to view technologies on the site, search by category, or search by keyword.
- The technologies page link is is visible on the navbar for all visitors. It shows all the technologies in cards to all visitors to the site. This page is headed by a search form which can search the technologies by keyword or category.
3. All visitors should be able to view all the comments about any technology.
- All visitors can navigate to the comments page from within the technologies card.
4.  All visitors should be able to register for the website.
- The registration link is visible on the navbar for all visitors. It has a form for all the required registration details. All fields have specifications and requirements.
5. Logged in visitors should be able to add new technologies to the site.
-  The add a technology link is only visible on the navbar for logged in users. This page has a form which insists on the user filling in all the details necessary for a technology. It has guidance on what is needed through placeholder text.
6. Logged in visitors should be able to edit or delete the technologies they have added.
- This functionality is available to registered, logged in users from their profile page. The link to the profile page is only visible to logged in users. Unfortunately due to the way the comments were linked to the technology the ability for users to edit the technology name had to be disabled.
7. Logged in visitors should be able to add comments to aon a form on the comments page. 
- This facility is available to registered, logged in users when they have navigated from the technolgy's card on the technologies page. Although anyone can wrote a comment on the card, if a an unregistered user tries to submit a comment they get a flash message explaining this and get redirected to the registration page.
8.  Logged in visitors should be able to edit or delete the comments they have added to a technology.
- This functionality is available to registered, logged in users from their profile page. The link to the profile page is only visible to logged in users.
9. View their profile page
- The link to the profile page is  visible to logged in users.
10. Log out
- The log out option is displayed on the navbar only when the user is logged in. When a user logs out the user is removed from the session cookie and the navbar goes back to the display for non-logged in users.
11. Admin users should be able to add, edit or delete categories.
- This functionality is available to admin users from the 'manage the site' page. The link to this is only visible to users designated as admin in the database.
12. Admin users should be able to edit or delete any technology.
- This functionality is available to admin users from the 'manage the site' page. The link to this page is only visible to users designated as admin in the database. All the technologies are listed on this page regardless of who added them.
13. Admin users should be able to edit or delete any comment.
- This functionality is available to admin users from the 'manage the site' page. The link to this page is only visible to users designated as admin in the database. All the technologies are listed on this page regardless of who added them.
## Changes over course of development
The manage_categories site was expanded to manage_site as it was easier to let admin users manage comments and technologies from there.

## Known Bugs
1. It was noted during testing that if a logged in user was allowed to change the name of a technology it lost the associated comments. This is because the technology name was used as the check to match comments and technologies. If the name got changed this check would not match and for this reason the facility to allow users to edit the technology name was removed. If time allowed I could have used unique Ids to match technologoies and  comments or added the comments as a list to the technology and iterated through this to display them. 
2. During testing it was noted that in the search facility on the technologies page, if a user selected a category the result would (as intended) show all the technologies in that category however if any of the words in the category name appeared in any of the fields included in the index then they also got displayed. If there was time I would make this search function more specific.
3. When tested it was noticed that the carousel overlaps the background image on some mobile phones and does not look great.
4. The submit and clear buttons in the form to add a comment can get overlapped or lost on some mobiles.
5. Although the placeholder text for adding the technology image says it must be a url, there is no check to ensure it is and the form will accept an input that does not result in an image being uploaded.
6. On small screens sometimes some of the text overflow the buttons.


## Deployment
### The project was deployed to Heroku in the following way. 
In Heroku.com
1. 'New' was selected.
2. 'Create new app' was selected.
3. The app-name was added and region selected
4. 'Create app' was selected.
5. The app was set up to automatically deploy from the associated GitHub repository by selecting the 'GitHub' Deployment method, ensuring the correct repository was selected, adding the repository name and clicking 'Search'. Once the correct repo was found 'Connect' was clicked
6. Before enabling automatic deployment Heroku had to be told the environment variables securely. This was done by clicking on 'Settings' for the app, selecting 'Reveal Config Vars' and adding the IP, PORT, SECRET_KEY, MONGO_URI and MONGO_DBNAME and clicking 'Hide Config Vars'.
7. In the Deploy tab of the app 'Enable Automatic Deploys'  was selected and as the project only has one branch 'main' was chosen as the branch to deploy and 'Deploy Branch' was selected. After a few minutes, when Heroku had received the code from GitHub and built the app a message appeared saying 'Your app was successfully deployed.' The app was then deployed and automatically updated when code wass pushed to GitHub.

### Forking the GitHub Repository
The  GitHub Repository can be forked to make a copy of the original repository on the GitHub account to view and/or make changes without affecting the original repository in the following way.
1.	By logging in to GitHub and locating the [GitHub Repository](https://github.com/ConacBreslin/technostalgia).
2.	Selecting the "Fork" button at the top of the Repository located above the "Settings" Button and  to the right.
3.	There should then be a copy of the original repository in your GitHub account.

### Making a Local Clone
1.	By logging in to GitHub and locating the [GitHub Repository](https://github.com/ConacBreslin/technostalgia).
2.	Under the repository name, clicking the dropdown button marked “Code” and then selecting "Clone or download".
3.	Copying the link under "Clone with HTTPS", to clone the repository using HTTPS.
4.	Opening Git Bash.
5.	Changing the current working directory to the location where you want the cloned directory to be made.
6.	Typing git clone, and pasting the URL copied in Step 3.
7.	Pressing Enter to create the local clone.

## Acknowledgements
I would like to thank the following people;
- my mentor Chris Quinn whose advice is always perfectly judged. 
_ my temporary mentor Daisy McGirr for taking me on at short notice and giving me useful, practical advice. 
- Tim Nelson for his excellent walkthough projects in the Code Institute's diploma programme that provided essential guidance in the development process of this flask app.
- the many tutors in Code Institute for being unfailingly helpful, patient and knowledgeable throughout the hours and hours I spent online with them.   
- Amy O'Shea from Code Institute for her [excellent presentation](https://www.youtube.com/watch?v=f7kpF8huK_8) on preparation for MS3 projects that helped me enormously is getting started.  
- my family and friends for all their support and feedback.

