# Build the Docker image
docker build -t jupyter-graphviz .

# Run the Docker container and mount the current directory
docker run -rm -p 8989:8888 -v $pwd:/app jupyter-graphviz

 sudo podman run --rm -it -p 8989:8888 -v $(pwd):/home/ibrahim/app --name graphviz-dev jupyter-graphviz 
# Install and set path for Graphviz

> https://graphviz.org/download/

>>set PATH=%PATH%;C:\Graphviz\bin 