# Lyhnidas Your Job Coach Testing

:arrow_left: [Return to the README](READEME.md)

## Table of Contents
- [Performance](#performance)
  - [Lighthouse Performance](#lighthouse-performance)
- [Code Validation](#code-validation)
  - [HTML Validation](#html-validation)
  - [CSS Validation](#css-validation)
  - [JS Validation](#js-validation)
  - [PEP8 Validation](#pep8-validation)
- [Testing](#testing)
  - [Manual Testing (BDD)](#manual-testing-bdd)

# Performance

## Lighthouse Performance

![Lighthouse](https://res.cloudinary.com/dmlbtywv4/image/upload/v1680379501/lighthouse_shw1ob.png)

*Go back to the [top](#table-of-contents)*

---

# Code Validation

## HTML Validation

The [W3C Markup Validation Service](https://validator.w3.org/) was used to validate the HTML of the website.

[HTML Validation](https://res.cloudinary.com/dmlbtywv4/image/upload/v1680379501/HTMLValidator_u8fcg0.png)

*Go back to the [top](#table-of-contents)*

---

## CSS Validation

The [W3C Jigsaw CSS Validation Service](https://jigsaw.w3.org/css-validator/) was used to validate the CSS of the website. The CSS passes with 0 errors.

[CSS Validation](https://res.cloudinary.com/dmlbtywv4/image/upload/v1680379502/CSSValidator_yvficg.png)


*Go back to the [top](#table-of-contents)*

---

## JS Validation

[JSHint](https://jshint.com/) was used to validate the JavaScript/Jquery of the website. No major issues were found.


*Go back to the [top](#table-of-contents)*

---

## PEP8 Validation

For the python validation I used CI Python Linter ny Code Institute. The final flagged files were checked in [PEP8 Online](https://pep8ci.herokuapp.com/#)). The only issues found were a few longer lines in the base project's settings.py, models.py and webhook_handler.py and migrations files due to HTML blocks.

*Go back to the [top](#table-of-contents)*

# Testing

## Manual Testing (BDD)

BDD, or Behaviour Driven Development, is the process used to test user stories in a non-technical way, allowing anyone to test the features of an app.

User Story | BDD Test | Pass
--- | --- | :---:
As a first time user<br>I want to know what is expected of me on the home page<br>So that I can read some blog posts navigate the site and decide on whether or not I want to sign up | Given that I'm a first time user<br>When I view/scroll down the homepage<br>Then I should see what the purpose of the site is, easy navigation, a link to sign up and some news stories | :white_check_mark:
As a first time user<br>I want to be able to<br>search and read job posts, So that I can<br>decide on whether or not I think it is worth signing up to. | Given that I'm a first time user<br>When I view/scroll down the homepage<br>Then I read job posts, a link to sign up.  | :white_check_mark:
As a first time user<br>I want to be able to<br>know how to sign up to the web site easily and create a profile. So that I can<br>apply and search for other job posts. | Given that I'm a first time user<br>When I sign up to the web site<br>apply and search for other job posts. | :white_check_mark:
As a Site User<br>I want to be able to<br>easily register a profile. So that I can<br>create a profile and access the main functionality of the site. | Given that I'm a site user<br>When I register a profile<br>Then I can access the main functionality of the site | :white_check_mark:
As a Site User<br>I want to be able to<br>easily login/log out. So that I can<br>access my information without filling in forms every time and ensure the security of my account. | Given that I'm a site user<br>When I login/log out<br>Then I can access my information without filling in forms every time and ensure the security of my account | :white_check_mark:
As a Site User<br>I want to be able to<br>search different job posts. So that I can<br>identify specific jobs and not waste time looking at other job posts. | Given that I'm a site user<br>When I search the type of job, or location<br>Then I should see see the posts and be able to click and read the details of a job post | :white_check_mark:
As a Site User<br>I want to be able to<br>search for a job post by title or location. So that I can<br>find a specific post I'd like I am interested in. | Given that I'm a site user<br>When I use the search bar<br>Then I should see specific post/s that match my search query | :white_check_mark:
As a Site User<br>I want to be able to<br>create/read/update/remove a job post. So that I can<br>alter how I would like my post to look to allow for maximum engagement. | Given that I'm a site user<br>When I choose create/read/update/delete a job post<br>Then I should receive a confirmation message and all functionality works as expected | :white_check_mark:
As a Site owner<br>I want to be able to<br>review all job posts, applicants, users,  etc.	So that I can<br>maintain the site and remove any offensive content. | Given that I'm a Site owner<br>When I navigate to the admin<br>Then I should see all posts, candidats, recruiters, users, etc. | :white_check_mark:
As a Site owner<br>I want to be able to<br>edit/update/delete a post.	So that I can<br>maintain the site and remove any offensive content. | Given that I'm a Site owner<br>When I navigate to the admin<br>Then I should see be able to control all content on the website | :white_check_mark:
As a Site owner<br>I want to be able to<br>direct users to my social profiles. So that I can<br>increase social interaction and attract new users. | Given that I'm a Site owner<br>When I view/scroll down to the footer<br>Then I should see working links to my social media profiles | :white_check_mark:
As a Site owner<br>I want to be able to ensure<br>all areas of the site to function correctly and have no bugs. So that I can<br>ensure an enjoyable browsing experience for all newcomers. | Given that I'm a Site owner<br>When I check all site functionality<br>Then I should see that everything works as expected, there are no bugs and all links and forms work as expected | :white_check_mark:

*Go back to the [top](#table-of-contents)*

---


