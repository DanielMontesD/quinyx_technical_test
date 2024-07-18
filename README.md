# quinyx_technical_test
Associate Technical Consultant test

1.	How long did you take to complete the technical test?

It took me about 1 hour and 40 minutes to complete. Most of my time was spent on task 2 part 1 because I was not able to retrieve the information from the provided link.

2.	Was it easy or challenging? Which parts of the test was easy, and which was challenging?

For Task 2, Part 1:

Fortunately for me, I had used Flask in my last university project, so I had some knowledge about how it works, which made it easier to create the application. I would say my biggest problem was remembering how GitHub works to make commits and push requests. However, the most challenging part was getting the link http://localhost:5000/getJokes to work. This part took the most time because I got stuck here. As you can see in the code, I solved it by accessing another URL that I found on the web for this purpose.

For Task 2, Part 2:
I found it to be a straightforward and generally simple task. I had to refresh my memory a bit, but I have used Pandas on multiple occasions, such as in university or courses. The part that took the most time was understanding how to format the 'Time' column as shown in the provided image since I had never seen this type of format before. After researching online, I found that it was formatted using ISO8601, but even then, it didn't give me the exact format. Using the code I found, I formatted as %Y-%m-%dT%H:%M:%SZ but this didn’t work so I manually added the zeros with %Y-%m-%dT%H:%M:%S.0000000Z.

3.	What resources did you use to learn how to solve the test (i.e. Google, forums, books)?

Most of the resources I found were through Google, Stack Overflow, and GeeksforGeeks. For the general functionality of the Flask application, I relied heavily on my old code since it had some similar parts that helped me solve this problem. To refresh my memory on how GitHub works, I watched a YouTube video.

Here are the links I used:

https://www.youtube.com/watch?v=eLmpKKaQL54&ab_channel=SoftwareEngineerTutorials

https://stackoverflow.com/questions/18618288/how-do-i-convert-dates-into-iso-8601-datetime-format-in-a-pandas-dataframe

https://api.chucknorris.io/

4.	Briefly describe the process that you went through to find the solution for the problem.

To solve the problem, I first read the assignment carefully to understand what was required and to grasp each part. When coding, I started with simple tests, such as creating the /home route to print a simple message and see if the application would work. Next, I created the /getJokes route along with the function to fetch 10 jokes. Seeing that each joke had more information like ID and other details, I decided to append only the necessary part, which in this case was the 'value' (the joke itself).

For Part 2, I simply checked that the data was complete and proceeded to manipulate the DataFrame using Pandas functions.

5. Are there any other key experiences/notes that you would like us to know in regard to your experience in taking the test?

I don't have much to add, except that it was great to revisit something I'm passionate about and see that I could successfully make it work.
