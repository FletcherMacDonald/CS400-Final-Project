Project Title: Rehab Revive

Group Name: OrangeOS

Group Members: Fletcher MacDonald, Alexis-Rachelle Ramelb, Wilneris Carrion-Colon

Link to API Documentation: 
[https://documenter.getpostman.com/view/42594454/2sB2ca7L7F]

How to Run Software Application: 
1. Go to the CS400-Final-Project repo and into the 'current-website-branch-2' branch and clone the repository to your computer locally using: 
```python
git clone --branch current-website-branch-2 https://github.com/FletcherMacDonald/CS400-Final-Project.git
```

2. Open up your terminal and cd into the CS400-Final-Project folder.

3. Run:
```python
docker-compose up --build
```

4. Go to your browser and in open the url:
[http://127.0.0.1:5555/]

5. You are now in the webpage, feel try to browse through and open the tabs/other pages (Medical Imaging, Physical Therapy, and Orthopedics). Use our "Add Clinic" feature to add a clinic to any of those three pages. For our DELETE request, open Postman and utilize http://127.0.0.1:5555/delete/<clinic_name> to delete a Medical Imaging clinic. For example, in Postman, if you enter http://127.0.0.1:5555/delete/Kuakini Plaza Imaging, it will delete that medical imaging clinic from the page.

Enjoy!
