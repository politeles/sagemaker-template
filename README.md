# Sagemaker template for VS code with remote containers in windows
Template project for Sagemaker in Visual Studio Code with remote containers.

The problem we solved here is the use of Sagemaker in windows (SDK not available for windows). To do so, we are creating a remote container (using Docker & WSL2 in windows) so, the entire development is done within the container.

The base image of the container can be found in the *.devcontainer* folder. 

The *requirements.txt* file contains all the dependencies for python.

Finally, the *app.py * file is an example of executing a hugging face sentiment analysis task.

Once you launch the container, you can connect with your browser to port 9000 (look at the console output after the build).