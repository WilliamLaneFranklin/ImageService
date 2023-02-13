# ImageService

This is a microservice that takes the name of a city and returns a url to a public, free image of that city.

Requesting Data

To request the image url, a string in the format "City, State" or "City, Country" (with the capitalizations) must be entered into the readIn.txt file. Example: Sarasota, Florida. Example: Madrid, Spain. In some cases, you can get away with only entering the name of the city and still getting a correct result, but the easiest way to control for a correct request is to use the recommended format. The microservice simply checks whether the file is empty or not. After it reads the string from the file it erases the contents and after the image is served it continues to check if the file is empty or not.

Receiving Data

To receive the image url, a string of the url is written to the writeOut.txt file. Right now, the micrsoervice also prints the url to the console just for the sake of demonstration but this can of course be removed before using the service. The main app simply needs to read from the writeOut.txt file and see if a url is present or if the file is empty. 

![image](https://user-images.githubusercontent.com/102389851/218574401-99e04f40-eca3-4f68-b5e1-f5f93c7c6d6a.png)
