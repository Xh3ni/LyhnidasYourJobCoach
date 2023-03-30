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







