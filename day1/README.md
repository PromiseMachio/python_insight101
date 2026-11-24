#Learing how to use Git
This are basic ways to play around with the your projects in the github (hoslting server).

## Git clone
--- 
This is a code for copying a repository data from the github to your local machine so that you can work on 
---
## ls
---
This is a list function - it lists all the features that are in our cloned project
---
#Functions that are inside the git 
## git -init
---
When the repository for instance is not cloned it is initialized by git init but at the moment since one cloned the project it is not initialize 
---
## git add
---
git add is adding the files that you want to track
---
## git remote -v
---
This enables you to check if the repositorate exists or not => What if the repo doesnt exist what now ...
For case where the project was not cloned but one started to work on it just form scratch they are now able to create the git repo and add the repo to their project using git add remote <https://github.com/<username>/<projectname>>
---
## git status
---
Checking the status of your initial staged files -tracked or untracked
---
## git commit -m
---
This is the message you want to push your files with to github
---
## git push 
---
This enables us to push the files to github server 
For the first time we will use git push -u origin main , or git push -u origin master depending on how you want it to be.
---

# HTML & CSS
---
Here we are just to check something called specificity:
In a case of conflicting tags like a class and id refer to one data / text for instance and class refers to the elements and add colour blue to the elements and id refers to it with color red. You will find the element having color red instead. So specificity rank starts from 
Inline styles => IDs => Classes => Elements => Universal selectors 
---
## Viewport and media queries
---
This are the ability of the content to scale and to respond to different screens sizes eg mobile, laptop, tablet
---
## Flexbox 
---
Wraping elements to the next line if there is no enough space for them in the screen to avoid overflow and items to scale perfectly in different screens.
---
```
    .box{
        display: flex;
        flex-wrap: wrap;

    }
```
## Grid
---

---