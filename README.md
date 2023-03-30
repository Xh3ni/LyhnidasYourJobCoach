<h1 align="center">If opportunity doesn't knock, build a door.</h1>
<h2 align="center"><strong>Lyhnidas Your Job Coach</strong></h2>

### **Live Site:**
[The Newsbox](https://lyhnidas-your-job-coach.herokuapp.com/)

### **Repository:**
[The Newsbox Repository](https://github.com/Xh3ni/LyhnidasYourJobCoach)

### **Developer:**
Xhensila Stambolliu

# About
This is a full-stack project built using Django, Python, HTML, CSS, and JavaScript. 
I have created this website for my fourth project of the codeinstitute's Diploma in FullStack Development. It is a  website which helps job seekers and recruiters come together and hire easily built using Django Framework.

## Table of Contents
1. [Project Aim](#aim)
2. [User Experience]()
    1. [Target Audience](#database)
    2. [Apps]()
    3. [Design](#design)
    4. [Scope](#scope)
    5. [User stories](#user-stories)
3. [Technical]()
    1. [Agile](#agile)
4. [Features](#features)
5. [Marketing](#marketing)
6. [Bugs](#Bugs)
7. [Technologies Used](#tech)
8. [Testing](#validation)
9. [Deployment](#deployment)
10. [Credits](#credits)
11. [Acknowledgments](#acknowledgments)

### Aim <a name="aim"></a>
To create a web application which will allow helps job seekers and recruiters come together and hire easily.
A user can easily access the website to search and apply for a job, and also, a user can add a job as a recruiter.

## Database Design <a name="database"></a>
[Database Schema] 

#### **User Account**
This app is use for all authentication, profile and account purposes. I am using the allauth 
package to handle the authentication. Also, I am only using account login providers, so we are free from any password handling and recovery issues.
<br/><br/>
<hr>

**Login**


![Login](https://res.cloudinary.com/dmlbtywv4/image/upload/v1680203688/signin_ad4voy.png)

**SignUp**

![Sign Up](https://res.cloudinary.com/dmlbtywv4/image/upload/v1680203688/signup_bttnc7.png)

**base.html**
This is the base of the entire website which each other webpage extends from. 
It contains the header and footer of the website.
It links this template to all the CSS and JS files.
I have used Bootstrap4 CSS and JS files and a pair of other CSS files.
Thereare  two sections for the navigation bar, one for the recruiter side and the other for the candidate side.
Also,there is a button to move to the other side.
<br/><br/>
<hr>
The default opening is on the candidate side.

![Candidate Nav Not Login](https://res.cloudinary.com/dmlbtywv4/image/upload/v1680203177/candidate_nav_notlogin_lhkhxv.png)
<br/><br/>
<hr>

The default opening is on the recruiter side.

![Recruiter Nav Not Login](https://res.cloudinary.com/dmlbtywv4/image/upload/v1680203177/recruiter_nav_notlogin_uu7smj.png)

<br/><br/>
<hr>

It also has the login button when the user is not signed in, and when loged in, the login button disappears, and the logout button appears.

![Candidate Nav Login](https://res.cloudinary.com/dmlbtywv4/image/upload/v1680204357/Successfully_signed_in_as_User_k68xxf.png)

<br><br>
<hr>
Recruiter Nav after Login

![Recruiter Nav Login](https://res.cloudinary.com/dmlbtywv4/image/upload/v1680205174/recruiter_nav_login_snu6ta.png)

<br><br>
<hr>
The footer is the same. There are some links to pages and some details about the website and some social media handles.
All the social media links open on a new page and redirect to Lyhnidas Pages.

![Footer](https://res.cloudinary.com/dmlbtywv4/image/upload/v1680204824/footer_ymimtw.png)

<br><br>
<hr>

**Sign Out**

![SignOut](https://res.cloudinary.com/dmlbtywv4/image/upload/v1680204357/YouhaveSignOut_vh2v4z.png)


#### **Candidates App**

In the candidates part, are all the things relevant to the job seekers (candidates), which consists of the job search, job application and saving of jobs. It also shows the current status of the application, whether its accepted, pending or rejected. Also, there is an intelligence search feature built-in which shows the jobs which are the best fit for the user 
based on the skills skills and job requirements.

Firstly is defined a CHOICES variable which consists of four choices (Full Time, Part Time, Internship, Remte),
which is used in the Profile class.

`Profile`— This class contains all the information about the candidate. It is linked to the default 
User model of Django. It also consists of the full name, country, location, resume, graduation year and 
looking for an option. It also has a slug option, which helps to generate a slug from the user variable. 
Resumes are stored in cloud storage. It also has a function which returns its absolute URL with the help of a 
slug.
`Skill`- This is the model class which contains the skill and a foreign key linking to the User.

`SavedJobs` - This is the class of the model which consists of three parameters — job, user and date_posted. 
Job links it to the Job model from the recruiters' App, user links with the User Model, and date uses the current time via the Django timezone. The purpose is to store the jobs saved by a user.

`AppliedJobs` - This is the class of the model which consists of three parameters — job, user and 
date_posted. Job links it to the Job model from the recruiters' App, user links with the User Model, and 
date uses the current time via the Django timezone. The purpose is to store the jobs applied by a user. It is very similar to the Saved Jobs class.

**forms.py**
The forms part consists of two forms which is used for the candidates part of the website:
ProfileUpdateForm and NewSkillForm. 

1. ProfileUpdateForm — The purpose of this form is to enable a user to update his candidate profile. 
The user can update all the parameters of the Profile model class.

2. NewSkillForm — This form is used to add a new skill to the skills model class for a user.


#### **Recruiters App**
In the recruiters part, there are mostly all the things which are relevant to the recruiters and hiring companies,
which consist of the job posting, getting candidates applying on job posts, selecting these candidates and also 
viewing the resumes of all the candidates on the database. It also shows the current status of the job post, 
like how many have applied and can see the applicants list.
Then can select or reject them based on their profile and resume. 
Also, there is an intelligence search feature built-in which shows the candidates who are the best fit
based on their skills and job requirements to save time.

Firstly is defined a CHOICES variable which consists of four choices (Full Time, Part Time, Internship, Remte),
which is used in the Job class.

`Job` - This class contains all the information relevant to the job post. 
It has a <i>recruiter</i> variable which links it to the Recruiter posting the job post. 
It also has all details about the job, like the title, location, company, description, skills required 
and the type of the job, whether it is a full-time job, part-time job, an internship or a remote opportunity. 
There is also a link section which can be left blank (only required when the recruiter wants to accept applicants on their website). 
It also has a slug that helps create unique slugs based on the job title.

`Applicants` - This class stores all the data related to the candidates who have applied to a particular job post. 
It has a job variable linking it to the relevant job, an applicant variable which links it to the candidate who applied and a date when the candidate applied.

`Selected` - This is the class which stores all the data related to the candidates 
who have been selected for a particular job post. 
It has a job variable linking it to the relevant job, an applicant variable which 
links it to the candidate who was selected and a date when the candidate was selected.

**forms.py**

The form consists of two forms which is used for the recruiters part of the website:
NewJobForm and JobUpdateForm.

1. NewJobForm — The purpose of this form is to enable a recruiter to post a new job.

2. JobUpdateForm— Recruiters use this form to update an existing job post.

## Scope <a name="scope"></a>

 * A simple, straightforward, intuitive UX experience;
 * Explicit content;
 * An easy navigation for the user through all the pages and features;
 * A site that is visually appealing on all screen sizes.

### Structure

* A clear and straightforward layout is in place to ensure users can navigate intuitively and have an enjoyable browsing experience.
* Mobile navigation is the same on all pages to ensure easy navigation.
* Footer is fixed on the bottom with links to social media.

## User Experience

### User Stories <a name="user-stories"></a>

*Epic: Viewing & Navigation of the web app as a Job Seeker works as expected
1.	As a ... first time user... I can... see the home page of the website and jobs so that I can ...decide whether or not I should sign-up...
2. As a ...first time user... I can ...easily navigate to the log in so that I can ...create a profile...
3. As a ...first time user, as a candidate... I want to be able to... know what is expected of me on the home page so that I can ...easily navigate and find information...

* EPIC: Registration & User accounts work as expected
4. As a ...Candidate.. I can be able to ...easily login and log out... so that I can ...ensure my account is secure...
5. As a ...candidate... I can be able to ...have a personalised user profile... so that I can ...view and update my details...
6. As a ...Recruiter... I can be able to ...easily login and log out... so that I can ...ensure my account is secure...

* Epic: Job Sorting & Searching work as expected
7. As a ...candidate... I can be able to ...search for a job by title or locaton... so that I can ...find a specific job I'm interested in...
8. As a ...candidate... I can ...see and access all job listed... so that I can ...apply on different job positions....

* Epic: Applying & Saving Jobs work as expected
9. As a ...candidate... I can ...read/ apply/ save a job... so that I can ...ensure maximum engagement in my profile...
10. As a ...candidate... I can be able to ...read/ apply/ save a job... so that I can ...alter how I would like my job application to look to allow for maximum engagement...

*Epic: Viewing & Navigation of the web app as a Recruiter works as expected
11. As a ...first time user... I can ...see the home page of the website and jobs... so that ...I can decide whether or not I should sign-up...
12. As a ...first time user as a recruiter... I want to be able to ...know what is expected of me on the home page... so that I can ...easily navigate and find information...
13. As a ...first time user... I can ...easily navigate to the log in... so that I can ...create a profile...

* Epic: Job Posting & Selecting Candidates works as expected
14. As a ...Recruiter...I can ...Read/ edit/ delete a job post & Candidates... so that I can ...ensure the perfect candidate for the job position...
15. As a ...Recruiter... I can be able ...to Read/ edit/ delete a job post & Candidates... so that I can ...ensure the perfect candidate for the job position...

* EPIC: Site management
16. As an ...admin... I can ...add/edit/update/delete a job post... so that ...maintain the site and remove any inappropriate contents...
17. As an ...admin... I can ...review all job posts... so that I can ...maintain the site and remove any inappropriate post...

### Agile methodology <a name="agile"></a>

* All functionality and development of this project will be managed through GitHub issues, milestones and projects.

<summary>All sprints are described here.</summary>

* Sprint 1 19/03/23 - 20/03/23 (Finished at 21/03/23)

  + Initial setup
    - Install django
    - Install Allauth
    - Add Allauth templates to project templates
    - Create base.html
    - Create LyhnidasYourJobCoach project
    - Create style.css and footer.css
    - Create responsive navigation
  
* Sprint 21/03/23 - 23/03/23 (Finished on 23/03/23)

  + Add Recruiter app
    - Set up all Recruiters view
    - Set up recruiter details (rec_details) view
    - Set up add_job view
    - Set up edit_job
    - Set up job_detail
    - Set up all_jobs
    - Set up search_candidates
    - Set up job_candidate_search
    - Set up applicant_list
    - Set up selected_list
    - Set up select_applicant
    - Set up remove_applicant

  + Add Candidates app
    - Set up home view
    - Set up job_search_list
    - Set up job_detail
    - Set up saved_jobs
    - Set up applied_jobs
    - Set up my_profile
    - Set up edit_profile
    - Set up profile_view
    - Set up delete_skill
    - Set up save_job
    - Set up apply_job
    - Set up remove_job

    + Add Urls for Recruiters App and Candidates App

* Sprint 3 23/03/23 - 26/03/23 (Finished on 26/03/23)
    + Customise allauth templates
    - Set up templates
    - Set up neccessary views

* Sprint 4 26/03/23- 28/03/23 (finished 28/03 2023)
    + Customise login templates
    - Customise templates
    + Add messages

* Sprint 5 revising the project and making neccesary fixes 29/03/23 - 31/03/23 (Finished on 31/03/23)
    + Debug and fixes
    - Remove heroku app and reset databases to run locally
    - Add new model and databases
    - Fix views to add login required, search and category sorting functionality
    + Testing
    - Document all testing, revise code and complete README.md

### Features <a name="features"></a>
* Responsive design.
* Website title and information on the site's purpose.
* Navigation Menu (Site Wide).
* Postgress databases to store information and user login/profile information.
* Cloudinary to store static files
* CRUD Functionality
* Login functionality.
* Logout functionality.
* Ability to view all job posts.
* Ability to view job details.
* Ability to be able to search for job
* Ability to search job by title and location,
* Ability to apply, save and remove job.
* Ability to Update profile.
* Ability to see applied, Saved jobs
* Ability to see if a user is selected, rejected or in process for a job

* Ability to add and edit of job posts.
* Ability to manage applicants list and selected list
* Ability to search for candidates.

* Admin creation and management of job posts.

**Importance and Difficulty**

|       Feature         |   Difficulty   |   Importance   |
|:--------------------  |--------------- |--------------- |
|Postgress databases to |       5        |       5        |
|store information and  |                |                |
|user login/profile     |                |                |
|information            |                |                |
|:--------------------  |--------------- |--------------- |
|CRUD Functionality     |       5        |       5        |
|:--------------------  |--------------- |--------------- |
|Admin creation and     |       5        |       5        |
|management of Posts    |                |                |
|:--------------------  |--------------- |--------------- |
|Ability to view all    |       2        |       5        |
|job posts.             |                |                |
|:--------------------  |--------------- |--------------- |
|Ability to view        |       2        |       5        |
|job details            |                |                |
|:--------------------  |--------------- |--------------- |
|Ability to search      |       2        |       5        |
|for a job by title     |                |                |
|and location           |                |                |
|:--------------------  |--------------- |--------------- |
|Ability to apply,save  |       3        |       5        |
| and remove job        |                |                |
|:--------------------  |--------------- |--------------- |
|Ability to Update      |       3        |       5        |
| Profile               |                |                |
|:--------------------  |--------------- |--------------- |
|Ability to see Applied,|       3        |       5        |
|Saved Jobs             |                |                |
|:--------------------  |--------------- |--------------- |
|Ability to see selected|       3        |       5        |
|rejected, in process   |
|candidates             |                |                |
|:--------------------  |--------------- |--------------- |
|Ability to Add and     |       5        |       5        |
| edit a job            |                |                |
|:--------------------  |--------------- |--------------- |
|Ability to manage      |       5        |       5        |
|jobs and candidates    |                |                |
|:--------------------  |--------------- |--------------- |
|Registered user can    |       5        |       5        |
|add a job              |                |                |
|:--------------------  |--------------- |--------------- |
|Login functionality    |       3        |       5        |
|:--------------------  |--------------- |--------------- |
|Navigation Menu        |       3        |       5        |
|(Site Wide)            |                |                |
|:--------------------  |--------------- |--------------- |
|Responsive design      |       2        |       5        |
|:--------------------  |--------------- |--------------- |
|Website title and      |       1        |       5        |
|information on the     |                |                |
|the site purpose       |                |                |
|:--------------------  |--------------- |--------------- |
|Logout functionality   |       1        |       5        |
|:--------------------  |--------------- |--------------- |
|Search functionality   |       3        |       3        |
|:--------------------  |--------------- |--------------- |


### Future Features
This project will be maintained in the future for the purpose of a job portal.
Some features that I would like to implement are listed below.
* Allow for the use of social sign ins.
* Better form validation.
* Add a limit for job postings by recruiters
* For more job posts implement a payment
* Add create/ generate CV section for candidations
* Implement better filters
* User permissions / groups to allow staff to have non-breaking access to the CMS.
* Further improve user experience.
* Add a FAQs, subscribers list, and contact section.

## Marketing <a name="marketing"></a>

+ This site has a link to Lyhnidas Social Pages (Facebook, twitter, LinkedIn and gmail adresse) with a link on the page footer.

## Technologies Used <a name="tech"></a>

* [HTML](https://en.wikipedia.org/wiki/HTML)
	* This project uses HTML as the main language used to complete the structure of the Website.
* [CSS](https://en.wikipedia.org/wiki/CSS)
	* This project uses custom written CSS to style the Website.
* [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
    * JavaScript is used on multiple pages to manipulate the DOM.
* [Python](https://www.python.org/)
    * This projects core was created using Python, the back-end logic and the means to run/view the Website.
    * Python Modules used (These can be found in the requirements.txt project file):
* [Django](https://en.wikipedia.org/wiki/Django_(web_framework))
    * This project was created using the Django framework, the back-end logic and the means to run/view the Website.
* [Bootstrap](https://getbootstrap.com/)
    * The Bootstrap framework 4 was used through the website for layout and responsiveness.
* [Google Fonts](https://fonts.google.com/)
	* Google fonts are used in the project to import the fonts for the site.
* [GitHub](https://github.com/)
	* GithHub is the hosting site used to store the source code for the Website, as well as github projects to manage the planning and implementation of all functionality using a kanban board. 
* [Gitpod](https://gitpod.io/)
	* Gitpod is used as version control software to commit and push code to the GitHub repository where the source code is stored.
* [Heroku](https://dashboard.heroku.com/apps)
    * Heroku was used to deploy the live website.
* [Google Chrome Developer Tools](https://developers.google.com/web/tools/chrome-devtools)
	* Google chromes built in developer tools are used to inspect page elements and help debug issues with the site layout and test different CSS styles.
* [Font Awesome](https://fontawesome.com/)
    * All the Icons displayed throughout the website are Font Awesome icons.
* [Favicon](https://favicon.io/)
    * Favicon.io was used to make the site favicon 
* [Cloudinary](https://cloudinary.com/)  
    * Cloudinary is an end-to-end image and video-management solution for websites and mobile apps, covering everything from image and video uploads, storage, manipulations, optimizations to delivery.
* [humanize](https://github.com/Humanizr/Humanizer) 
    * Provides an easy human readable time format when viewing posts.
* [crispyforms](https://django-crispy-forms.readthedocs.io/en/latest/#) 
    * To render django forms in an elegant manner and one which interacts very well with bootstrap styling.
* [AutoSlug](https://django-autoslug.readthedocs.io/en/latest/)
    * To generate slug
* [django-countries](https://pypi.org/project/django-countries/)
    * A Django application that provides country choices for use with forms, flag icons static files, and a country field for models.
* [django_filters](https://pypi.org/project/django-filter/)
    * Django-filter is a reusable Django application allowing users to declaratively add dynamic QuerySet filtering from URL parameters.
* [cities_light](https://pypi.org/project/django-cities-light/)
    * This add-on provides models and commands to import country, subregion, region/state, and city data in your database.
    (Removed from project/ Not used)
* [django_summernote](https://pypi.org/project/django-summernote/)
    * Allows to embed Summernote into Django very handy. Support admin mixins and widgets.





