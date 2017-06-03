# Reconstruction-of-Color-Image-Using-Principal-Component-Analysis-PCA-

While reviewing linear algebra, I decided to work on some funny projects that will help me to understand the concepts more deeply. In this repo, I have reconstructed a [600,600,3] RGB image using PCA. To undestand this project, one may need to have solid knowledge of eigendecomposition and covariance matrix. I have another repository where i have included these concepts with python codes, basically using Numpy. Feel free to have a look there!

The input image:

![dhoni](https://cloud.githubusercontent.com/assets/24511419/26755123/c98b4234-48a8-11e7-93ee-bf101afa7e33.jpg)

with 10 principal components:

![screenshot from 2017-06-03 22-09-09](https://cloud.githubusercontent.com/assets/24511419/26755177/e91a7646-48a9-11e7-8fbe-f2c67579de05.png)

20 Principal Components:

![screenshot from 2017-06-03 22-09-53](https://cloud.githubusercontent.com/assets/24511419/26755176/e918ebaa-48a9-11e7-837f-0b856f2c4d1b.png)

50 Principal Components:

![screenshot from 2017-06-03 22-10-33](https://cloud.githubusercontent.com/assets/24511419/26755178/e9256600-48a9-11e7-9193-973a34f15162.png)

100 Principal Components:

![screenshot from 2017-06-03 22-11-27](https://cloud.githubusercontent.com/assets/24511419/26755179/e9271572-48a9-11e7-93e7-448a592b573c.png)

Using first 100 PCs, a quite good image has been recontructed. Remember our input image had 600 columns, so we had 600 PCs in our eigendecomposition step. So, clearly a great dimension reduction is possible using PCA analysis on any image. 

I have added two .py files here. One is main fuction to do it and another is my practice file which I did fo myself but that's too helpful if anyone wants to understand each steps more clearly. 

To run the code on ubuntu, save input file "dhoni.jpg" and "image_reconstruction_using_PCA.py" in same directory and run the .py file. However, install all required packages before running the code. You can use this code on any image, with a bit of change, for similar purpose. 
