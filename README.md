# **Technostalgia - a website where you can reminisce about obsolete technologies**
Technologies are developing at an unprecedented pace. It is easy to forget about older technologies that were once cutting edge but are now obsolete and risk being forgotten. This site gives people the opportuntity to look at older technologies, comment on them and add  technologies to the site.
![Technostalgia home page image](static link to image)
## Visit the deployed website
[![Technostalgia website](static link to website "Visit the deployed site here")](https://conac-technostalgia.herokuapp.com/)

## User Experience (UX)

### Project Goals

#### Visitor Goals
#####All visitors to the site should be able to; 
1. Understand what the website is about and navigate it intuitively.
2. View technologies on the site, search by category, or search by keyword.
3. View all the comments about any technology.
4. Register for the website.

#####In addition to the those aspects available to all users, all registered users should be able to log in to the website. When logged in they should be able to;
1. Add new technologies to the site.
2. Edit or delete the technolgies they have added.
3. Add comments to any technology.
4. Edit or delete the comments they have added to a technology.
5. View their profile page
6. Log out

#####Admin user should be able to
1. Add, edit or delete categories.
2. Edit or delete any comment.
3. Edit or delete any technology.


#### Registered User goals

#### Developer and Business goals

#### User Stories

## Strategy
The site should be a simple and attractive  with sufficient activity to engage visitors, encourage them to sign up and return to the site.

Objective Requirement;         To encourage visitors to register with the site.

Functional requirements; 	    To provide a collection of technologies that users can view. To provide a facility for users to register, log in and log out of the site. To provide registered users with the facility to add, edit and delete their own technologies and comments.

Non-functional requirements; 	The site should be attractive and intuitive.

## Scope

## Structure
The site has 12 pages, These will be home, registration, login, profile, technologies, add technology, edit technology, comments, edit comment, manage categories, add category and edit category. The user is directed back to an appropriate location after each functionality is complete.
## Skeleton
The **home** page  introduces the site. 
The **registration** page is where the user can register for the site and is navigated to from the navbar.
The **login** page is where returning users can log in to the site.
The **profile** page displays all the technologies that the current user has added and all the comments they have made. From this page the user can navigate to the **edit technologies**  or **edit comments** pages. Technologies can also be deleted from the profile page and all comments related to the technology are automatically deleted too.
The **technologies** page is where each technology is displayed in a card. The page can be searched by keyword or by category From each card the user can navigate to the **comments** page related to that technology where they can read all the comments that have been made about that technology and (if registered) they can add comments.
The **add technology** page is accessed from the navbar (for registered users only) and has a form where the user can add a new technology.
The **manage categories** page is accessed from the navbar (for admin users only) from here an admin user can navigate to the **edit category** and **add category** pages. Categories can be deleted from the manage technology page. When a category is deleted all associated technologies and comments are also deleted.
 
## Surface/Design (Design Choices fonts, icons, colours, styling, backgroundss)

### Imagery
The overall feel of the site was to be bright, fun, simple and intuitive.
### Colour scheme
According to Shane Barker in ["The Psychology of Color in Web Design"](https://www.vandelaydesign.com/the-psychology-of-color-in-web-design/), pink raises emotions of fun and romance and is "ideal for websites that hearken back to olden days". The predominantly pink background image was picked with this in mind. The colours from the image were identified using [imagecolorpicker.com](https://imagecolorpicker.com/) and used throughout the site.
 A [minimum contrast ratio](https://developer.mozilla.org/en-US/docs/Web/Accessibility/Understanding_WCAG/Perceivable/Color_contrast) of 4.5:1 for small text and 3:1 for large text is recommended. There were a range of combinations of backgrounds and text across the site and their contrast ratios ranged from the best 10.45 (#f3e5f5 pink backgound of site and #000 - black text) to 4.81 (#ab47bc navbar backgound purple lighten-1 and #fff white text)

### Typography
The fonts were found on google font. The 'Press Start 2P' used for the title was picked because it looked a bit like a 1980s arcade game font and the 'Ubuntu Mono' was recommended by google fonts as a popular pairing and it was clear and very readable.
## Features
- Responsiveness on all device sizes.
- A home page which dynamically displays images of all the categories that have been added to the site.
- A navigation bar on main page that displays navigation relevent to the user type.
- A page to view all the technologies that are on the site
- A way of searching all the technologies with means of dynamically populating of category drop down menus to include all added categories.
- A means of allowing visitors to register.
- A means of allowing registered users to add technologies and comments. 
- A means of allowing registered users to edit or delete technologies and comments that they have added.
- A means of allowing an admin user to add, edit and delete categories.
- A means of dynamice populating of category drop down menus to incluse all added categories.

## Wireframes

## Future features
Polls, rattings, favorites.

## Languages used
[HTML5](https://en.wikipedia.org/wiki/HTML5)

[CSS](https://en.wikipedia.org/wiki/CSS)

[python](https://www.python.org/)

## Frameworks, Libraries and online resources used
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
- The space invader image for the favicon was found in [iconfinder.com](https://www.iconfinder.com/)
- The favicon image was converted to an .ico file using [favicon.io](https://favicon.io/)
- Instructions for adding the favicon were found on [flask.palletsprojects.co](https://flask.palletsprojects.com/)
- The following websites were used for problem solving [stackoverflow.com](https://stackoverflow.com/), [w3schools.com](https://www.w3schools.com/), [geeksforgeeks.org](https://www.geeksforgeeks.org/), [pythonmorsels.com](https://www.pythonmorsels.com/)
- The html code was formatted using [webformatter.com](https://webformatter.com/html)
- Information about automatically formatting  python with [black](https://pypi.org/project/black/) was found on [freecodecamp.org](https://www.freecodecamp.org/news/auto-format-your-python-code-with-black/)
- The images were formatted using [https://tinypng.com/](https://tinypng.com/)
- Help on datetime was found on [pythonexamples.org](https://pythonexamples.org/python-datetime-now/)
- Information on jinja filters was found on [exponea.com](https://docs.exponea.com/docs/filters)
- Information on date formatting was found on [jquery-az.com](https://www.jquery-az.com/python-datetime-to-string/) and [sendwithus.com](https://support.sendwithus.com/jinja/jinja_time/)
- I made use of tutorials from [www.freecodecamp.org](https://www.freecodecamp.org/), [codemy.com](https://codemy.com/) and [www.udemy.com](https://www.udemy.com/)
## Images
- The images were stored in [Imgur](https://i.imgur.com/)
- The Walkman image is by [Florian Schmetz on unsplash.com](https://unsplash.com/photos/Rks6FTfX5OU)
- The cassette tape image is in by [Volodymyr Hryshchenko on unsplash.com](https://unsplash.com/photos/D5_cfqMAY0Y)
- The motorola image is from [oneandroid.net/](https://oneandroid.net/)
- The floppy disk image is by [Fredy Jacob in unsplash.com](https://unsplash.com/photos/t0SlmanfFcg)
- The acoustic coupler imager was found on [arstechnica.com](https://arstechnica.com/)
- The credit card machine image was found on[singletrackworld.com](http://singletrackworld.com/)
- The punch card image was found on [www.palvenn.no/](http://www.palvenn.no/)
- The homepage background image is by [Hello I'm Nik in unsplash.com](https://unsplash.com/photos/6nqbKX5UI9I)
## Testing.
Bugs identified during development and testing and their solutions can be seen [here](link to image).
### Validation
- HTML and CSS. All pages of the quiz were tested by direct input into [validator.w3.org](https://validator.w3.org/) for html and [jigsaw.w3.org](https://jigsaw.w3.org/css-validator/) for css and errors identified were corrected until no errors were showing in either validator. 

- Lighthouse Audits. The quiz’s Performance, Accessibility, Best Practices and SEO were assessed by [Chrome Lighthouse](https://chrome.google.com/webstore/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk) and the results of this are [here](assets/images/lighthousereport.png).
- Manual Testing. Extensive use was made of console.log() at every step of the functionality development and each time an error was noted it was addressed before proceeeding.
The app was tested on Google Chrome, Internet Explorer, Microsoft Edge and Safari browsers.
It was viewed on a variety of devices. Friends and family members reviewed the site to identify bugs and give feedback on user experience. The code was submitted for peer-review in Code Institute's peer-code-review channel in [slack.com](https://app.slack.com/). 
### Testing User Stories from User Experience (UX) Section.
1. Understand what the website is about.
2. View all technologies on the site, or view by category, or select specific technologies.
3. Users should be able to register for the website.
4. Users should be able to login to the website.
5. Logged in users should be able to post new technologies.
6. Logged in users should be able to edit and delete their own additions to the site.
7. Logged in users should be able to post comments on technologies.
8. Logged in users should be able to edit and delete comments on technologies.
9. Logged in users should be able to Logout easily.
10. The site administrator should be able to add new categories to teh site and these should automatically be included in all menus.
## Changes over course of development

## Known Bugs

## Deployment
### The project was deployed to Heroku in the following way. 
In Heroku.com
1. 'New' was selected.
2. 'Create new app' was selected.
3. app-name was added and region selected
4. 'Create app' was selected.
5. The app was set up to automatically deploy from the associated GitHub repository by selecting the 'GitHub' Deployment method, ensuring the correct repository was selected, adding the repository name and clicking 'Search'. Once the correct repo is found 'Connect' was clicked
6. Before enabling automatic deployment Heroku had to be told the environment variables securely. This was done by clicking on 'Settings' for the app, selecting 'Reveal Config Vars' and adding the IP, PORT, SECRET_KEY, MONGO_URI and MONGO_DBNAME and clicking 'Hide Config Vars'.
7. In the Deploy tab of the app select 'Enable Automatic Deploys' and then as the project only has one branch 'main' was chosen as the branch to deploy and 'Deploy Branch' was selected. After a few minutes, when Heroku was received the code from GitHub and built the app a message appears saying 'Your app was successfully deployed.' The app is then deployed and automaytically updated when code is pushed to GitHub.

### Forking the GitHub Repository
The  GitHub Repository can be forked to make a copy of the original repository on the GitHub account to view and/or make changes without affecting the original repository in the following way.
1.	By logging in to GitHub and locating the [GitHub Repository](https://github.com/ConacBreslin/technostalgia).
2.	Selecting the "Fork" button at the top of the Repository (it is located above the "Settings" Button and over to the right).
3.	There should then be a copy of the original repository in your GitHub account.

### Making a Local Clone
1.	By logging in to GitHub and locating the [GitHub Repository](https://github.com/ConacBreslin/technostalgia).
2.	Under the repository name, clicking the dropdown button marked “Code” and then selecting "Clone or download".
3.	Copying the link under "Clone with HTTPS", to clone the repository using HTTPS.
4.	Opening Git Bash.
5.	Changing the current working directory to the location where you want the cloned directory to be made.
6.	Typing git clone, and pasting the URL copied in Step 3.
7.	Pressing Enter to create the local clone.## Credits

## Acknowledgements
I would like to thank my mentor Chris Quinn whose advice is always perfectly judged.  
I would like to thank many tutors in Code Institute for being unfailingly helpful, patient and knowledgeable and without whom I never would have got this far.   
I would like to thank AMy O'Shea from Code Institute for her [excellent presentation](https:) on preparation for MS3 projects that helped me enormously is getting started.  
I would like to thank my family and friends for all their support and feedback.

