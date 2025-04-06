# ONE-WAY JOB DISCOVERY PLATFORM 

In today’s fast paced job market, thousands of jobseekers apply through a website where third part recruiters,<br /> 
redundant application processes and complex portals which challenge applicants. To simplify the job search, <br />
the One-Way Job Discovery Platform helps them navigate the applicants to the right employer – without any middleman involved. <br /> 
This website bridges the gap between the seekers and job listings. This application is a web-based platform that connects jobseekers to get their desired dream job.Allowing jobseekers to connect with employers directly via email allowing efficient browsing and application of job postings enabling transparency. This website helps small businesses as well as large businesses, by allowing them to post their jobs online. </br> The application is built using Django, a high-level programming language using Python web framework supporting CRUD operations on job postings. Employers can create, read, update and delete for the jobs that were posted, and users can generally view the jobs around the places and apply for the same. <br /> With a focus of clear and concise job posts, users can focus on their job hunt independently <br />
without the need for applying online. This application uses CI/CD pipeline for seamless and reliable interaction between integration and deployment. As this project’s future enhancements are increasing the verification process for the employers, enhancing profile integrations to optimize them, as its current scope prioritizes one-on-one job viewing experience seamlessly.

# Architecture Diagram

![image](https://github.com/user-attachments/assets/ddb68291-f2b4-429a-9043-288dceed30bc)

# VI.	CONTINUOUS INTEGRATION, DELIVERY AND DEPLOYMENT (CI/CD)
CI/CD is vital in today's software development. It allows developers to automatically code, test build and deploy applications. As a result it enhances productivity, guarantees code quality and accelerates the delivery cycle through automation and regular feedback. <br />
A.	Continuous Integration (CI) <br />
A critical aspect of modern software development is continuous integration. The concept is all about automating the integration of code changes made by different developers into a shared repository. Developers often upload their changes to the central repository, and every time this happens, automated build and test execute. This way, the following benefits could be achieved:
•	Spot the bugs. Get the errors in the early stages of the process
•	Automate the testing and code review process to ensure consistent code quality.
•	Enabling frictionless collaboration for individual developers or teams is vital.
B.	Continuous Delivery (CD) <br />
Continuous Delivery takes CI forward by making the release process automatic. This means that every code change triggers a sequence of events to prepare the code to be deployed. The aim is to always keep the codebase in a potentially deployable state. This includes: <br / >
•	Building the application. <br / >
•	Running automated tests. <br / >
•	The provisioning of the necessary infrastructure for the deployment is required <br / >
This Always prepares for deployment in a state application should exist in with minimal human touch. <br / >
C.	Continuous Deployment <br / >
Continuous Deployment advances one step by automating all of the process, which includes deployment in production environments. Continuous Deployment, when coupled with CI/CD that is correctly implemented, has the capacity to allow for the automatic deployment of code alterations if all checks and tests pass for the application to be deployed.

# CI/CD Pipeline
The entire pipeline traverses stages of integration delivery, deployment, which are usually regarded as CI/CD stages, and it involves the following steps: <br / >
<br / >
•	Source Stage: Integration of the code from distinct branches put forward by various developers. <br / >
•	Build Stage: This stage consists of building and testing integrated codebase.<br / >
•	Testing: The execution of automatic tests is conducted to check the quality of the code<br / >
•	Security levels of the audit process are performing vulnerability scanning using Bandit.<br / >
• Code Quality tested using Pylint. <br / >
•	The Deployment Step includes Deploying the application to production or staging environments.<br / >

![image](https://github.com/user-attachments/assets/b588e1a5-4fb0-4b3e-a961-a0986317d12e)

![image](https://github.com/user-attachments/assets/84817a31-6faa-460a-be02-8af5a3f3071d)

![image](https://github.com/user-attachments/assets/4ab0d24e-1144-44ab-9631-b6b3b80c9e02)

# Home Page
![image](https://github.com/user-attachments/assets/061aeb51-69ef-45ae-8f5a-da8cab17ed04)

# Login page
![image](https://github.com/user-attachments/assets/3f5eeea0-0ce7-409c-ba5a-1e729838bc86)

# Profile page
![image](https://github.com/user-attachments/assets/1fc1d53a-7abb-42ac-be84-709baccd25e8)

# Employers page
![image](https://github.com/user-attachments/assets/3f31c92e-fefa-44c5-b745-f1261a2b159d)





