# dronebees

AWS Lambda function returns a bee density in a hypothetical orchard.
The objective is to poll the service and determine where the beehives are located.

This function will be a superposition of 3D gaussians so to make things easy let's use numpy. 
This in turn requires creating a zip file of the folder.
